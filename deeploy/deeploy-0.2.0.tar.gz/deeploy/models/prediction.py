from typing import List, Optional, Dict, Any

from pydantic import BaseModel


class Prediction(BaseModel):
    pass


class V1Prediction(Prediction):
    predictions: List[Any]


class V2Prediction(Prediction):
    id: str
    model_name: str
    model_version: Optional[str]
    parameters: Optional[Dict]
    outputs: List[Dict]
