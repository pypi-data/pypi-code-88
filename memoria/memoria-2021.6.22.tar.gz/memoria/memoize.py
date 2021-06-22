import functools
from disk import Path
from .Cache import Cache


def memoize(path, n_jobs, exclude_kwargs=None, s3=None, spark=None, id=0, echo=1):
	"""
	makes a decorator for memoizing a function
	:type path: amazonian.S3.S3Path or Path or str
	:type n_jobs: int
	:type id: int
	:type exclude_kwargs: list or tuple
	:type s3: amazonian.S3.S3
	:type spark: pyspark.sql.session.SparkSession
	:rtype: callable
	"""

	if s3 is not None:
		if isinstance(path, str):
			path = s3 / path

	if spark is not None:
		try:
			if path.spark is None:
				path.set_spark(spark)
		except AttributeError:
			pass

	def decorator(function):
		"""
		memoizes a function
		:type function: callable
		:rtype: callable
		"""
		cache = Cache(path=path, n_jobs=n_jobs, spark=spark, echo=echo)

		if not isinstance(exclude_kwargs, (list, tuple)) and exclude_kwargs is not None:
			raise TypeError(f'exclude_kwargs is of type {type(exclude_kwargs)}! None, list, and tuple are accepted.')

		@functools.wraps(function)
		def wrapper(*args, **kwargs):
			if exclude_kwargs is not None:
				kwargs_in_key = {key: value for key, value in kwargs.items() if key not in exclude_kwargs}
			else:
				kwargs_in_key = kwargs.copy()

			key = (id, function.__name__, function.__doc__, args, kwargs_in_key)
			if key in cache:
				result = cache[key]
			else:
				result = function(*args, **kwargs)
				cache[key] = result
			return result

		wrapper.cache = cache
		wrapper.excluded_kwargs = exclude_kwargs
		return wrapper
	return decorator
