import typing as t

import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from pydantic import BaseModel

from tktl.core.future.t import EndpointKinds

from .abc import Endpoint


class AdvancedEndpoint(Endpoint):
    kind: EndpointKinds = EndpointKinds.ADVANCED

    @staticmethod
    def supported(
        *,
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, t.Any, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, t.Any, BaseModel, None] = None,
        profile: t.Optional[str] = None,
    ) -> bool:
        return profile is None and X is None and y is None
