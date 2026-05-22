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
    # Hotel brands
    "MAR", "HLT", "H", "CHH", "WH", "IHG",
    "PK", "HST", "RHP", "SHO", "PEB", "APLE", "DRH",
    "XHR", "CLDT","VAC", "TNL", "HGV", "PLYA", "SOND",
    # Cruise
    "CCL", "RCL", "NCLH",
    "VIK", "ACEL",
    # Airlines
    "DAL", "UAL", "AAL", "LUV", "JBLU", "ALK", "ULCC",
    "SKYW", "SNCY", "HA", "MESA", "ATSG", "JOBY",  "ACHR", "BBY", "RJET",
    # Online travel / booking
    "BKNG", "EXPE", "TRIP", "ABNB", "VACQ", "TRVG", "MMYT",
    # Casino / Resorts
    "MGM", "LVS", "WYNN", "CZR", "PENN", "FUN",
    "BYD", "MLCO", "AGS", "SGMS", "CHDN", "DKNG",
    "RSI", "GDEN", "FULL",
    # Theme parks / attractions 
    "DIS", "SIX", "SEAS", "PLBY", "EPR", "CNK",  
    # Car rental / ground transportation 
    "HTZ", "CAR", "UBER", "LYFT",
    "BLDE", "WKHS", 
]

TRAVEL_HOSPITALITY_PHRASES = [
    # Hotels 
    '"new property"',
    '"new hotel"',
    '"hotel opening"',
    '"resort opening"',
    '"property opening"',
    '"brand conversion"',
    '"hotel franchise"',
    '"resort expansion"',
    '"new resort"',
    '"hotel acquisition"',
    '"property acquisition"',
    '"new full-service"',
    '"new select-service"',
    '"new boutique"',           
    '"all-inclusive resort"',   
    '"vacation club"',          
    '"new timeshare"',          
    '"luxury hotel"',           
    '"new inn"',                
    '"extended stay"',         
    # Airlines
    '"new route"',
    '"new gateway"',
    '"new terminal"',
    '"new nonstop"',
    '"new lounge"',
    '"new service"',
    '"new flight"',
    '"new hub"',
    '"new concourse"',          
    '"new maintenance"',        
    '"new crew base"',          
    '"new training center"',    
    # Cruise
    '"new ship"',
    '"port of call"',
    '"new cruise terminal"',
    '"homeport"',
    '"inaugural sailing"',
    '"new itinerary"',
    '"new deployment"',         
    '"new embarkation"',        
    '"private island"',         
    '"new destination"',
    # Casino / gaming
    '"casino opening"',
    '"grand opening"',
    '"new casino"',
    '"new gaming"',
    '"casino expansion"',
    '"new sportsbook"',
    '"retail sportsbook"',
    '"new poker"',              
    '"gaming expansion"',       
    '"new entertainment venue"',
    # Theme parks / attractions 
    '"new attraction"',
    '"park expansion"',
    '"new theme park"',
    '"new experience"',
    '"new ride"',               
    '"new land"',               
    '"new exhibit"',            
    '"new entertainment"',      
    # Car rental / ground transportation 
    '"new location"',
    '"new facility"',
    '"new terminal facility"',
    '"fleet expansion"',
    '"new rental"',             
    '"rental location"',
    '"new shuttle"',
    # Air mobility
    '"new vertiport"',          
    '"new skyport"',           
    '"new air mobility"',      
    '"new charter"',
]