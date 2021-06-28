import typing as t

import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from pydantic import BaseModel

from .endpoints import ArrowEndpoint, BasicEndpoint, ProfiledEndpoint, TypedEndpoint

# Enpoint types sorted by precedence
ENDPOINT_TYPES = [ProfiledEndpoint, ArrowEndpoint, TypedEndpoint, BasicEndpoint]


class Tktl:
    def __init__(self):
        self._endpoints = []

    @property
    def endpoints(self):
        return self._endpoints

    def endpoint(
        self,
        *,
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, BaseModel, None] = None,
        profile: t.Optional[str] = None,
        profile_columns: t.Optional[t.List[str]] = None,
        **kwargs,
    ):

        try:
            Constructor = next(
                endpoint
                for endpoint in ENDPOINT_TYPES
                if endpoint.supported(X=X, y=y, profile=profile)
            )
        except StopIteration:
            raise ValueError(
                f"Arguments of type X={type(X)} y={type(y)} and profile={profile}"
                " are not supported by any endpoint type."
            )

        def decorator(f):
            endpoint = Constructor(name=f.__name__, func=f, **kwargs, X=X, y=y)
            self._endpoints.append(endpoint)
            return f

        return decorator
