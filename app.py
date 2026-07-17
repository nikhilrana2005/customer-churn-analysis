from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    title="Customer Lifetime Value Prediction API",
    version="1.0"
)

# Load model and feature columns
model = joblib.load("random_forest_ltv.pkl")
feature_columns = joblib.load("feature_columns.pkl")


class CustomerData(BaseModel):
    SeniorCitizen: int
    Partner: int
    Dependents: int
    PhoneService: int
    PaperlessBilling: int
    TotalCharges: float
    


@app.get("/")
def home():
    return {
        "message": "Customer Lifetime Value Prediction API Running"
    }


@app.post("/predict")
def predict(data: CustomerData):

    input_df = pd.DataFrame([data.model_dump()])

    input_df = pd.get_dummies(input_df)

    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[feature_columns]

    prediction = model.predict(input_df)

    return {
        "Predicted_LTV": round(float(prediction[0]), 2)
    }


@app.post("/batch_predict")
async def batch_predict(file: UploadFile = File(...)):

    # Check file type
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Please upload only CSV files."
        )

    try:
        # Read uploaded CSV
        df = pd.read_csv(file.file)

        # One-hot encoding
        df = pd.get_dummies(df)

        # Add missing columns
        for col in feature_columns:
            if col not in df.columns:
                df[col] = 0

        # Arrange columns
        df = df[feature_columns]

        # Predict
        predictions = model.predict(df)

        # Save predictions
        result = pd.DataFrame({
            "Predicted_LTV": predictions
        })

        output_file = "batch_predictions.csv"
        result.to_csv(output_file, index=False)

        # Return downloadable file
        return FileResponse(
            output_file,
            media_type="text/csv",
            filename="batch_predictions.csv"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )