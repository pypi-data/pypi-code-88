from __future__ import annotations

import numpy as np
import torch
from sklearn.svm import (
    SVC
)

from ..base import BaseModel
from ..fields import (
    RealHyperParameter,
    DiscreteHyperParameter,
    OrdinalHyperParameter
)

__authors__ = ['Hao Wang']


class SupportVectorClassifier(BaseModel):
    """Wrapper for sklearn's SVC"""
    C = RealHyperParameter([1e-2, 10], 1.0, scale='log10')
    kernel = DiscreteHyperParameter(['linear', 'poly', 'rbf', 'sigmoid'], 'sigmoid')
    degree = OrdinalHyperParameter(
        [1, 5], 3, conditions="`kernel` != 'poly'", action=0
    )
    gamma = DiscreteHyperParameter(
        ['scale', 'auto'], 'scale',
        conditions="`kernel` not in ['poly', 'rbf', 'sigmoid']", action='scale'
    )
    coef0 = RealHyperParameter(
        [1e-5, 10], 0, scale='log10',
        conditions="`kernel` not in ['poly', 'sigmoid']", action=0
    )

    @staticmethod
    def _unzip_data(data_iter):
        X, y = [], []
        for data, target in data_iter:
            if isinstance(data, torch.Tensor):
                data = data.detach().cpu().numpy()
            if isinstance(target, torch.Tensor):
                target = target.detach().cpu().numpy()
            X.append(data)
            y.append(target)
        return np.concatenate(X, axis=0), np.concatenate(y, axis=0)

    def fit(self) -> SupportVectorClassifier:
        # construct the support vector machine from hyper-parameter
        self._model = SVC(
            **self.get_hyper_params(),
            random_state=self.random_seed
        )
        # training
        self._model.fit(*self._unzip_data(self.data_train))
        # testing
        if self._perform_validation:
            self.best_perf = self._model.score(*self._unzip_data(self.data_val))
        return self
