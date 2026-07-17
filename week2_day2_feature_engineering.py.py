import pandas as pd


df = pd.read_csv("feature_engineered_churn.csv")

print("Original Shape:", df.shape)


df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 24, 48, 72],
    labels=[
        "New Customer",
        "Regular Customer",
        "Loyal Customer",
        "VIP Customer"
    ]
)

df["ContractRisk"] = 0

df.loc[df["Contract_One year"] == 1, "ContractRisk"] = 1
df.loc[df["Contract_Two year"] == 1, "ContractRisk"] = 2


df["CustomerLifetimeValue"] = (
    df["MonthlyCharges"] * df["tenure"]
)

print("\nNew Features Added Successfully")

print(
    df[[
        "TenureGroup",
        "ContractRisk",
        "CustomerLifetimeValue"
    ]].head()
)


df.to_csv(
    "feature_engineered_churn_v2.csv",
    index=False
)

print("\nDataset Saved Successfully")
print("New Shape:", df.shape)

