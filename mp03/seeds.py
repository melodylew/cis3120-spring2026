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
#  Financial Services (default seed: 14 companies across sub-segments)
# ──────────────────────────────────────────────────────────────────────────

FINANCIAL_SERVICES_TICKERS = [
    # Money-center banks
    "JPM", "BAC", "WFC", "C",
    # Regional banks
    "PNC", "USB", "TFC",
    # Asset management
    "BLK", "BX",
    # Insurance
    "MET", "PRU",
    # Payments
    "V", "MA", "AXP",
]

FINANCIAL_SERVICES_PHRASES = [
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
# ─────────────────────────────────────────────────────────────────────────────
# Retail (added by Jenna: 14 companies across sub-segments)
# ─────────────────────────────────────────────────────────────────────────────

RETAIL_TICKERS = [
    # Big-box / general merchandise
    "WMT", "TGT", "COST",
    # Home improvement
    "HD", "LOW",
    # Off-price / discount / dollar
    "TJX", "ROST", "DG", "DLTR",
    # Drug stores
    "WBA", "CVS",
    # Specialty
    "BBY", "GPS",
    # Grocery
    "KR",
    # Additional sub-segments (extended by Jenna)
    # Department stores
    "M", "KSS",
    # Off-price extension
    "BURL",
    # Beauty specialty
    "ULTA",
    # Discount specialty
    "FIVE",
    # Auto retail
    "AAP",
]

RETAIL_PHRASES = [
    # Store openings
    '"new store"',
    '"store opening"',
    '"grand opening"',
    '"flagship store"',
    # Store closings / consolidation
    '"store closure"',
    '"store closing"',
    '"store closures"',
    '"store consolidation"',
    # Distribution / supply chain real estate
    '"distribution center"',
    '"fulfillment center"',
]

