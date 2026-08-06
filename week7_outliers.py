"""
Week 7 Deliverable - Outlier Detection and Data Quality
Saved as:
  - sold_flagged.csv  = full dataset with outlier flag columns
  - sold_filtered.csv = same dataset with outlier rows removed

"""

import pandas as pd

# Loaded the dataset from Week 6
sold = pd.read_csv('IDX_Deliverables/sold_with_metrics.csv')

print(f"Rows before outlier filtering: {len(sold)}")
print(f"Median ClosePrice before filtering: {sold['ClosePrice'].median()}")
print(f"Median LivingArea before filtering: {sold['LivingArea'].median()}")
print(f"Median DaysOnMarket before filtering: {sold['DaysOnMarket'].median()}")


# ClosePrice - IQR outlier flag

Q1 = sold['ClosePrice'].quantile(0.25)
Q3 = sold['ClosePrice'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
sold['ClosePrice_outlier_flag'] = (sold['ClosePrice'] < lower) | (sold['ClosePrice'] > upper)


# LivingArea - IQR outlier flag

Q1 = sold['LivingArea'].quantile(0.25)
Q3 = sold['LivingArea'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
sold['LivingArea_outlier_flag'] = (sold['LivingArea'] < lower) | (sold['LivingArea'] > upper)

# DaysOnMarket - IQR outlier flag

Q1 = sold['DaysOnMarket'].quantile(0.25)
Q3 = sold['DaysOnMarket'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
sold['DaysOnMarket_outlier_flag'] = (sold['DaysOnMarket'] < lower) | (sold['DaysOnMarket'] > upper)

# Count how many rows got flagged for each field
print(f"\nClosePrice outliers flagged: {sold['ClosePrice_outlier_flag'].sum()}")
print(f"LivingArea outliers flagged: {sold['LivingArea_outlier_flag'].sum()}")
print(f"DaysOnMarket outliers flagged: {sold['DaysOnMarket_outlier_flag'].sum()}")

# Save the FULL dataset with flag columns added
sold.to_csv('IDX_Deliverables/sold_flagged.csv', index=False)
print("\nSaved sold_flagged.csv (full dataset, outliers flagged not removed)")


# Remove rows flagged as an outlier on any field

sold_filtered = sold[
    (sold['ClosePrice_outlier_flag'] == False)
    & (sold['LivingArea_outlier_flag'] == False)
    & (sold['DaysOnMarket_outlier_flag'] == False)
]

print(f"\nRows after outlier filtering: {len(sold_filtered)}")
print(f"Median ClosePrice after filtering: {sold_filtered['ClosePrice'].median()}")
print(f"Median LivingArea after filtering: {sold_filtered['LivingArea'].median()}")
print(f"Median DaysOnMarket after filtering: {sold_filtered['DaysOnMarket'].median()}")

sold_filtered.to_csv('IDX_Deliverables/sold_filtered.csv', index=False)
print("\nSaved sold_filtered.csv (outlier rows removed)")
