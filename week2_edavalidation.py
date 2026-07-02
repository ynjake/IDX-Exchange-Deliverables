"""
Weeks 2-3 Deliverable - Dataset Structuring and Validation

"""

import pandas as pd
import os

DELIVERABLES_FOLDER = "IDX_Deliverables"
NUMERIC_FIELDS = ['ClosePrice', 'LivingArea', 'DaysOnMarket']


def validate_dataset(filename, label):
    path = os.path.join(DELIVERABLES_FOLDER, filename)
    df = pd.read_csv(path, low_memory=False)

    print("=" * 70)
    print(f"{label.upper()} DATASET")
    print("=" * 70)

    # 1. Unique property types and filtering logic
    print(f"\nUnique PropertyType values: {df['PropertyType'].unique()}")
    print("Filtering logic applied (in Week 1, before this CSV was saved):")
    print(f"    {label.lower()} = {label.lower()}[{label.lower()}.PropertyType == 'Residential']")

    # 2. Null-count summary table
    null_counts = df.isnull().sum()
    print(f"\nNull-count summary table ({label}):")
    print(null_counts.to_string())

    # 3. Missing value report
    missing_pct = (null_counts / len(df) * 100).round(2)
    missing_report = pd.DataFrame({
        'column': df.columns,
        'null_count': null_counts.values,
        'null_pct': missing_pct.values
    }).sort_values('null_pct', ascending=False)

    high_missing = missing_report[missing_report['null_pct'] > 90]
    print(f"\nColumns above 90% null ({len(high_missing)} total):")
    if len(high_missing) > 0:
        print(high_missing[['column', 'null_pct']].to_string(index=False))
    else:
        print("  None")

    # 4. Numeric distribution summary 
    print(f"\nNumeric distribution summary ({label}):")
    for field in NUMERIC_FIELDS:
        if field not in df.columns:
            print(f"  [{field}] not found in {label} dataset - skipping")
            continue

        series = pd.to_numeric(df[field], errors='coerce').dropna()
        if len(series) == 0:
            print(f"  [{field}] has no usable numeric data - skipping")
            continue

        print(f"\n  {field}:")
        print(f"    min:              {series.min():,.2f}")
        print(f"    max:              {series.max():,.2f}")
        print(f"    mean:             {series.mean():,.2f}")
        print(f"    median:           {series.median():,.2f}")
        print(f"    25th percentile:  {series.quantile(0.25):,.2f}")
        print(f"    75th percentile:  {series.quantile(0.75):,.2f}")
        print(f"    99th percentile:  {series.quantile(0.99):,.2f}")

    # 5. Save the filtered dataset as a new CSV
    output_path = os.path.join(DELIVERABLES_FOLDER, f"{label.lower()}_validated.csv")
    df.to_csv(output_path, index=False)
    print(f"\nSaved validated {label} dataset to {output_path} ({len(df)} rows)")
    print()


def main():
    validate_dataset('sold.csv', 'Sold')
    validate_dataset('listings.csv', 'Listings')


if __name__ == "__main__":
    main()