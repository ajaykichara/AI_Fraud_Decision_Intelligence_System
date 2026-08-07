import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("credit_card_transactions.csv")

# ===========================
# Rename Columns
# ===========================
df.rename(columns={
    "trans_date_trans_time": "transaction_time",
    "amt": "transaction_amount",
    "category": "merchant_category",
    "zip": "customer_zip",
    "lat": "customer_latitude",
    "long": "customer_longitude",
    "city_pop": "city_population",
    "dob": "customer_dob",
    "merch_lat": "merchant_latitude",
    "merch_long": "merchant_longitude",
    "merch_zipcode": "merchant_zip"
}, inplace=True)

# ===========================
# Drop Unnecessary Columns
# ===========================
df.drop(columns=[
    "Unnamed: 0",
    "cc_num",
    "first",
    "last",
    "street",
    "trans_num",
    "unix_time"
], inplace=True)

# ===========================
# Handle Missing Values
# ===========================
df["merchant_zip"] = df["merchant_zip"].fillna(-1)

# ============================================
# Convert Date Columns
# ============================================

df["transaction_time"] = pd.to_datetime(df["transaction_time"])
df["customer_dob"] = pd.to_datetime(df["customer_dob"])

# ============================================
# Customer Age
# ============================================

current_year = pd.Timestamp.now().year
df["customer_age"] = current_year - df["customer_dob"].dt.year

# ============================================
# Transaction Time Features
# ============================================

df["transaction_hour"] = df["transaction_time"].dt.hour
df["transaction_day"] = df["transaction_time"].dt.day
df["transaction_month"] = df["transaction_time"].dt.month
df["transaction_weekday"] = df["transaction_time"].dt.dayofweek

# ============================================
# Weekend Transaction
# ============================================

df["is_weekend"] = np.where(
    df["transaction_weekday"] >= 5,
    1,
    0
)

# ============================================
# Night Transaction
# ============================================

df["is_night_transaction"] = np.where(
    (df["transaction_hour"] >= 22) |
    (df["transaction_hour"] <= 5),
    1,
    0
)

# ============================================
# High Amount Transaction
# ============================================

df["high_amount_transaction"] = np.where(
    df["transaction_amount"] >= 1000,
    1,
    0
)




# ============================================
# Drop Original Date Columns
# ============================================
df.drop(columns=[
    "customer_latitude",
    "customer_longitude",
    "merchant_latitude",
    "merchant_longitude",
    "transaction_time",
    "customer_dob"
], inplace=True)

print("=" * 80)
print("FINAL DATASET")
print("=" * 80)

print(df.info())

print("\nShape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nColumns:")
print(df.columns.tolist())

print("\nTarget Distribution:")
print(df["is_fraud"].value_counts())

print("\nDataset saved as final_credit_fraud_dataset.csv")# ===========================


# Save Clean Dataset
# ===========================
# df.to_csv("final_credit_fraud_dataset.csv", index=False)
