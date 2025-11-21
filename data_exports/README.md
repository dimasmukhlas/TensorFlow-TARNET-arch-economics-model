# Data Export Information

## Files Exported

1. **train_data.csv** - Training set (2,100 samples)
2. **val_data.csv** - Validation set (300 samples)
3. **test_data.csv** - Test set (600 samples)
4. **data_splits_summary.csv** - Summary statistics for each split
5. **feature_names.csv** - Feature column names and indices

## Column Structure

Each CSV file contains:
- **Feature columns**: gdp_growth, credit_gap, inflation, interest_rate, exchange_rate, household_debt_income, unemployment, lag_housing_price
- **treatment**: Binary treatment indicator (0 = control, 1 = treated)
- **outcome**: Observed outcome variable

## How to Load with Real Data

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load your real data
train_df = pd.read_csv('train_data.csv')
val_df = pd.read_csv('val_data.csv')
test_df = pd.read_csv('test_data.csv')

# Extract features, treatment, and outcome
feature_cols = ['gdp_growth', 'credit_gap', 'inflation', 'interest_rate', 'exchange_rate', 'household_debt_income', 'unemployment', 'lag_housing_price']

X_train = train_df[feature_cols].values
T_train = train_df['treatment'].values
Y_train = train_df['outcome'].values.reshape(-1, 1)

X_val = val_df[feature_cols].values
T_val = val_df['treatment'].values
Y_val = val_df['outcome'].values.reshape(-1, 1)

X_test = test_df[feature_cols].values
T_test = test_df['treatment'].values
Y_test = test_df['outcome'].values.reshape(-1, 1)

# Note: These data are already normalized (StandardScaler was applied)
# If loading new raw data, you'll need to:
# 1. Normalize using StandardScaler
# 2. Ensure same feature order as feature_names.csv
```

## Important Notes

- All features are **normalized** (StandardScaler applied)
- Treatment is binary: 0 = control, 1 = treated
- Outcome is continuous (housing price change %)
- Data splits maintain stratification by treatment

## Replicating with Real Data

To use this structure with your real data:

1. Prepare your data with the same feature columns
2. Ensure you have a binary treatment column (0/1)
3. Ensure you have an outcome column
4. Normalize features using StandardScaler
5. Split into train/val/test maintaining treatment stratification
6. Save in the same CSV format

Generated: 2025-11-18 15:08:14
