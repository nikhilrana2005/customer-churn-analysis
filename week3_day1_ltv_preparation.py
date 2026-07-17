import pandas as pd

df = pd.read_csv("final_feature_engineered_churn.csv")

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())



df["LTV"] = df["MonthlyCharges"] * df["tenure"]

print("\nLTV Created Successfully")

print("\nTop 5 Customers")

print(
    df[
        [
            "MonthlyCharges",
            "tenure",
            "LTV"
        ]
    ].head()
)



print("\nLTV Statistics")

print(df["LTV"].describe())



df.to_csv(
    "ltv_dataset.csv",
    index=False
)

print("\nDataset Saved Successfully")

print("\nFinal Shape:", df.shape)