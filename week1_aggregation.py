import pandas as pd

listings = pd.read_csv('CRMLSListing202601_202605.csv', encoding='latin-1')

print("=== LISTINGS ===")
print(f"Rows BEFORE Residential filter: {len(listings)}")

listings_residential = listings[listings['PropertyType'] == 'Residential']

print(f"Rows AFTER Residential filter:  {len(listings_residential)}")
print(f"Rows removed: {len(listings) - len(listings_residential)}")

listings_residential.to_csv('CRMLSListing_Residential.csv', index=False)
print("Saved: CRMLSListing_Residential.csv")
print()

sold = pd.read_csv('CRMLSSold202601_202605.csv', encoding='latin-1')

print("=== SOLD ===")
print(f"Rows BEFORE Residential filter: {len(sold)}")

sold_residential = sold[sold['PropertyType'] == 'Residential']

print(f"Rows AFTER Residential filter:  {len(sold_residential)}")
print(f"Rows removed: {len(sold) - len(sold_residential)}")

sold_residential.to_csv('CRMLSSold_Residential.csv', index=False)
print("Saved: CRMLSSold_Residential.csv")
print()

print("Complete")