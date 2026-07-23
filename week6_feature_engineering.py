"""
Week 6 Deliverable - Feature Engineering and Market Metrics

"""

DELIVERABLES_FOLDER = "IDX_Deliverables"

import pandas as pd

# Load the cleaned sold dataset from Weeks 4-5
sold = pd.read_csv('IDX_Deliverables/sold_cleaned.csv')

print(f"Rows before engineering: {len(sold)}")

# Convert date columns to real dates
sold['CloseDate'] = pd.to_datetime(sold['CloseDate'])
sold['PurchaseContractDate'] = pd.to_datetime(sold['PurchaseContractDate'])
sold['ListingContractDate'] = pd.to_datetime(sold['ListingContractDate'])

# Price Ratio and Close to Original List Ratio (same formula, two names per the handbook)
sold['PriceRatio'] = sold['ClosePrice'] / sold['OriginalListPrice']
sold['CloseToOriginalListRatio'] = sold['ClosePrice'] / sold['OriginalListPrice']

# Price Per Sq Ft
sold['PricePerSqFt'] = sold['ClosePrice'] / sold['LivingArea']

# Year / Month / YrMo, derived from CloseDate
sold['Year'] = sold['CloseDate'].dt.year
sold['Month'] = sold['CloseDate'].dt.month
sold['YrMo'] = sold['CloseDate'].dt.to_period('M')

# Listing to Contract Days and Contract to Close Days
sold['ListingToContractDays'] = (sold['PurchaseContractDate'] - sold['ListingContractDate']).dt.days
sold['ContractToCloseDays'] = (sold['CloseDate'] - sold['PurchaseContractDate']).dt.days

print(f"Rows after engineering: {len(sold)}")

# Sample output showing the new columns
print("\nSample of engineered metrics:")
print(sold[[
    'PriceRatio', 'CloseToOriginalListRatio', 'PricePerSqFt',
    'Year', 'Month', 'YrMo', 'ListingToContractDays', 'ContractToCloseDays'
]].head(10))

# Segmented summary by PropertyType
print("\nMedian ClosePrice, PricePerSqFt, DaysOnMarket by PropertyType:")
summary_by_type = sold.groupby('PropertyType')[['ClosePrice', 'PricePerSqFt', 'DaysOnMarket']].median()
print(summary_by_type)

# Segmented summary by CountyOrParish
print("\nMedian ClosePrice, PricePerSqFt, DaysOnMarket by CountyOrParish:")
summary_by_county = sold.groupby('CountyOrParish')[['ClosePrice', 'PricePerSqFt', 'DaysOnMarket']].median()
print(summary_by_county)

# Save the dataset with the new metric columns
sold.to_csv('IDX_Deliverables/sold_with_metrics.csv', index=False)
print("\nSaved sold_with_metrics.csv")