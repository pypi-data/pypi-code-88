from pyspark import SparkContext
from pyspark.sql.column import Column, _to_java_column  # type: ignore


def _get_get_jvm_function(name, sc):
    """
    Retrieves JVM function identified by name from
    Java gateway associated with sc.
    """
    return getattr(sc._jvm.org.streamstate.streamstateutils.functions, name)


def _invoke_function(name, *args):
    """
    Invokes JVM function identified by name with args
    and wraps the result with :class:`~pyspark.sql.Column`.
    """
    jf = _get_get_jvm_function(name, SparkContext._active_spark_context)
    return Column(jf(*args))


def _invoke_function_over_column(name, col):
    """
    Invokes unary JVM function identified by name
    and wraps the result with :class:`~pyspark.sql.Column`.
    """
    return _invoke_function(name, _to_java_column(col))


def geometricMean(col):
    return geometric_mean(col)


def geometric_mean(col):
    return _invoke_function_over_column("geometricMean", col)


def standardDeviation(col):
    return standard_deviation(col)


def standard_deviation(col):
    return _invoke_function_over_column("standardDeviation", col)
