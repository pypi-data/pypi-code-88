import typing as t

import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from pydantic import BaseModel

from tktl.core.future.t import EndpointKinds

from .advanced import AdvancedEndpoint


class TypedEndpoint(AdvancedEndpoint):
    kind: EndpointKinds = EndpointKinds.TYPED

    @staticmethod
    def supported(
        *,
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, t.Any, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, t.Any, BaseModel, None] = None,
        profile: t.Optional[str] = None,
    ) -> bool:
        return (
            profile is None
            and isinstance(X, (type(BaseModel), type(t.Any)))
            and isinstance(y, (type(BaseModel), type(t.Any)))
        )
