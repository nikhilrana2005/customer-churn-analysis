import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


df = pd.read_csv("final_feature_engineered_churn.csv")

print("Dataset Shape:", df.shape)


X = df.drop("Churn", axis=1)
y = df["Churn"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)


scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Scaling Completed")


model = LogisticRegression(
    max_iter=2000,
    random_state=42
)


model.fit(X_train_scaled, y_train)

print("Model Training Completed")


y_pred = model.predict(X_test_scaled)


accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("LOGISTIC REGRESSION RESULTS")
print("==============================")

print(f"\nAccuracy: {accuracy:.4f}")


print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


print("\nClassification Report:")
print(classification_report(y_test, y_pred))

with open("week2_day4_results.txt", "w") as f:
    f.write("Week 2 Day 4 - Logistic Regression\n\n")
    f.write(f"Accuracy: {accuracy:.4f}\n\n")
    f.write("Confusion Matrix:\n")
    f.write(str(confusion_matrix(y_test, y_pred)))
    f.write("\n\nClassification Report:\n")
    f.write(classification_report(y_test, y_pred))

print("\nResults Saved Successfully")