"""Utils for caching functions."""
import json

from functools import wraps

from utils.cache_impl import _Cache

CACHE_DIR = '/tmp/cache'
CACHE_DEFAULT_TIMEOUT = 60


def cache(cache_name, timeout=CACHE_DEFAULT_TIMEOUT):
    """Wrap class Cache as decorator."""

    def cache_inner(func):

        @wraps(func)
        def cache_inner_inner(*args, **kwargs):
            cache_key = json.dumps({
                'cache_name': cache_name,
                'function_name': func.__name__,
                'kwargs': kwargs,
                'args': args,
            })

            def fallback():
                return func(*args, **kwargs)

            return _Cache(cache_name, timeout).get(cache_key, fallback)

        return cache_inner_inner
    return cache_inner
