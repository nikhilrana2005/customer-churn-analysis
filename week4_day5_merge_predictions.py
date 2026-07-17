import pandas as pd

# Load original predictions
pred = pd.read_csv("batch_predictions.csv")

# Load LTV dataset
ltv = pd.read_csv("ltv_dataset.csv")

# Add prediction column
ltv["Predicted_LTV"] = pred["Predicted_LTV"]

# Save new file
ltv.to_csv("ltv_dataset_with_predictions.csv", index=False)

print("Done!")
print(ltv.head())