from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from .routers.home_price_prediction import home_price_prediction_router



logger.info("app starting...")
app = FastAPI(title="House Price Prediction API")

logger.info("Adding CORS middleware...")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Defining routes...")
app.include_router(home_price_prediction_router, prefix="")
