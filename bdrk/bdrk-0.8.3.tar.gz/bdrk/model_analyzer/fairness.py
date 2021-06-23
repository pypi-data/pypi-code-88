import logging
from abc import ABC, abstractmethod
from typing import Dict

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class Fairness(ABC):
    def __init__(
        self,
        fconfig: Dict,
        features: pd.DataFrame,
        predictions: np.array,
        labels: np.array,
    ):
        self.fconfig = fconfig
        self.features = features
        self.predictions = predictions
        self.labels = labels

    @abstractmethod
    def analyze_fairness(self):
        raise NotImplementedError

    @classmethod
    def binarize(cls, y, label):
        """Binarize array-like data according to label."""
        return (np.array(y) == label).astype(int)
