from sklearn.base import BaseEstimator
import numpy as np
from sklearn.base import clone
from .logs.loggers import get_logger
import math


class DeepModel(BaseEstimator):

    def __init__(self, estimator, depths, n_estimators=100,
                 learning_rate=0.01, verbose=True, logging=None, logging_params={}):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.verbose = verbose
        self.depths = depths
        self.estimator = estimator
        self.logger = get_logger(logging, 'DeepModel', logging_params)

    def fit(self, X_train, y_train):
        self.models = []
        self.logger('Training...')
        feed = y_train.copy()
        for depth in self.depths:
            self.logger(f"Depth: {depth}")
            model = clone(self.estimator)
            model.fit(X_train, feed)
            self.models.append(model)
            preds = model.predict(X_train)
            feed -= preds
            self.logger('%.15f' % np.mean(abs(feed)))

    def predict(self, X_test):
        preds = np.zeros(X_test.shape[0])
        for model in self.models:
            preds += model.predict(X_test)
            return preds
        return preds


class EarlyStoppingError(Exception):
    pass


class EarlyStopping:

    def __init__(self, direction, patience=100, threshold=1e-3):
        self.best = -math.inf if direction == 'maximize' else math.inf
        self.fn = max if direction == 'maximize' else min
        self.count = 0
        self.threshold = threshold
        self.patience = patience

    def __call__(self, value):
        new_value = self.fn(self.best, value)
        if abs(new_value - self.best) < self.threshold:
            self.count += 1
            if self.count > self.patience:
                raise EarlyStoppingError()
        else:
            self.count = 0
            self.best = new_value