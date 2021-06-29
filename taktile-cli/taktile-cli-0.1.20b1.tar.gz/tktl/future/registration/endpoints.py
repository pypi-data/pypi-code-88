import abc
import typing as t

import numpy as np  # type: ignore
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
        **kwargs,
    ):
        self._kwargs = kwargs
        self._name = name
        self._func = func
        self._X = X
        self._y = y

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

    @staticmethod
    @abc.abstractmethod
    def supported(
        *,
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        profile: t.Optional[str] = None,
    ) -> bool:
        """supported.
        Given the parameters, is this tyep of endpoint supported?

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


class BasicEndpoint(Endpoint):
    kind: EndpointKinds = EndpointKinds.BASIC

    @staticmethod
    def supported(
        *,
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        profile: t.Optional[str] = None,
    ) -> bool:
        return profile is None and X is None and y is None


class TypedEndpoint(Endpoint):
    kind: EndpointKinds = EndpointKinds.TYPED

    @staticmethod
    def supported(
        *,
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        profile: t.Optional[str] = None,
    ) -> bool:
        return (
            profile is None
            and isinstance(X, type(BaseModel))
            and isinstance(y, type(BaseModel))
        )


class ArrowEndpoint(TypedEndpoint):
    kind: EndpointKinds = EndpointKinds.ARROW

    @staticmethod
    def supported(
        *,
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        profile: t.Optional[str] = None,
    ) -> bool:
        return (
            profile is None
            and isinstance(X, (np.ndarray, pd.DataFrame, pd.Series))
            and isinstance(y, (np.ndarray, pd.DataFrame, pd.Series))
        )


class ProfiledEndpoint(ArrowEndpoint):
    kind: EndpointKinds = EndpointKinds.PROFILED

    @staticmethod
    def supported(
        *,
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        profile: t.Optional[str] = None,
    ) -> bool:
        return (
            profile in ProfileKinds.set()
            and isinstance(X, (np.ndarray, pd.DataFrame, pd.Series))
            and isinstance(y, (np.ndarray, pd.DataFrame, pd.Series))
        )
