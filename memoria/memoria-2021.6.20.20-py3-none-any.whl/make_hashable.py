from pyspark.sql.dataframe import DataFrame as SparkDF
from pandas import DataFrame as PandasDF

import numpy as np
from functools import reduce
from pyspark.sql.types import LongType
from pyspark.sql import functions as f
import hashlib
import base64

from .to_bytes import to_bytes


def hash_int(x):
	s = represent_and_encode(x)
	_hash_maker = hashlib.sha256()

	encoded = to_bytes(s)  # instead of x.encode()
	_hash_maker.update(encoded)
	return hash(base64.b64encode(_hash_maker.digest()).decode())


def concat_spark_columns(data, name='concat_column', sep='|', return_data=False):
	"""
	concatenates each row and creates a new column
	:type data: SparkDF
	:type name: str
	:type sep: str
	:type return_data: bool
	:param return_data: if True, the whole data frome with the new column is returned, otherwise just the column
	:rtype: SparkDF
	"""
	data = data.withColumn(
		name, f.concat_ws(
			sep, *[f.col(col) for col in data.columns]
		)
	)

	if return_data:
		return data
	else:
		return data.select(name)


def map_spark_to_int(data):
	def _map_function(row):
		"""
		:type row: Row
		:rtype: list[int]
		"""
		return [hash_int(x) for column, x in row.asDict().items()]

	return data.rdd.map(_map_function).toDF(data.columns)


def aggregate_spark_int(data):
	@f.udf(LongType())
	def spark_bitwise_xor(numbers):
		return reduce(lambda x, y: x ^ y, numbers)

	return data.agg(*[
		spark_bitwise_xor(f.collect_list(col)).alias(col)
		for col in data.columns
	])


def concat_pandas_columns(data, name='concat_column', sep='|', return_data=False):
	"""
	concatenates each row and creates a new column
	:type data: PandasDF
	:type name: str
	:type sep: str
	:type return_data: bool
	:param return_data: if True, the whole dataframe with the new column is returned, otherwise just the column
	:rtype: PandasDF
	"""
	def concat_row(x):
		return sep.join([str(value) for value in x.values if value is not None])

	data = data.copy()
	if name in data.columns:
		data.drop(columns=name, inplace=True)
	data[name] = data.apply(concat_row, axis=1)

	if return_data:
		return data
	else:
		return data[[name]]


def map_pandas_to_int(data):
	try:
		pandas_int_data = data.applymap(hash_int, na_action=None)
	except TypeError:
		pandas_int_data = data.apply(lambda x: x.map(hash_int, na_action=None))
	return pandas_int_data


def aggregate_pandas_int(data):
	def pandas_bitwise_xor(numbers):
		return reduce(lambda x, y: np.bitwise_xor(x, y), numbers)

	return data.agg(pandas_bitwise_xor, axis='rows')


def represent_and_encode(obj):
	class_representation = f'{obj.__class__.__name__}'
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
		aggregate_dictionary = pandas_aggregate.to_dict()

	else:
		raise RuntimeError(f'Usage "{use}" is not supported!')

	return tuple(sorted((k, v) for k, v in aggregate_dictionary.items()))
