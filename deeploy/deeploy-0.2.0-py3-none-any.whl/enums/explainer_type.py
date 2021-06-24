from enum import Enum


class ExplainerType(Enum):
    NO_EXPLAINER = 0
    ANCHOR_TABULAR = 1
    ANCHOR_IMAGES = 2
    ANCHOR_TEXT = 3
    SHAP_KERNEL = 4
