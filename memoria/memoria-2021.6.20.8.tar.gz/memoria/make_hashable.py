from pyspark.sql.types import StringType, IntegerType
from pyspark.sql.dataframe import DataFrame as SparkDF
from pyspark.sql import functions as f
from pandas import DataFrame as PandasDF
import numpy as np

from functools import reduce
import hashlib
import base64

from .to_bytes import to_bytes


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


def concat_pandas_columns(data, name='concat_column', sep='|', return_data=False):
	"""
	concatenates each row and creates a new column
	:type data: PandasDF
	:type name: str
	:type sep: str
	:type return_data: bool
	:param return_data: if True, the whole data frome with the new column is returned, otherwise just the column
	:rtype: PandasDF
	"""
	def concat_row(x):
		return sep.join([str(value) for value in x.values])

	data[name] = data.apply(concat_row, axis=1)

	if return_data:
		return data
	else:
		return data[[name]]


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
	def _hash_int(x):
		s = represent_and_encode(x)
		_hash_maker = hashlib.sha256()

		encoded = to_bytes(s)  # instead of x.encode()
		_hash_maker.update(encoded)
		return hash(base64.b64encode(_hash_maker.digest()).decode())

	if use == 'spark':
		def _map_function(row):
			"""
			:type row: Row
			:rtype: list[int]
			"""
			return [_hash_int(x) for column, x in row.asDict().items()]

		spark_int_data = spark_compressed.rdd.map(_map_function,).toDF(spark_compressed.columns)

		@f.udf(IntegerType())
		def spark_bitwise_xor(numbers):
			return reduce(lambda x, y: x ^ y, numbers)

		spark_aggregate = spark_int_data.agg(*[
			spark_bitwise_xor(f.collect_list(col)).alias(col)
			for col in spark_int_data.columns
		])
		aggregate_dictionary = spark_aggregate.first().asDict()

	elif use == 'pandas':
		pandas_int_data = pandas_compressed.applymap(_hash_int, na_action=None)

		def pandas_bitwise_xor(numbers):
			return reduce(lambda x, y: np.bitwise_xor(x, y), numbers)

		aggregate_dictionary = pandas_int_data.agg(pandas_bitwise_xor, axis='rows').to_dict()

	else:
		raise RuntimeError(f'Usage "{use}" is not supported!')

	return tuple(sorted((k, v) for k, v in aggregate_dictionary.items()))
