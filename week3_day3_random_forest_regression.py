import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)



df = pd.read_csv("ltv_dataset.csv")

print("=" * 50)
print("LTV DATASET")
print("=" * 50)

print("Dataset Shape:", df.shape)



y = df["LTV"]



X = df.drop(columns=["LTV"], errors="ignore")

if "customerID" in X.columns:
    X = X.drop(columns=["customerID"])


bool_cols = X.select_dtypes(include="bool").columns

for col in bool_cols:
    X[col] = X[col].astype(int)

# Encode Object Columns
X = pd.get_dummies(X, drop_first=True)

print("Feature Shape:", X.shape)



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))



model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel Training Completed")



y_pred = model.predict(X_test)



mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

print("\n==============================")
print("RANDOM FOREST REGRESSION")
print("==============================")

print(f"\nMAE : {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²  : {r2:.4f}")



results = pd.DataFrame({
    "Actual LTV": y_test.values,
    "Predicted LTV": y_pred
})

print("\nSample Predictions")
print(results.head(10))



results.to_csv(
    "week3_day3_predictions.csv",
    index=False
)




joblib.dump(
    model,
    "random_forest_ltv.pkl"
)



with open("week3_day3_results.txt", "w") as f:
    f.write("WEEK 3 DAY 3 - RANDOM FOREST REGRESSION\n\n")
    f.write(f"MAE : {mae:.2f}\n")
    f.write(f"RMSE: {rmse:.2f}\n")
    f.write(f"R2  : {r2:.4f}\n")

print("\nResults Saved Successfully")
print("Model Saved Successfully")
print("Prediction File Saved Successfully")