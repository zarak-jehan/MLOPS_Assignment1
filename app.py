from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("diabetes_model.pkl")
training_columns = joblib.load("training_columns.pkl")

app = FastAPI()


class PatientData(BaseModel):
    age: float
    urea: float
    cr: float
    hba1c: float
    chol: float
    tg: float
    hdl: float
    ldl: float
    vldl: float
    bmi: float
    gender: Literal["M", "F"]



@app.get("/")
def home():
    return {"status": "API is running"}


@app.post("/predict")
def predict(data: PatientData):

    # convert input to dataframe
    input_df = pd.DataFrame([data.dict()])

    # one-hot encode gender
    input_df = pd.get_dummies(input_df, columns=["gender"], drop_first=True)

    # align columns with training data
    input_df = input_df.reindex(columns=training_columns, fill_value=0)

    # prediction
    prediction = model.predict(input_df)[0]

    return {
    "prediction": prediction
}

