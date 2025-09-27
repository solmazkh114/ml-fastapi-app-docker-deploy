from ..handlers.home_price_prediction import PredictRequest, home_price_prediction
from fastapi import APIRouter

home_price_prediction_router = APIRouter()

@home_price_prediction_router.post("/predict")
def predict(request: PredictRequest): return home_price_prediction(request)