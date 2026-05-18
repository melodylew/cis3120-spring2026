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
    # Money-center banks (seed)
    "JPM", "BAC", "WFC", "C",
    # Regional banks (seed)
    "PNC", "USB", "TFC",
    # Mid-cap regionals - active branch consolidation filers
    "FITB", "RF", "KEY",
    # Capital markets / investment banks - closes biggest seed gap
    "GS", "MS",
    # Asset management (seed + KKR added)
    "BLK", "BX", "KKR",
    # Custody / trust banks - largest ops centers in the industry
    "BK", "STT", "NTRS",
    # Exchanges - data-center and matching-engine relocations
    "ICE", "CME", "NDAQ",
    # Brokerage and consumer finance
    "SCHW", "ALLY",
    # Insurance (seed)
    "MET", "PRU",
    # Payments (seed)
    "V", "MA", "AXP",
]