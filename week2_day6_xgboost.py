import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

from xgboost import XGBClassifier


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

xgb_model = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    random_state=42,
    eval_metric="logloss"
)


xgb_model.fit(X_train, y_train)

print("Model Training Completed")


y_pred = xgb_model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("XGBOOST RESULTS")
print("==============================")

print(f"\nAccuracy: {accuracy:.4f}")


print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


print("\nClassification Report:")
print(classification_report(y_test, y_pred))


feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": xgb_model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 10 Important Features")
print(feature_importance.head(10))


with open("week2_day6_results.txt", "w") as f:
    f.write("Week 2 Day 6 - XGBoost\n\n")
    f.write(f"Accuracy: {accuracy:.4f}\n\n")
    f.write("Confusion Matrix:\n")
    f.write(str(confusion_matrix(y_test, y_pred)))
    f.write("\n\nClassification Report:\n")
    f.write(classification_report(y_test, y_pred))

print("\nResults Saved Successfully")