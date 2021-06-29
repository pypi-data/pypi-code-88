import typing as t

import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from pydantic import BaseModel

from tktl.core.future.t import EndpointKinds
from tktl.future.registration.exceptions import ValidationError
from tktl.future.registration.serialization import deserialize, serialize, to_example
from tktl.future.registration.validation import validate
from tktl.future.utils import JSONStructure

from .typed import TypedEndpoint


class ArrowEndpoint(TypedEndpoint):
    kind: EndpointKinds = EndpointKinds.ARROW

    @staticmethod
    def supported(
        *,
        X: t.Union[pd.Series, pd.DataFrame, np.ndarray, t.Any, BaseModel, None] = None,
        y: t.Union[pd.Series, pd.DataFrame, np.ndarray, t.Any, BaseModel, None] = None,
        profile: t.Optional[str] = None,
    ) -> bool:
        return (
            profile is None
            and isinstance(X, (np.ndarray, pd.DataFrame, pd.Series))
            and isinstance(y, (np.ndarray, pd.DataFrame, pd.Series))
        )

    def deserialize_function(
        self,
    ) -> t.Callable[[str], t.Union[pd.Series, pd.DataFrame, np.ndarray]]:
        def _deserialize(serial_value):
            try:
                value = deserialize(self._X, value=serial_value)
                value = validate(value, sample=self._X)
                return value
            except ValidationError as exc:
                raise ValidationError(f"Validation error on input: {str(exc)}") from exc

        return _deserialize

    def serialize_function(self) -> t.Callable[[t.Any], str]:
        def _serialize(value):
            try:
                value = validate(value, sample=self._y)
                return serialize(value)
            except ValidationError as exc:
                raise ValidationError(
                    f"Validation error on output: {str(exc)}"
                ) from exc

        return _serialize

    def request_type(self) -> object:
        return JSONStructure

    def request_example(self) -> t.Any:
        return to_example(self._X)

    def response_type(self) -> object:
        if isinstance(self._y, pd.DataFrame):
            return str
        return JSONStructure

    def response_example(self) -> t.Any:
        return to_example(self._y)
