import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Telco-Customer-Churn.csv")


payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"]
)

print(payment_churn)

plt.figure(figsize=(10,5))

sns.countplot(
    x="PaymentMethod",
    hue="Churn",
    data=df
)

plt.xticks(rotation=30)
plt.title("Payment Method vs Churn")
plt.show()

internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"]
)

print(internet_churn)

sns.countplot(
    x="InternetService",
    hue="Churn",
    data=df
)

plt.title("Internet Service vs Churn")
plt.show()

tech_churn = pd.crosstab(
    df["TechSupport"],
    df["Churn"]
)

print(tech_churn)

sns.countplot(
    x="TechSupport",
    hue="Churn",
    data=df
)

plt.title("Tech Support vs Churn")
plt.show()


security_churn = pd.crosstab(
    df["OnlineSecurity"],
    df["Churn"]
)

print(security_churn)


sns.countplot(
    x="OnlineSecurity",
    hue="Churn",
    data=df
)

plt.title("Online Security vs Churn")
plt.show()