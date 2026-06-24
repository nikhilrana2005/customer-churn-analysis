import pandas as pd


df = pd.read_csv("cleaned_telco_churn.csv")

print("Original Shape:", df.shape)


df["RevenuePerMonth"] = (
    df["TotalCharges"] /
    (df["tenure"] + 1)
)


df["ChargeRatio"] = (
    df["MonthlyCharges"] /
    (df["RevenuePerMonth"] + 1)
)


df["HighValueCustomer"] = (
    df["MonthlyCharges"] >
    df["MonthlyCharges"].median()
).astype(int)

print("\nNew Features Created Successfully")

print(df[[
    "RevenuePerMonth",
    "ChargeRatio",
    "HighValueCustomer"
]].head())


df.to_csv(
    "feature_engineered_churn.csv",
    index=False
)

print("\nDataset Saved")
print("New Shape:", df.shape)