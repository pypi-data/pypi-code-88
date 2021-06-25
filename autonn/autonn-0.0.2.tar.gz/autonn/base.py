from __future__ import annotations

import logging
import random
import sys
import typing
from abc import abstractmethod

import numpy as np

from .fields import Parameter
from .operator import AbstractOperator
from .utils import LoggerFormatter

__authors__ = ["Hao Wang"]


class BaseModel(AbstractOperator):
    """Base ML model"""

    random_seed = Parameter(42)  # the answer to life, universe, and everything
    verbose = Parameter(True)
    logger = Parameter(None)

    # TODO: some meta-information. generalize it to tags in the future
    # e.g., 'pytorch,regression..'
    _task: str = None

    def __init__(self, *args, **kwargs):
        # TODO: also make those protected?
        self.data_train: typing.Iterable = None
        self.data_val: typing.Iterable = None

        # protected attributes
        self._model = None
        self._perform_validation: bool = False  # if validation will be performed
        super().__init__(*args, **kwargs)

    def set_data(
        self, data_train: typing.Iterable, data_val: typing.Optional[typing.Iterable] = None
    ) -> BaseModel:
        """Set the training and validation data set (optional) and validate
        both data sources

        Parameters
        ----------
        data_train : Iterable
            The training data set
        data_val : Optional[Iterable], optional
            The validation data set, by default None

        Returns
        -------
        self : a BaseOperator instance
        """
        self.validate_data(data_train)
        self.validate_data(data_val)
        self.data_train = data_train
        self.data_val = data_val
        self._perform_validation = self.data_val is not None
        return self

    @abstractmethod
    def validate_data(self, data: typing.Iterable):
        pass

    def predict(self, X):
        assert self._model is not None
        y_ = self._model.predict(X)
        if self._task == "classification":
            y_ = np.zeros_like(y_)
            y_[np.arange(len(y_)), y_.argmax(axis=1)] = 1

        return y_

    def predict_prob(self, X):
        assert self._task == "classification"
        return self._model.predict(X)

    def save(self, filename: str, exclude: typing.List[str]):
        """Dump the operator to a file, excluding member vars `data_train` and
        `data_val` by default

        Parameters
        ----------
        filename : str
            The dump file name
        """
        # NOTE: `data_train/data_val` are iterators
        exclude += ["data_train", "data_val"]
        super().save(filename, exclude)

    def set_logger(self, logger: typing.Union[str, logging.Logger] = None) -> BaseModel:
        """set the logger of this operator

        Parameters
        ----------
        logger : Union[str, logging.Logger, None], optional
            Either a file name or an instance of the `logging.Logger` class.
            When set to None (by default), no logging action will be taken.

        Returns
        -------
        self : a BaseModel instance
        """
        if isinstance(logger, logging.Logger):
            self._logger = logger
            self._logger.propagate = False
            return self

        # NOTE: logging.getLogger create new instance based on `name`
        # no new instance will be created if the same name is provided
        self._logger = logging.getLogger(f"{self.__class__.__name__}({id(self)})")
        self._logger.setLevel(logging.DEBUG)
        fmt = LoggerFormatter()

        # create console handler and set level to the vebosity
        SH = list(filter(lambda h: isinstance(h, logging.StreamHandler), self._logger.handlers))
        if self.verbose and len(SH) == 0:
            # create console handler and set level to warning
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(logging.INFO)
            ch.setFormatter(fmt)
            self._logger.addHandler(ch)

        # create file handler and set level to debug
        if logger is not None:
            fh = logging.FileHandler(logger)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(fmt)
            self._logger.addHandler(fh)

        if hasattr(self, "logger"):
            self._logger.propagate = False
        return self

    def set_random_seed(self, random_seed: int) -> BaseModel:
        """Set the random state

        Parameters
        ----------
        random_seed : int
            the random seed
        """
        self._random_seed = random_seed
        np.random.seed(self._random_seed)
        random.seed(self._random_seed)
        return self


class BasePipeline(AbstractOperator):
    pass


class SimplePipeline(AbstractOperator):
    pass
