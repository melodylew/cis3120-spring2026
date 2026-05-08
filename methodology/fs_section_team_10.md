# Financial Services — Methodology Contribution (Team 10)

> **Author:** Financial Services Pipeline Lead
> **For the integrator:** these three sections drop into the team
> methodology document under the indicated headings. The window-trial
> table and Stage 3 quality observations get filled in after the pipeline
> run; placeholders are marked **TBD** below.

---

## 1. Ticker-list rationale (Financial Services)

The instructor-seeded list of 14 tickers covers money-center banks, three
regionals, two asset managers, two insurers, and the three card networks.
Section 3 of the assignment explicitly notes this seed is biased toward
retail-banking events and undercounts capital-markets activity. We
extended the list to **25 tickers**, keeping every seed ticker and adding
eleven names across four under-represented segments:

**Mid-cap regional banks** (FITB, RF, KEY). Branch consolidation and
operations-center relocation activity is most concentrated in mid-cap
regionals, not at the money-centers, because mid-caps are still
rationalizing post-2008 acquisitions and have less consolidated
footprints than the top four.

**Capital markets / investment banks** (GS, MS). Pure investment banks
file location 8-Ks for trading-floor relocations, headquarters moves,
and EMEA / APAC office shifts. The seed had zero capital-markets
coverage, which would systematically bias our map toward retail
geography (suburbs, secondary cities) and away from the financial
centers (Manhattan midtown, Chicago Loop, Jersey City) where
capital-markets capacity actually sits.

**Custody and trust banks** (BK, STT, NTRS). Custody banks operate the
largest operations centers in the industry by headcount and are
unusually frequent filers of operations-center relocation 8-Ks.
Entirely absent from the seed.

**Exchanges** (ICE, CME, NDAQ). Exchanges file 8-Ks on data-center moves
and matching-engine relocations. Including them surfaces a class of
location event (low-latency-driven data-center geography) that no bank
or asset manager produces.

**Brokerage, consumer finance, and alternative asset management** (SCHW,
ALLY, KKR). Rounded out the corpus where the seed had obvious
single-name representation only.

**Names considered but excluded:** small-cap fintechs (small footprint,
infrequent real-estate 8-Ks), pure-play insurers beyond MET and PRU
(insurance location events tend to be obscured inside larger annual
filings rather than stand-alone 8-Ks), and additional alternative
managers beyond KKR (low expected location-event density).

## 2. Search-phrase rationale (Financial Services)

The seeded ten phrases are heavy on retail-branch language. We extended
to **23 phrases** across four buckets, keeping every seed phrase:

**Corporate real estate** — `"headquarters relocation"`,
`"relocate its headquarters"`, `"new headquarters"`,
`"lease termination"`, `"office relocation"`. Captures HQ moves and
lease decisions that the retail-branch vocabulary misses entirely.

**Capital-markets-specific infrastructure** — `"trading floor"`,
`"matching engine"`, `"exchange floor"`. Targets the gap the assignment
explicitly flagged. These phrases produce essentially no hits outside
capital markets, so precision is high.

**Consolidation and footprint reduction** — `"footprint reduction"`,
`"consolidate operations"`, `"office consolidation"`. Picks up
cost-rationalization filings that don't use the word "branch", which
matters because some of the most interesting consolidation 8-Ks
(white-collar operations, not retail) avoid retail-branch vocabulary.

**Expansion language** — `"expanded presence"`, `"new office"`. Added
on the expansion side so the corpus is not structurally biased toward
consolidation alone — important for the comparative reflection's
ability to compare expansion-vs-consolidation balance across
industries.

**Phrases considered but excluded:** `"office"` alone (false-positive
rate is prohibitive — every governance section mentions "office"),
`"closing"` alone (matches every loan-closing event in bank 8-Ks),
and `"relocation"` alone (matches employee-relocation benefit
disclosures).

## 3. Stage 3 classification quality (Financial Services)

> **TBD — populated after the FS pipeline run.** Items to fill in:
>
> - Total candidates after Stage 1 + ticker filter: ___
> - Records flagged `is_location_event=True`: ___
> - Records that survived geocoding: ___
> - Sampled false positives (model said location event, but on read-through it was not): case 1 [accession, why]; case 2 [accession, why]
> - Sampled false negatives (model said no, but on read-through it was): case 1 [accession, why]
> - Recall vs precision posture: do we lean toward including ambiguous cases (recall) or excluding them (precision)? Defended.
> - Geographic coverage check: any obvious clusters or gaps?

## 4. Limitations specific to the FS slice

> **TBD — populated after the run.** Items likely to surface:
>
> - Geocoding granularity: many 8-Ks list state but not city, forcing a state-centroid placement. This is acceptable for the comparative map but the integrator should note it in the team methodology.
> - Recency vs comparability: a long window improves event count but mixes 8-Ks filed under different macro conditions. We document the chosen window and its tradeoffs in the team window-experiment section.
> - Capital-markets coverage skew: even with the expanded ticker list, capital-markets location 8-Ks are still rare relative to retail-branch 8-Ks because investment banks consolidate location events into their 10-Q / 10-K rather than filing stand-alone 8-Ks. Our event counts will probably still skew retail, just less than the seed.