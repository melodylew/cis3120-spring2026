"""
MP03 required new functions.

These three functions are specified in Section 3 of the assignment. They sit
on top of the five preserved Module 15 signatures (search_edgar_one_phrase,
build_exhibit_url, fetch_exhibit_text, extract_with_claude, geocode_location),
which the canonical pipeline notebook is expected to import or define before
calling run_industry_pipeline.

Owner: Financial Services Pipeline Lead (Team 10)
Note: filter_candidates_by_tickers and summarize_window_trial are pure
helpers and are shared verbatim across both industry pipelines.
run_industry_pipeline is the orchestration function each lead calls for
their slice.
"""

from datetime import date, timedelta
from typing import Callable


# ---------------------------------------------------------------------------
# Stage 1 candidate filtering
# ---------------------------------------------------------------------------
def filter_candidates_by_tickers(
    candidates: list[dict],
    ticker_list: list[str],
) -> list[dict]:
    """Restrict a Stage 1 candidate set to a list of tickers.

    Each EDGAR hit carries an iterable of associated tickers at
    hit["_source"]["tickers"]. We keep a hit if ANY of its tickers matches
    ANY ticker in ticker_list, case-insensitively. Hits whose _source or
    tickers field is missing are dropped (not raised) because EDGAR
    occasionally returns hits with incomplete metadata and we don't want one
    bad row to abort an entire trial.

    Parameters
    ----------
    candidates : list[dict]
        Raw hits returned by Stage 1 (search_edgar_one_phrase).
    ticker_list : list[str]
        Industry ticker universe; e.g., FINANCIAL_SERVICES_TICKERS.

    Returns
    -------
    list[dict]
        Subset of candidates whose tickers intersect ticker_list.
    """
    allowed = {t.upper() for t in ticker_list}

    filtered: list[dict] = []
    for hit in candidates:
        source = hit.get("_source") or {}
        hit_tickers = source.get("tickers") or []
        # EDGAR sometimes returns tickers as a single string; normalize.
        if isinstance(hit_tickers, str):
            hit_tickers = [hit_tickers]
        hit_tickers_upper = {str(t).upper() for t in hit_tickers}
        if hit_tickers_upper & allowed:
            filtered.append(hit)
    return filtered


# ---------------------------------------------------------------------------
# Full pipeline for one industry slice
# ---------------------------------------------------------------------------
def run_industry_pipeline(
    industry_label: str,
    ticker_list: list[str],
    phrase_list: list[str],
    window_days: int,
    *,
    search_edgar_one_phrase: Callable,
    fetch_exhibit_text: Callable,
    extract_with_claude: Callable,
    geocode_location: Callable,
) -> list[dict]:
    """Run all five canonical pipeline stages for a single industry slice.

    Stages, in order:
      1. Stage 1 -- EDGAR full-text search across phrase_list (one call per
         phrase). Hits are deduplicated by accession number.
      2. Industry filter -- restrict the candidate set to ticker_list using
         filter_candidates_by_tickers. Filter happens BEFORE Stage 3 to
         keep API costs down.
      3. Stage 2 -- fetch exhibit text for each surviving candidate.
      4. Stage 3 -- classify and extract structured event fields with Claude.
         Records where is_location_event is False are dropped.
      5. Stage 4 -- geocode (city, state) to (lat, lon). Records that fail
         geocoding are dropped (the map cannot place them).
      An "industry" field equal to industry_label is stamped on every
      surviving record so the integrator's map can color-code by industry.

    The four Module 15 callables are passed in as keyword arguments rather
    than imported at module top, because the canonical Module 15 functions
    live in the notebook scope and are not packaged as importable modules.
    The notebook supplies them at call time.

    Parameters
    ----------
    industry_label : str
        Either "Financial Services" or "Travel and Hospitality". Stamped onto
        every returned record.
    ticker_list : list[str]
        Industry ticker universe.
    phrase_list : list[str]
        Industry search-phrase list (each entry already wrapped in quotes).
    window_days : int
        Look-back window. end_date = today; start_date = today - window_days.
    search_edgar_one_phrase, fetch_exhibit_text, extract_with_claude,
    geocode_location : Callable
        The four canonical Module 15 stage functions.

    Returns
    -------
    list[dict]
        Geocoded event records, one per surviving filing. Each record
        contains the extract_with_claude fields plus "industry", "lat",
        "lon", and the underlying filing URL.
    """
    end_date = date.today()
    start_date = end_date - timedelta(days=window_days)

    # ----- Stage 1: EDGAR search across all phrases -----
    # Deduplicate by accession number; the same filing can hit on multiple
    # phrases (e.g., "new branch" AND "branch opening" in the same 8-K).
    seen_accessions: set[str] = set()
    candidates: list[dict] = []
    for phrase in phrase_list:
        hits, _total = search_edgar_one_phrase(
            phrase=phrase,
            start_date=start_date,
            end_date=end_date,
        )
        for hit in hits:
            accession = (hit.get("_source") or {}).get("adsh") or hit.get("_id")
            if accession and accession not in seen_accessions:
                seen_accessions.add(accession)
                candidates.append(hit)

    # ----- Industry filter (before Stage 3 to keep API costs down) -----
    candidates = filter_candidates_by_tickers(candidates, ticker_list)

    # ----- Stage 2: fetch exhibit text -----
    fetched: list[dict] = []
    for hit in candidates:
        source = hit.get("_source") or {}
        try:
            exhibit_text, exhibit_url = fetch_exhibit_text(hit)
        except Exception as exc:
            # Network or parser failures on a single filing should not abort
            # the whole pipeline; we drop the row and continue.
            print(f"  [stage2] skip {source.get('adsh', '?')}: {exc}")
            continue
        filing = {
            "accession": source.get("adsh"),
            "ticker": (source.get("tickers") or [""])[0],
            "company_name": (source.get("display_names") or [""])[0],
            "filing_date": source.get("file_date"),
            "exhibit_url": exhibit_url,
            "exhibit_text": exhibit_text,
        }
        fetched.append(filing)

    # ----- Stage 3: classify + extract via Claude -----
    extracted: list[dict] = []
    for filing in fetched:
        try:
            record = extract_with_claude(filing)
        except Exception as exc:
            print(f"  [stage3] skip {filing.get('accession', '?')}: {exc}")
            continue
        # Keep the source fields the downstream map needs.
        record.setdefault("ticker", filing["ticker"])
        record.setdefault("company_name", filing["company_name"])
        record.setdefault("filing_date", filing["filing_date"])
        record.setdefault("exhibit_url", filing["exhibit_url"])
        if record.get("is_location_event"):
            extracted.append(record)

    # ----- Stage 4: geocode -----
    geocoded: list[dict] = []
    for record in extracted:
        coords = geocode_location(record.get("city"), record.get("state"))
        if coords is None:
            continue
        lat, lon = coords
        record["lat"] = lat
        record["lon"] = lon
        record["industry"] = industry_label
        geocoded.append(record)

    return geocoded


# ---------------------------------------------------------------------------
# Window-trial bookkeeping
# ---------------------------------------------------------------------------
def summarize_window_trial(
    industry_label: str,
    window_days: int,
    candidate_count: int,
    event_count: int,
    estimated_cost_usd: float,
) -> dict:
    """Build one row of the window-experiment results table.

    The returned dict matches the column schema in Section 4 of the
    assignment exactly:

        industry            str    "Financial Services" | "Travel and Hospitality"
        window_days         int    one of {30, 60, 90, 180, 360}
        candidate_count     int    rows after filter_candidates_by_tickers
        event_count         int    rows where is_location_event is True
        estimated_cost_usd  float  sum of input + output token cost (Haiku 4.5)

    Returns
    -------
    dict
        Directly appendable to the team's window-trial results table.
    """
    return {
        "industry": industry_label,
        "window_days": int(window_days),
        "candidate_count": int(candidate_count),
        "event_count": int(event_count),
        "estimated_cost_usd": round(float(estimated_cost_usd), 4),
    }
