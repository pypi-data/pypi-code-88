from enum import Enum


class ModelType(Enum):
    TENSORFLOW = 0
    PYTORCH = 1
    SKLEARN = 2
    XGBOOST = 3
    ONNX = 4
    TRITON = 5
