from pydantic import BaseModel, Field
from typing import List


class PredictionRequest(BaseModel):
    features: List[float] = Field(..., min_length=4, max_length=4)


class PredictionResponse(BaseModel):
    prediction: int