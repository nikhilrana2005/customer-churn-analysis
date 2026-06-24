import pandas as pd

comparison = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],
    "Accuracy": [
        0.8038,
        0.7854,
        0.0000
    ]
})

print(comparison)

comparison.to_csv(
    "model_comparison.csv",
    index=False
)

print("\nComparison Saved Successfully")