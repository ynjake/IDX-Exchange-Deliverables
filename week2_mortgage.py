"""
Weeks 2-3 Deliverable (Part 2) - Mortgage Rate Enrichment

"""

import pandas as pd
import os

DELIVERABLES_FOLDER = "IDX_Deliverables"


def fetch_mortgage_rates():
    """Fetches the weekly 30-year fixed mortgage rate from FRED and
    changes it to a monthly average."""
    print("Fetching mortgage rate data from FRED...")
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
    mortgage = pd.read_csv(url, parse_dates=['observation_date'])
    mortgage.columns = ['date', 'rate_30yr_fixed']

    mortgage['year_month'] = mortgage['date'].dt.to_period('M')

    mortgage_monthly = (
        mortgage.groupby('year_month')['rate_30yr_fixed']
        .mean()
        .reset_index()
    )

    print(f"Retrieved and resampled {len(mortgage_monthly)} months of mortgage rate data.")
    return mortgage_monthly


def enrich_with_rates(df, date_column, mortgage_monthly, label):
    """
    Creates a year_month key, merges the mortgage
    rate onto it, and makes sure that no rows are missing a rate afterward.
    """
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    df['year_month'] = df[date_column].dt.to_period('M')

    enriched = df.merge(mortgage_monthly, on='year_month', how='left')

    missing_rate_count = enriched['rate_30yr_fixed'].isnull().sum()
    print(f"\n{label} - rows with missing rate_30yr_fixed after merge: {missing_rate_count}")

    if missing_rate_count > 0:
        # Show which year_months didn't get a match, so you can see why
        missing_months = enriched.loc[enriched['rate_30yr_fixed'].isnull(), 'year_month'].unique()
        print(f"{label} - year_months with no matching FRED rate: {list(missing_months)}")

    print(f"{label} - preview of enriched data:")
    preview_cols = [date_column, 'year_month', 'rate_30yr_fixed']
    print(enriched[preview_cols].head().to_string(index=False))

    return enriched


def main():
    # Fetch and resample mortgage rates 
    mortgage_monthly = fetch_mortgage_rates()

    # Load sold and listings datasets from the Weeks 2-3 validation step
    sold = pd.read_csv(os.path.join(DELIVERABLES_FOLDER, 'sold_validated.csv'), low_memory=False)
    listings = pd.read_csv(os.path.join(DELIVERABLES_FOLDER, 'listings_validated.csv'), low_memory=False)

    # Enrich each dataset with the matching monthly rate
   
    sold_with_rates = enrich_with_rates(sold, 'CloseDate', mortgage_monthly, 'Sold')
    listings_with_rates = enrich_with_rates(listings, 'ListingContractDate', mortgage_monthly, 'Listings')

    # Save enriched datasets
    sold_out_path = os.path.join(DELIVERABLES_FOLDER, 'sold_with_rates.csv')
    listings_out_path = os.path.join(DELIVERABLES_FOLDER, 'listings_with_rates.csv')

    sold_with_rates.to_csv(sold_out_path, index=False)
    listings_with_rates.to_csv(listings_out_path, index=False)

    print(f"\nSaved {sold_out_path} with {len(sold_with_rates)} rows.")
    print(f"Saved {listings_out_path} with {len(listings_with_rates)} rows.")


if __name__ == "__main__":
    main()