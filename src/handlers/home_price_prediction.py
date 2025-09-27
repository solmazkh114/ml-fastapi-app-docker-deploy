from pydantic import BaseModel
from loguru import logger
import pandas as pd
import joblib

logger.info("Loading model...")
model = joblib.load("model/model.joblib")

class PredictRequest(BaseModel):
    size: float
    zone: str


def home_price_prediction(request: PredictRequest):
    logger.info("prediction request received")
    data = pd.DataFrame([request.dict()])
    prediction = model.predict(data)[0]
    logger.info(f"prediction: {prediction}")
    return {"predicted_price": round(float(prediction), 2)}