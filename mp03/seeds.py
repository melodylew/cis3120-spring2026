"""
Seeded data for Mini-Project MP03 — Press Release to Plot: Industry Comparison.

These lists are starting points provided by the instructor. Teams are expected
to modify both the ticker lists and the phrase lists during the project.
Modifications must be justified in the methodology section.

The seeds were chosen to give each industry a working starting point, not to
be optimal. The Financial Services seed is biased toward retail-banking events
and undercounts capital-markets activity; the Travel and Hospitality seed
mixes hotel-style and airline-style location events that may warrant separate
treatment in your map. Identifying these limitations and proposing fixes is
the methodology section's purpose.

Reference: docs/MP03_Assignment.docx, Section 3.
"""

# ──────────────────────────────────────────────────────────────────────────
#  Financial Services (Team 10 expanded list: 25 tickers, 23 phrases)
#
#  Extended from the instructor seed (14 tickers, 10 phrases). The seed was
#  biased toward retail-banking events and undercounted capital markets,
#  custody, and exchanges. Additions broaden coverage across four
#  under-represented segments and add corporate-real-estate, capital-markets,
#  and consolidation-specific phrase vocabulary. Rationale lives in
#  methodology/mp03_methodology_team_10.md.
# ──────────────────────────────────────────────────────────────────────────

FINANCIAL_SERVICES_TICKERS = [
    # --- Money-center banks (seed; kept) ---
    "JPM", "BAC", "WFC", "C",
    # --- Regional banks (seed; kept) ---
    "PNC", "USB", "TFC",
    # --- Regional banks (added: mid-cap regionals where consolidation activity is concentrated) ---
    "FITB",  # Fifth Third Bancorp
    "RF",    # Regions Financial
    "KEY",   # KeyCorp
    # --- Capital markets / investment banks (added: closes the seed's biggest gap) ---
    "GS",    # Goldman Sachs
    "MS",    # Morgan Stanley
    # --- Asset management (seed kept + 1 added) ---
    "BLK", "BX",
    "KKR",   # KKR -- alternative asset manager, frequent office-expansion 8-Ks
    # --- Custody / trust banks (added: largest ops centers in the industry, absent from seed) ---
    "BK",    # Bank of New York Mellon
    "STT",   # State Street
    "NTRS",  # Northern Trust
    # --- Exchanges (added: data-center / matching-engine relocations) ---
    "ICE",   # Intercontinental Exchange (NYSE parent)
    "CME",   # CME Group
    "NDAQ",  # Nasdaq
    # --- Brokerage / consumer finance (added) ---
    "SCHW",  # Charles Schwab
    "ALLY",  # Ally Financial
    # --- Insurance (seed; kept) ---
    "MET", "PRU",
    # --- Payments (seed; kept) ---
    "V", "MA", "AXP",
]

FINANCIAL_SERVICES_PHRASES = [
    # --- Retail branch language (seed; kept) ---
    '"new branch"',
    '"branch opening"',
    '"branch closure"',
    '"branch closing"',
    '"branch consolidation"',
    '"regional office"',
    '"office closure"',
    '"operations center"',
    '"data center"',
    '"new location"',
    # --- Corporate real estate (added: HQ moves and lease decisions) ---
    '"headquarters relocation"',
    '"relocate its headquarters"',
    '"new headquarters"',
    '"lease termination"',
    '"office relocation"',
    # --- Capital-markets-specific infrastructure (added: targets the seed's biggest gap) ---
    '"trading floor"',
    '"matching engine"',
    '"exchange floor"',
    # --- Consolidation / footprint reduction (added: catches non-branch cost-rationalization) ---
    '"footprint reduction"',
    '"consolidate operations"',
    '"office consolidation"',
    # --- Expansion language (added: balances corpus against consolidation bias) ---
    '"expanded presence"',
    '"new office"',
]
# ──────────────────────────────────────────────────────────────────────────
#  Travel and Hospitality (default seed: 14 companies across sub-segments)
# ──────────────────────────────────────────────────────────────────────────

TRAVEL_HOSPITALITY_TICKERS = [
    # Hotels
    "MAR", "HLT", "H", "CHH", "WH",
    # Cruise
    "CCL", "RCL", "NCLH",
    # Airlines
    "DAL", "UAL", "AAL", "LUV",
    # Online travel
    "BKNG", "EXPE",
]

TRAVEL_HOSPITALITY_PHRASES = [
    '"new property"',
    '"new hotel"',
    '"hotel opening"',
    '"resort opening"',
    '"property opening"',
    '"brand conversion"',
    '"new route"',
    '"new gateway"',
    '"new terminal"',
    '"grand opening"',
]
