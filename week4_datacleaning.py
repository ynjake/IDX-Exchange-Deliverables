"""
Weeks 4-5 Deliverable - Data Cleaning and Preparation

"""

import pandas as pd
import os

DELIVERABLES_FOLDER = "IDX_Deliverables"

# Date fields present in MLS data 

DATE_FIELDS = [
    'CloseDate', 'PurchaseContractDate', 'ListingContractDate',
    'ContractStatusChangeDate'
]


def convert_dates(df, label):
    """
    Converts any of the known date fields present in df to real datetime values.
    """
    print(f"\n--- {label}: Date Type Conversion ---")
    for field in DATE_FIELDS:
        if field in df.columns:
            before_dtype = df[field].dtype
            df[field] = pd.to_datetime(df[field], errors='coerce')
            print(f"  {field}: {before_dtype} -> {df[field].dtype}")
    return df


def flag_invalid_numeric_values(df, label):
    """
    Flags rows with invalid numeric values:
    ClosePrice <= 0, LivingArea <= 0, DaysOnMarket < 0, negative Bedrooms/Bathrooms.
    """
    print(f"\n--- {label}: Invalid Numeric Value Flags ---")

    if 'ClosePrice' in df.columns:
        df['invalid_close_price_flag'] = pd.to_numeric(df['ClosePrice'], errors='coerce') <= 0
        print(f"  invalid_close_price_flag (ClosePrice <= 0): {df['invalid_close_price_flag'].sum()}")

    if 'LivingArea' in df.columns:
        df['invalid_living_area_flag'] = pd.to_numeric(df['LivingArea'], errors='coerce') <= 0
        print(f"  invalid_living_area_flag (LivingArea <= 0): {df['invalid_living_area_flag'].sum()}")

    if 'DaysOnMarket' in df.columns:
        df['invalid_dom_flag'] = pd.to_numeric(df['DaysOnMarket'], errors='coerce') < 0
        print(f"  invalid_dom_flag (DaysOnMarket < 0): {df['invalid_dom_flag'].sum()}")

    if 'BedroomsTotal' in df.columns:
        df['invalid_bedrooms_flag'] = pd.to_numeric(df['BedroomsTotal'], errors='coerce') < 0
        print(f"  invalid_bedrooms_flag (Bedrooms < 0): {df['invalid_bedrooms_flag'].sum()}")

    if 'BathroomsTotalInteger' in df.columns:
        df['invalid_bathrooms_flag'] = pd.to_numeric(df['BathroomsTotalInteger'], errors='coerce') < 0
        print(f"  invalid_bathrooms_flag (Bathrooms < 0): {df['invalid_bathrooms_flag'].sum()}")

    return df


def flag_date_consistency(df, label):
    """
    Flags records where the transaction timeline doesn't make sense:
    listing should come before purchase contract, which should come before close.
    """
    print(f"\n--- {label}: Date Consistency Flags ---")

    has_listing = 'ListingContractDate' in df.columns
    has_purchase = 'PurchaseContractDate' in df.columns
    has_close = 'CloseDate' in df.columns

    if has_listing and has_close:
        df['listing_after_close_flag'] = df['ListingContractDate'] > df['CloseDate']
        print(f"  listing_after_close_flag: {df['listing_after_close_flag'].sum()}")
    else:
        df['listing_after_close_flag'] = False
        print(f"  listing_after_close_flag: skipped (missing ListingContractDate or CloseDate)")

    if has_purchase and has_close:
        df['purchase_after_close_flag'] = df['PurchaseContractDate'] > df['CloseDate']
        print(f"  purchase_after_close_flag: {df['purchase_after_close_flag'].sum()}")
    else:
        df['purchase_after_close_flag'] = False
        print(f"  purchase_after_close_flag: skipped (missing PurchaseContractDate or CloseDate)")

    if has_listing and has_purchase:
        df['negative_timeline_flag'] = df['ListingContractDate'] > df['PurchaseContractDate']
        print(f"  negative_timeline_flag: {df['negative_timeline_flag'].sum()}")
    else:
        df['negative_timeline_flag'] = False
        print(f"  negative_timeline_flag: skipped (missing ListingContractDate or PurchaseContractDate)")

    return df


def flag_geographic_issues(df, label):
    """
    Flags records with missing or implausible Latitude/Longitude values.
    California coordinates should always have a negative longitude.
    """
    print(f"\n--- {label}: Geographic Data Quality ---")

    has_lat = 'Latitude' in df.columns
    has_lon = 'Longitude' in df.columns

    if has_lat and has_lon:
        lat = pd.to_numeric(df['Latitude'], errors='coerce')
        lon = pd.to_numeric(df['Longitude'], errors='coerce')

        df['missing_coordinates_flag'] = lat.isnull() | lon.isnull()
        df['zero_coordinates_flag'] = (lat == 0) | (lon == 0)
        df['positive_longitude_flag'] = lon > 0  # CA longitude should be negative

        print(f"  missing_coordinates_flag: {df['missing_coordinates_flag'].sum()}")
        print(f"  zero_coordinates_flag (sentinel nulls): {df['zero_coordinates_flag'].sum()}")
        print(f"  positive_longitude_flag (should be negative for CA): {df['positive_longitude_flag'].sum()}")
    else:
        print("  Latitude/Longitude columns not found - skipping geographic checks")

    return df


def clean_dataset(filename, label):
    path = os.path.join(DELIVERABLES_FOLDER, filename)
    df = pd.read_csv(path, low_memory=False)

    print("=" * 70)
    print(f"{label.upper()} DATASET")
    print("=" * 70)

    rows_before = len(df)
    print(f"\nRows before cleaning: {rows_before}")

    df = convert_dates(df, label)
    df = flag_invalid_numeric_values(df, label)
    df = flag_date_consistency(df, label)
    df = flag_geographic_issues(df, label)

    rows_after = len(df)
    print(f"\nRows after cleaning (no rows removed, only flagged): {rows_after}")

    output_path = os.path.join(DELIVERABLES_FOLDER, f"{label.lower()}_cleaned.csv")
    df.to_csv(output_path, index=False)
    print(f"\nSaved cleaned {label} dataset to {output_path} ({len(df)} rows)")
    print()

    return df


def main():
    clean_dataset('sold_with_rates.csv', 'Sold')
    clean_dataset('listings_with_rates.csv', 'Listings')

if __name__ == "__main__":
    main()