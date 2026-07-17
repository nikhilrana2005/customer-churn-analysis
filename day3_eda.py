import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nChurn Distribution")
print(df["Churn"].value_counts())

print("\nChurn Percentage")
print(df["Churn"].value_counts(normalize=True)*100)


import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x="Churn", data=df)

plt.title("Customer Churn Distribution")
plt.show()

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"]
)

print(contract_churn)


sns.countplot(
    x="Contract",
    hue="Churn",
    data=df
)

plt.title("Contract Type vs Churn")
plt.xticks(rotation=15)
plt.show()

sns.boxplot(
    x="Churn",
    y="tenure",
    data=df
)

plt.title("Tenure vs Churn")
plt.show()


sns.boxplot(
    x="Churn",
    y="MonthlyCharges",
    data=df
)

plt.title("Monthly Charges vs Churn")
plt.show()