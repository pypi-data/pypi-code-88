import abc
import typing as t

import numpy as np
import pandas as pd  # type: ignore
from fastapi import Response
from pydantic import BaseModel

from tktl.core.future.t import EndpointKinds, ProfileKinds


class Endpoint(abc.ABC):
    kind: EndpointKinds

    def __init__(
        self,
        name: str,
        func: t.Callable[..., t.Coroutine[t.Any, t.Any, Response]],
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        profile_columns: t.Optional[t.List[str]] = None,
        profile: t.Optional[ProfileKinds] = None,
        **kwargs,
    ):
        self._kwargs = kwargs
        self._name = name
        self._func = func
        self._X = X
        self._y = y
        self._profile_columns = profile_columns
        self._profile_kind = profile

    @property
    def kwargs(self):
        return self._kwargs

    @property
    def name(self):
        return self._name

    @property
    def func(self):
        return self._func

    @property
    def X(self):
        return self._X

    @property
    def y(self):
        return self._y

    @property
    def profile_kind(self):
        return self._profile_kind

    @property
    def profile_columns(self):
        return self._profile_columns

    @property
    def input_names(self):
        return []

    @property
    def output_names(self):
        return ""

    @staticmethod
    @abc.abstractmethod
    def supported(
        *,
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, t.Any, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, t.Any, BaseModel, None] = None,
        profile: t.Optional[str] = None,
    ) -> bool:
        """supported.
        Given the parameters, is this type of endpoint supported?

        Parameters
        ----------
        X : t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None]
        y : t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None]
        profile : t.Optional[str]
            the paramters

        Returns
        -------
        bool - true if supported, false else

        """
