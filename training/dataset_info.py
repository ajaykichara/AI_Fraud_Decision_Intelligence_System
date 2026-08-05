#   the mount in it  is  dollar not  rupee 
import  pandas as  pd  

df =  pd.read_csv("data/final_credit_fraud_dataset.csv")
# ==========================================================
# DATASET ANALYSIS FOR DECISION ENGINE
# ==========================================================
print(df.info())
print(df["is_fraud"].value_counts())




print("=" * 60)
print("1. Transaction Amount Statistics")
print("=" * 60)
print(df["transaction_amount"].describe())

print("\n" + "=" * 60)
print("2. Transaction Amount Percentiles")
print("=" * 60)
print(df["transaction_amount"].quantile(
    [0.25, 0.50, 0.75, 0.90, 0.95, 0.99]
))

print("\n" + "=" * 60)
print("3. Night Transaction Distribution")
print("=" * 60)
print(df["is_night_transaction"].value_counts())

print("\n" + "=" * 60)
print("4. High Amount Transaction Distribution")
print("=" * 60)
print(df["high_amount_transaction"].value_counts())

print("\n" + "=" * 60)
print("5. Fraud Distribution")
print("=" * 60)
print(df["is_fraud"].value_counts())

print("\n" + "=" * 60)
print("6. Maximum Transaction Amount")
print("=" * 60)
print(df["transaction_amount"].max())

print("\n" + "=" * 60)
print("7. Minimum Transaction Amount")
print("=" * 60)
print(df["transaction_amount"].min())

print("\n" + "=" * 60)
print("8. Average Transaction Amount")
print("=" * 60)
print(df["transaction_amount"].mean())




print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())

print(df["transaction_amount"].describe())
print(df["transaction_amount"].quantile())

print(df["is_fraud"].value_counts())
print(df["is_night_transaction"].value_counts())
print(df["high_amount_transaction"].value_counts())


print("=" * 60)
print("9. Skewness")
print("=" * 60)

print(df["transaction_amount"].skew())

print("=" * 60)
print("9. Skewness")
print("=" * 60)

print(df["transaction_amount"].skew())




Q1 = df["transaction_amount"].quantile(0.25)
Q3 = df["transaction_amount"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["transaction_amount"] < lower) |
    (df["transaction_amount"] > upper)
]

print("=" * 60)
print("10. Outlier Detection")
print("=" * 60)

print("Outliers:", len(outliers))
print("Percentage:", len(outliers)/len(df)*100)