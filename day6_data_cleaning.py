import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

print(df.shape)

print(df.isnull().sum())

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

print(df.isnull().sum())

df.dropna(inplace=True)

print(df.shape)

df.drop("customerID", axis=1, inplace=True)

df["Churn"] = df["Churn"].map({
    "No":0,
    "Yes":1
})

print(df["Churn"].value_counts())

binary_cols = [
    "gender",
    "Partner",
    "Dependents",
    "PhoneService",
    "PaperlessBilling"
]

for col in binary_cols:
    print(col, df[col].unique())
    
    df["gender"] = df["gender"].map({
    "Female":0,
    "Male":1
})

df["Partner"] = df["Partner"].map({
    "No":0,
    "Yes":1
})

df["Dependents"] = df["Dependents"].map({
    "No":0,
    "Yes":1
})

df["PhoneService"] = df["PhoneService"].map({
    "No":0,
    "Yes":1
})

df["PaperlessBilling"] = df["PaperlessBilling"].map({
    "No":0,
    "Yes":1
})

df = pd.get_dummies(
    df,
    drop_first=True
)

print(df.head())

print(df.shape)

print(df.info())

df.to_csv(
    "cleaned_telco_churn.csv",
    index=False
)

print("Clean Dataset Saved")