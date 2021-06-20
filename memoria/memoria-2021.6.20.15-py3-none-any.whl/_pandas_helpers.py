from functools import reduce
import numpy as np
from pandas import DataFrame as PandasDF
from ._hash_int import hash_int


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
