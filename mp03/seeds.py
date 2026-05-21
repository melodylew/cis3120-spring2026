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
# Retail (added by Jenna: 20 companies across nine sub-segments)
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
    # Round 3 additions
    # Apparel / fashion
    "AEO", "URBN", "ANF", "LULU", "PLCE", "CRI", "GES", "EXPR", "BKE",
    "ZUMZ", "CAL", "FL", "GCO", "DBI", "JWN", "PVH", "RL", "VFC",
    "TPR", "CPRI", "LEVI", "FIGS",
    # Pet retail
    "CHWY", "PETQ", "WOOF",
    # Office / business supplies
    "ODP",
    # Furniture / home
    "W", "RH", "WSM", "ETD", "LZB", "ARHS", "HVT",
    # E-commerce / online
    "AMZN", "EBAY", "ETSY", "OSTK",
    # Sporting / outdoor / hobby
    "DKS", "ASO", "HIBB", "BOOT", "VSTO",
    # Convenience / wholesale
    "CASY", "BJ",
    # Auto parts
    "ORLY", "AZO",
    # Beauty / personal care
    "SBH", "ELF", "COTY",
    # Discount / closeout
    "OLLI", "BIG", "PSMT",
    # Mattress / specialty home
    "TPX", "SNBR", "PRPL",
    # Crafts / hobby
    "MIK",
    # Vitamins / health
    "GNC", "VSI",
    # Jewelry
    "SIG", "TIF",
    # Toys
    "FNKO",
    # Grocery extension
    "SFM", "ACI", "WMK", "GO",
    # Drug store extension
    "RAD",
    # Convenience / fuel retail
    "MUSA",
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
    # Additional phrases (extended by Jenna)
    '"new location"',
    '"warehouse opening"',
    '"distribution facility"',
    '"store relocation"',
    '"new format"',
    '"omnichannel hub"',
    # Round 3 additions
    '"opened a new"',
    '"announced the opening"',
    '"plans to open"',
    '"plans to close"',
    '"to close"',
    '"will close"',
    '"announced the closure"',
    '"closing stores"',
    '"closure of"',
    '"new outlet"',
    '"new market"',
    '"market entry"',
    '"market expansion"',
    '"first store"',
    '"open its first"',
    '"opening of"',
    '"expanding"',
    '"expansion"',
    '"closing"',
    '"opening"',
    '"new facility"',
    '"facility opening"',
    '"facility closure"',
    '"new corporate office"',
    '"new headquarters"',
    '"headquarters relocation"',
    '"office relocation"',
    '"branch"',
    '"new branch"',
    '"showroom"',
    '"new showroom"',
    '"new club"',
    '"club opening"',
    '"prototype store"',
    '"concept store"',
    '"pilot store"',
    '"pop-up store"',
    '"pop-up shop"',
    '"store remodel"',
    '"remodeled store"',
    '"new market launch"',
    '"launch"',
    '"opened"',
    '"closed"',
    '"acquisition of"',
    '"divestiture"',
    '"sale-leaseback"',
    '"real estate"',
    '"property acquisition"',
    '"lease termination"',
    '"facility consolidation"',
    '"network optimization"',
    '"footprint reduction"',
    '"footprint expansion"',
    '"new region"',
    '"regional expansion"',
    '"international expansion"',
    '"new country"',
    '"new state"',
    '"new city"',
]

