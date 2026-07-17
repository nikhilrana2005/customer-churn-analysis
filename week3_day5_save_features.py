import pandas as pd
import joblib


df = pd.read_csv("ltv_dataset.csv")

X = df.drop(columns=["LTV"], errors="ignore")


if "customerID" in X.columns:
    X = X.drop(columns=["customerID"])

bool_cols = X.select_dtypes(include="bool").columns
for col in bool_cols:
    X[col] = X[col].astype(int)


X = pd.get_dummies(X, drop_first=True)


joblib.dump(list(X.columns), "feature_columns.pkl")

print("Feature Columns Saved Successfully")
print("Total Features:", len(X.columns))