import pandas as pd
from sqlalchemy import create_engine

# Load Dataset
df = pd.read_csv("Telco-Customer-Churn.csv")

print("Dataset Loaded Successfully")
print(df.shape)

# Connect PostgreSQL
engine = create_engine(
    "postgresql://postgres:nikhilM%402005@localhost:5432/telco_churn"
)
# Upload Data to PostgreSQL
df.to_sql(
    name="customer_churn",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data Uploaded Successfully")