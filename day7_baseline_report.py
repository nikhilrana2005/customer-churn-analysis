import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

print("\nColumns:")
print(df.columns.tolist())

churn_count = df["Churn"].value_counts()

print(churn_count)

churn_rate = (
    df["Churn"]
    .value_counts(normalize=True)
    * 100
)

print("\nChurn Percentage")
print(churn_rate)

contract_analysis = pd.crosstab(
    df["Contract"],
    df["Churn"]
)

print("\nContract Analysis")
print(contract_analysis)

print(
    df.groupby("Churn")["tenure"]
    .mean()
)

print(
    df.groupby("Churn")["MonthlyCharges"]
    .mean()
)

payment_analysis = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"]
)

print(payment_analysis)

internet_analysis = pd.crosstab(
    df["InternetService"],
    df["Churn"]
)

print(internet_analysis)

report = {
    "Total_Customers":[df.shape[0]],
    "Total_Features":[df.shape[1]]
}

summary_df = pd.DataFrame(report)

summary_df.to_csv(
    "baseline_summary.csv",
    index=False
)