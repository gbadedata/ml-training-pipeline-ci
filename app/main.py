from contextlib import asynccontextmanager

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.model_loader import load_model
from app.predictor import predict
from app.schemas import PredictionRequest, PredictionResponse


MODEL_PATH = "model/artifact/model.joblib"


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = load_model(MODEL_PATH)
    yield


app = FastAPI(title="ML Training Pipeline API", version="1.0.0", lifespan=lifespan)

Instrumentator().instrument(app).expose(app)


@app.get("/health/live")
def live():
    return {"status": "alive"}


@app.get("/health/ready")
def ready():
    if getattr(app.state, "model", None) is None:
        return {"status": "not_ready"}
    return {"status": "ready"}


@app.post("/predict", response_model=PredictionResponse)
def make_prediction(request: PredictionRequest):
    result = predict(request.features, app.state.model)
    return PredictionResponse(prediction=result)