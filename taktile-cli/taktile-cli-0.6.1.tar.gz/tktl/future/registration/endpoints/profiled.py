import typing as t

import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from pydantic import BaseModel

from tktl.core.future.t import EndpointKinds, ProfileKinds

from .arrow import ArrowEndpoint


class ProfiledEndpoint(ArrowEndpoint):
    kind: EndpointKinds = EndpointKinds.PROFILED

    @property
    def input_names(self):
        return self.profile_columns

    @property
    def output_names(self):
        return self.y.name

    @property
    def profile_columns(self) -> t.Optional[t.List[str]]:
        return (
            self._profile_columns
            if self._profile_columns is not None
            else self.X.columns.to_list()
        )

    @staticmethod
    def supported(
        *,
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, t.Any, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, t.Any, BaseModel, None] = None,
        profile: t.Optional[str] = None,
    ) -> bool:
        return (
            profile in ProfileKinds.set()
            and isinstance(X, pd.DataFrame)
            and isinstance(y, pd.Series)
        )
