import pandas as pd


df = pd.read_csv("feature_engineered_churn_v2.csv")

print("Original Shape:", df.shape)


df["ChargesPerTenure"] = (
    df["TotalCharges"] /
    (df["tenure"] + 1)
)


service_columns = [
    "OnlineSecurity_Yes",
    "OnlineBackup_Yes",
    "DeviceProtection_Yes",
    "TechSupport_Yes",
    "StreamingTV_Yes",
    "StreamingMovies_Yes"
]

df["ServiceUsageScore"] = df[service_columns].sum(axis=1)


df["RiskCategory"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0, 35, 70, 120],
    labels=[
        "Low Risk",
        "Medium Risk",
        "High Risk"
    ]
)

print("\nNew Features Added Successfully")

print(df[[
    "ChargesPerTenure",
    "ServiceUsageScore",
    "RiskCategory"
]].head())


df = pd.get_dummies(
    df,
    columns=["TenureGroup", "RiskCategory"],
    drop_first=True
)

bool_cols = df.select_dtypes(include="bool").columns

for col in bool_cols:
    df[col] = df[col].astype(int)


df.to_csv(
    "final_feature_engineered_churn.csv",
    index=False
)

print("\nFinal Dataset Saved")
print("Final Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum().sum())

