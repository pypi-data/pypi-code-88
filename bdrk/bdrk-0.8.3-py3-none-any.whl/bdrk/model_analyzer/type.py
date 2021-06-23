from enum import Enum


class ModelTask(Enum):
    CLASSIFICATION = "CLASSIFICATION"
    REGRESSION = "REGRESSION"


class ModelTypes(Enum):
    TREE = "TREE"
    DEEP = "DEEP"
    LINEAR = "LINEAR"


class DeepLearningFramework(Enum):
    TENSORFLOW = "TENSORFLOW"
    PYTORCH = "PYTORCH"
