from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import attr
import numpy
import pandas
import pyspark
import pytz

from tecton._internals.sdk_decorators import sdk_public_method


def set_pandas_timezone_from_spark(pandas_df):
    """Match pandas timezone to that of Spark, s.t. the timestamps are correctly displayed."""
    from tecton.tecton_context import TectonContext

    tz = TectonContext.get_instance()._spark.conf.get("spark.sql.session.timeZone")
    for col in pandas_df.columns:
        if pandas.core.dtypes.common.is_datetime64_dtype(pandas_df[col]):
            pandas_df[col] = pandas_df[col].dt.tz_localize(pytz.timezone(tz))
            pandas_df[col] = pandas_df[col].dt.tz_convert(pytz.timezone("UTC"))
            pandas_df[col] = pandas_df[col].dt.tz_localize(None)
    return pandas_df


@attr.s(auto_attribs=True)
class FeatureVector(object):
    """
    FeatureVector Class.

    A FeatureVector is a representation of a single feature vector. Usage of a FeatureVector typically involves
    extracting the feature vector using ``to_pandas()``, ``to_dict()``, or ``to_numpy``.

    """

    _names: List[str]
    _values: List[Union[int, str, bytes, float]]

    @sdk_public_method
    def to_dict(self) -> Dict[str, Union[int, str, bytes, float, None]]:
        """Turns vector into a Python dict.

        :return: A Python dict.
        """
        return dict(zip(self._names, self._values))

    @sdk_public_method
    def to_pandas(self) -> pandas.DataFrame:
        """Turns vector into a Pandas DataFrame.

        :return: A Pandas DataFrame.
        """
        return pandas.DataFrame([self._values], columns=self._names)

    @sdk_public_method
    def to_numpy(self) -> numpy.array:
        """Turns vector into a numpy array.

        :return: A numpy array.
        """
        return numpy.array(self._values)

    def _update(self, other: "FeatureVector"):
        self._names.extend(other._names)
        self._values.extend(other._values)


@attr.s(auto_attribs=True)
class DataFrame(object):
    """
    DataFrame class.

    This class is a thin wrapper around a Spark / Pandas DataFrame. To access
    functionality, use the ``to_pandas`` or ``to_spark`` method.
    """

    _spark_df: Optional[pyspark.sql.DataFrame]
    _pandas_df: Optional[pandas.DataFrame]

    @sdk_public_method
    def to_spark(self) -> pyspark.sql.DataFrame:
        """Returns data as a Spark DataFrame."""
        if self._spark_df is not None:
            return self._spark_df

        from tecton.tecton_context import TectonContext

        tc = TectonContext.get_instance()
        return tc._spark.createDataFrame(self._pandas_df)

    @sdk_public_method
    def to_pandas(self) -> pandas.DataFrame:
        """Returns data as a Pandas DataFrame."""
        if self._pandas_df is not None:
            return self._pandas_df

        assert self._spark_df is not None
        return set_pandas_timezone_from_spark(self._spark_df.toPandas())

    @classmethod
    def _create(cls, df: Union[pyspark.sql.DataFrame, pandas.DataFrame]):
        """Creates a Tecton DataFrame from a Spark or Pandas DataFrame."""
        if isinstance(df, pandas.DataFrame):
            return cls(spark_df=None, pandas_df=df)
        elif isinstance(df, pyspark.sql.DataFrame):
            return cls(spark_df=df, pandas_df=None)

        raise TypeError(f"DataFrame must be of type pandas.DataFrame or pyspark.sql.Dataframe, not {type(df)}")
