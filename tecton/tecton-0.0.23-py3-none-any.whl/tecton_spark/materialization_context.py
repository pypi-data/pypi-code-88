from dataclasses import dataclass
from typing import Union

import pendulum
from pyspark.sql import Column
from pyspark.sql.functions import expr
from pyspark.sql.functions import lit
from typeguard import typechecked

from tecton_spark.errors import TectonValidationError


@dataclass
class BaseMaterializationContext:
    _feature_start_time: pendulum.DateTime
    _feature_end_time: pendulum.DateTime

    @property
    def feature_start_time(self) -> pendulum.DateTime:
        return self._feature_start_time

    @property
    def feature_end_time(self) -> pendulum.DateTime:
        return self._feature_end_time

    @property
    def feature_start_time_string(self) -> str:
        return self.feature_start_time.to_datetime_string()

    @property
    def feature_end_time_string(self) -> str:
        return self.feature_end_time.to_datetime_string()

    @typechecked
    def feature_time_filter_sql(self, timestamp_expr: str) -> str:
        return f"('{self.feature_start_time_string}' <= ({timestamp_expr}) AND ({timestamp_expr}) < '{self.feature_end_time_string}')"

    @typechecked
    def feature_time_filter_pyspark(self, timestamp_expr: Union[str, Column]) -> Column:
        if isinstance(timestamp_expr, str):
            timestamp_col = expr(timestamp_expr)
        return (lit(self.feature_start_time_string) <= timestamp_col) & (
            timestamp_col < lit(self.feature_end_time_string)
        )


@dataclass
class UnboundMaterializationContext(BaseMaterializationContext):
    """
    This is only meant for instantiation in transformation default args. Using it directly will fail.
    """

    @property
    def feature_start_time(self):
        raise TectonValidationError(
            "tecton.materialization_context() must be passed in via a kwarg default only. Instantiation in function body is not allowed."
        )

    @property
    def feature_end_time(self):
        raise TectonValidationError(
            "tecton.materialization_context() must be passed in via a kwarg default only. Instantiation in function body is not allowed."
        )


@dataclass
class BoundMaterializationContext(BaseMaterializationContext):
    pass


def materialization_context():
    dummy_time = pendulum.datetime(1970, 1, 1)
    return UnboundMaterializationContext(_feature_start_time=dummy_time, _feature_end_time=dummy_time)
