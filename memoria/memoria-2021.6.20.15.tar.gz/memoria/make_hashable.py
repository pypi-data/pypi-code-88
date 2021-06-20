from pyspark.sql.dataframe import DataFrame as SparkDF
from pandas import DataFrame as PandasDF
import numpy as np

from functools import reduce
from ._hash_int import hash_int

from ._pandas_helpers import concat_pandas_columns, map_pandas_to_int, aggregate_pandas_int
from ._spark_helpers import concat_spark_columns, map_spark_to_int, aggregate_spark_int


def represent_and_encode(obj):
	class_representation = f'{obj.__class__.__module__}|{obj.__class__.__name__}'
	obj_representation = repr(make_hashable(obj))
	representation = f'{class_representation}|{obj_representation}'
	return representation.encode()


def make_hashable(obj):
	if hasattr(obj, '__hashkey__'):
		return make_hashable(obj.__hashkey__())
	else:
		if isinstance(obj, (tuple, list)):
			return tuple((make_hashable(e) for e in obj))

		if isinstance(obj, dict):
			return tuple(sorted((k, make_hashable(v)) for k, v in obj.items()))

		if isinstance(obj, (set, frozenset)):
			return tuple(sorted(make_hashable(e) for e in obj))

		if isinstance(obj, (SparkDF, PandasDF)):
			return make_dataframe_hashable(data=obj)

		return obj


def make_dataframe_hashable(data):
	"""
	:type data: SparkDF or PandasDF
	:rtype: tuple
	"""

	# turn the dataframe into a single column of concatenated values
	# this makes sure if two cells in the same column are swapped the change is captured in this column
	# even though it will be ignored by the aggregation of each column
	data = data
	name = 'concat_column'
	sep = '|'
	return_data = True

	if isinstance(data, SparkDF):
		spark_compressed = concat_spark_columns(data=data, name=name, sep=sep, return_data=return_data)
		use = 'spark'
	elif isinstance(data, PandasDF):
		pandas_compressed = concat_pandas_columns(data=data, name=name, sep=sep, return_data=return_data)
		use = 'pandas'
	else:
		raise TypeError(f'data of type "{type(data)}" is not supported!')

	# convert each value in the column into an int hash

	if use == 'spark':
		spark_int_data = map_spark_to_int(spark_compressed)
		spark_aggregate = aggregate_spark_int(spark_int_data)
		aggregate_dictionary = spark_aggregate.first().asDict()

	elif use == 'pandas':
		pandas_int_data = map_pandas_to_int(pandas_compressed)
		pandas_aggregate = aggregate_pandas_int(pandas_int_data)
		aggregate_dictionary =pandas_aggregate.to_dict()

	else:
		raise RuntimeError(f'Usage "{use}" is not supported!')

	return tuple(sorted((k, v) for k, v in aggregate_dictionary.items()))
