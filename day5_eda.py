import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Telco-Customer-Churn.csv")

plt.figure(figsize=(10,5))

sns.histplot(
    data=df,
    x="tenure",
    bins=30,
    kde=True
)

plt.title("Customer Tenure Distribution")
plt.show()


plt.figure(figsize=(10,5))

sns.histplot(
    data=df,
    x="MonthlyCharges",
    bins=30,
    kde=True
)

plt.title("Monthly Charges Distribution")
plt.show()

df["Churn"] = df["Churn"].map({
    "No":0,
    "Yes":1
})

corr_df = df[[
    "SeniorCitizen",
    "tenure",
    "MonthlyCharges",
    "Churn"
]]

print(corr_df.corr())

plt.figure(figsize=(8,6))

sns.heatmap(
    corr_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[0,12,24,48,72],
    labels=[
        "0-12",
        "13-24",
        "25-48",
        "49-72"
    ]
)

print(
    pd.crosstab(
        df["TenureGroup"],
        df["Churn"]
    )
)

sns.countplot(
    x="TenureGroup",
    hue="Churn",
    data=df
)

plt.title("Tenure Group vs Churn")
plt.show()

df["ChargeGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0,35,70,120],
    labels=[
        "Low",
        "Medium",
        "High"
    ]
)

print(
    pd.crosstab(
        df["ChargeGroup"],
        df["Churn"]
    )
)


sns.countplot(
    x="ChargeGroup",
    hue="Churn",
    data=df
)

plt.title("Monthly Charge Category vs Churn")
plt.show()