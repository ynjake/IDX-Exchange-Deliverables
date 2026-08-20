"""
Week 1 Deliverable - Monthly Dataset Aggregation
"""

import pandas as pd
import os


def load_month(filename):
    """
    Reads one monthly CSV. If the filename contains '_filled', drops the
    last 2 columns (those files have 2 extra columns we don't need).
    """
    try:
        df = pd.read_csv(filename, low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(filename, low_memory=False, encoding='cp1252')

    if "_filled" in filename:
        df = df.iloc[:, :-2]
    return df


# SOLD FILES

sold1 = load_month('CRMLSSold202401.csv')
sold2 = load_month('CRMLSSold202402.csv')
sold3 = load_month('CRMLSSold202403.csv')
sold4 = load_month('CRMLSSold202404.csv')
sold5 = load_month('CRMLSSold202405_filled.csv')
sold6 = load_month('CRMLSSold202406_filled.csv')
sold7 = load_month('CRMLSSold202407_filled.csv')
sold8 = load_month('CRMLSSold202408.csv')
sold9 = load_month('CRMLSSold202409.csv')
sold10 = load_month('CRMLSSold202410.csv')
sold11 = load_month('CRMLSSold202411.csv')
sold12 = load_month('CRMLSSold202412.csv')
sold13 = load_month('CRMLSSold202501_filled.csv')
sold14 = load_month('CRMLSSold202502.csv')
sold15 = load_month('CRMLSSold202503.csv')
sold16 = load_month('CRMLSSold202504.csv')
sold17 = load_month('CRMLSSold202505.csv')
sold18 = load_month('CRMLSSold202506.csv')
sold19 = load_month('CRMLSSold202507.csv')
sold20 = load_month('CRMLSSold202508.csv')
sold21 = load_month('CRMLSSold202509.csv')
sold22 = load_month('CRMLSSold202510.csv')
sold23 = load_month('CRMLSSold202511.csv')
sold24 = load_month('CRMLSSold202512.csv')
sold25 = load_month('CRMLSSold202601.csv')
sold26 = load_month('CRMLSSold202602.csv')
sold27 = load_month('CRMLSSold202603.csv')
sold28 = load_month('CRMLSSold202604.csv')
sold29 = load_month('CRMLSSold202605.csv')
sold30 = load_month('CRMLSSold202606.csv')
sold31 = load_month('CRMLSSold202607.csv')

# Row count check BEFORE concatenation (sum of each individual month)

sold_rows_before = (
    len(sold1) + len(sold2) + len(sold3) + len(sold4) + len(sold5) + len(sold6)
    + len(sold7) + len(sold8) + len(sold9) + len(sold10) + len(sold11) + len(sold12)
    + len(sold13) + len(sold14) + len(sold15) + len(sold16) + len(sold17) + len(sold18)
    + len(sold19) + len(sold20) + len(sold21) + len(sold22) + len(sold23) + len(sold24)
    + len(sold25) + len(sold26) + len(sold27) + len(sold28) + len(sold29) + len(sold30) + len(sold31)
)
print(f"Sold - rows before concatenation: {sold_rows_before}")

sold = pd.concat([
    sold1, sold2, sold3, sold4, sold5, sold6, sold7, sold8, sold9, sold10,
    sold11, sold12, sold13, sold14, sold15, sold16, sold17, sold18, sold19, sold20,
    sold21, sold22, sold23, sold24, sold25, sold26, sold27, sold28, sold29
], ignore_index=True)

print(f"Sold - rows after concatenation: {len(sold)}")



# Listing Files
# NOTE: Listing files start at 202403 (no 202401/202402 exist on the server)

list3 = load_month('CRMLSListing202403.csv')
list4 = load_month('CRMLSListing202404.csv')
list5 = load_month('CRMLSListing202405.csv')
list6 = load_month('CRMLSListing202406.csv')
list7 = load_month('CRMLSListing202407.csv')
list8 = load_month('CRMLSListing202408.csv')
list9 = load_month('CRMLSListing202409.csv')
list10 = load_month('CRMLSListing202410.csv')
list11 = load_month('CRMLSListing202411.csv')
list12 = load_month('CRMLSListing202412.csv')
list13 = load_month('CRMLSListing202501.csv')
list14 = load_month('CRMLSListing202502.csv')
list15 = load_month('CRMLSListing202503.csv')
list16 = load_month('CRMLSListing202504.csv')
list17 = load_month('CRMLSListing202505.csv')
list18 = load_month('CRMLSListing202506.csv')
list19 = load_month('CRMLSListing202507.csv')
list20 = load_month('CRMLSListing202508.csv')
list21 = load_month('CRMLSListing202509.csv')
list22 = load_month('CRMLSListing202510.csv')
list23 = load_month('CRMLSListing202511.csv')
list24 = load_month('CRMLSListing202512.csv')
list25 = load_month('CRMLSListing202601.csv')
list26 = load_month('CRMLSListing202602.csv')
list27 = load_month('CRMLSListing202603.csv')
list28 = load_month('CRMLSListing202604.csv')
list29 = load_month('CRMLSListing202605.csv')
list30 = load_month('CRMLSListing202606.csv')
list31 = load_month('CRMLSListing202607.csv')


# Row count check before concat
list_rows_before = (
    len(list3) + len(list4) + len(list5) + len(list6)
    + len(list7) + len(list8) + len(list9) + len(list10) + len(list11) + len(list12)
    + len(list13) + len(list14) + len(list15) + len(list16) + len(list17) + len(list18)
    + len(list19) + len(list20) + len(list21) + len(list22) + len(list23) + len(list24)
    + len(list25) + len(list26) + len(list27) + len(list28) + len(list29) + len(list30) + len(list31)
)
print(f"Listings - rows before concatenation: {list_rows_before}")

listing = pd.concat([
    list3, list4, list5, list6, list7, list8, list9, list10,
    list11, list12, list13, list14, list15, list16, list17, list18, list19, list20,
    list21, list22, list23, list24, list25, list26, list27, list28, list29
], ignore_index=True)

print(f"Listings - rows after concatenation: {len(listing)}")



# Filter to residential

print(f"\nSold - rows before Residential filter: {len(sold)}")
sold = sold[sold.PropertyType == 'Residential']
print(f"Sold - rows after Residential filter: {len(sold)}")

print(f"\nListings - rows before Residential filter: {len(listing)}")
listing = listing[listing.PropertyType == 'Residential']
print(f"Listings - rows after Residential filter: {len(listing)}")



# Saving final CVs to IDX_Deliverables folder

output_folder = "IDX_Deliverables"
os.makedirs(output_folder, exist_ok=True) 

sold.to_csv(os.path.join(output_folder, 'sold.csv'), index=False)
listing.to_csv(os.path.join(output_folder, 'listings.csv'), index=False)

print(f"\nSaved {output_folder}/sold.csv with {len(sold)} rows.")
print(f"Saved {output_folder}/listings.csv with {len(listing)} rows.")
