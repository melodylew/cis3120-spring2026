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
#  Financial Services (Team 10 expanded: 25 tickers, 23 phrases)
# ──────────────────────────────────────────────────────────────────────────

FINANCIAL_SERVICES_TICKERS = [
    # Money-center banks (seed)
    "JPM", "BAC", "WFC", "C",
    # Regional banks (seed)
    "PNC", "USB", "TFC",
    # Mid-cap regionals
    "FITB", "RF", "KEY", "ZION", "CFG", "HBAN", "MTB", "FHN",
    # Smaller regionals with active branch activity
    "BOKF", "WTFC", "CVBF", "IBCP", "UCBI", "SFNC", "FFIN",
    "NBTB", "CTBI", "FULT", "WSBC", "RNST", "HOPE", "BPOP",
    # Capital markets / investment banks
    "GS", "MS", "LAZ", "EVR", "PJT", "HLI",
    # Asset management
    "BLK", "BX", "KKR", "APO", "ARES", "OWL", "CG", "BAM",
    # Custody / trust banks
    "BK", "STT", "NTRS",
    # Exchanges
    "ICE", "CME", "NDAQ", "CBOE", "MKTX",
    # Brokerage and consumer finance
    "SCHW", "ALLY", "RJF", "AMTD", "LPL",
    # Payments and fintech
    "V", "MA", "AXP", "FIS", "FISV", "GPN", "PYPL", "SQ", "WEX",
    # Insurance
    "MET", "PRU", "AIG", "AFL", "CB", "HIG", "TRV", "ALL", "LNC",
    # Specialty finance
    "SLM", "OMF", "CACC", "ELVT", "WRLD",
    # Large regionals with active real estate filings
    "WAL", "EWBC", "COLB", "UMBF", "SNV", "NYCB", "ABCB",
    "HOMB", "IBTX", "TCBI", "GBCI", "FFBC", "IBOC", "CATY",
    # Smaller community banks — frequent branch 8-K filers
    "LKFN", "GABC", "SRCE", "BUSE", "SBCF", "FBNC", "TRST",
    "CHCO", "BSVN", "CFFI", "MOFG", "PPBI", "WABC", "TFSL",
    # Specialty/consumer finance
    "NAVI", "ENVA",
]

FINANCIAL_SERVICES_PHRASES = [
    # Retail branch language (seed)
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
    # Corporate real estate
    '"headquarters relocation"',
    '"relocate its headquarters"',
    '"new headquarters"',
    '"lease termination"',
    '"office relocation"',
    # Capital-markets infrastructure
    '"trading floor"',
    '"matching engine"',
    '"exchange floor"',
    # Consolidation
    '"footprint reduction"',
    '"consolidate operations"',
    '"office consolidation"',
    # Expansion
    '"expanded presence"',
    '"new office"',
    # Facility types
    '"technology center"',
    '"innovation center"',
    '"service center"',
    '"processing center"',
    '"financial center"',
    '"new facility"',
    # Lease and real estate actions
    '"entered into a lease"',
    '"signed a lease"',
    '"office space"',
    '"square feet"',
    '"corporate campus"',
    '"relocated its office"',
    '"new corporate headquarters"',
    '"principal offices"',
    '"executive offices"',
    '"change of address"',
    # Branch network language
    '"branch network"',
    '"retail banking"',
    '"banking center"',
    '"financial center opening"',
    '"de novo branch"',
    '"branch acquisition"',
    '"branch sale"',
    '"banking locations"',
    '"branch locations"',
    '"banking offices"',
    # Workforce / facility consolidation
    '"reduce its real estate"',
    '"office space reduction"',
    '"facility consolidation"',
    '"workforce consolidation"',
    '"shared services center"',
    '"captive center"',
    '"back office"',
    '"middle office"',
    # Announcement-style phrases — signal actual events, not boilerplate
    '"proud to announce"',
    '"pleased to announce"',
    '"officially opened"',
    '"grand opening"',
    '"ribbon cutting"',
    '"will relocate"',
    '"has relocated"',
    '"is relocating"',
    '"will open"',
    '"has opened"',
    '"will close"',
    '"has closed"',
    '"new location at"',
    '"moving to"',
    '"moved to"',
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