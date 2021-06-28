import traceback
from contextlib import contextmanager
from typing import Mapping, Optional

from sfu_ml_lib.base.metrics import NumericType, PrimitiveType


class Tracker:
    def set_tags(self, tags: Mapping[str, str]) -> None:
        raise NotImplementedError

    def register_parameters(self, parameters: Mapping[str, PrimitiveType]) -> None:
        raise NotImplementedError

    def log_metrics(self, metrics: Mapping[str, NumericType], step: Optional[int] = None) -> None:
        raise NotImplementedError

    def save_model(self, path: str) -> None:
        raise NotImplementedError

    def finish_epoch(self) -> None:
        raise NotImplementedError

    def __enter__(self) -> 'Tracker':
        raise NotImplementedError

    def __exit__(self, context_type, value, trace_back) -> None:
        raise NotImplementedError

    @contextmanager
    def exception_logging(self, limit: int = 10):
        try:
            yield

        except Exception as error:
            self.set_tags({'Error': traceback.format_exc(limit=limit)})
            raise error
