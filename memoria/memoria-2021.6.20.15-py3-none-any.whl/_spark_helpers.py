from functools import reduce
from pyspark.sql.dataframe import DataFrame as SparkDF
from pyspark.sql.types import LongType
from pyspark.sql import functions as f
from ._hash_int import hash_int


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