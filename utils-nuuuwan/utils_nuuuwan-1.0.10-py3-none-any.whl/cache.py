"""Utils for caching functions."""
import hashlib
import json
import os
import threading
import time
from functools import wraps

from utils import filex

CACHE_DIR = '/tmp/cache'
CACHE_DEFAULT_TIMEOUT = 60


class _Cache:
    """Implements base cache logic.

    Data is cached both in memory and, for persistance, on disk. On *get*
    requests, memory is first inspected. If cache key is not found there,
    disk is inspected.

    Args:
        cache_name(str): Name to identify cache.
        timeout (int): timeout in seconds

    Note:
        Used by decorator *cache* (See below).

    """

    @staticmethod
    def __get_hash(cache_key):
        return hashlib.md5(cache_key.encode()).hexdigest()

    __dir = '/tmp/cache'
    __store = {}
    __lock_map_lock = threading.Lock()
    __lock_map = {}
    __cache_name = 'new_cache'

    def __init__(self, cache_name, timeout=CACHE_DEFAULT_TIMEOUT):
        """Implement class constructor."""
        self.__cache_name = cache_name
        self.__timeout = timeout
        os.system('mkdir -p %s' % self.__get_dir())

    def __get_dir(self):
        return '%s/%s' % (CACHE_DIR, self.__cache_name)

    def __get_lock(self, key):
        # pylint: disable=R1732
        self.__lock_map_lock.acquire()
        if key not in self.__lock_map:
            self.__lock_map[key] = threading.Lock()
        lock = self.__lock_map[key]
        self.__lock_map_lock.release()
        return lock

    def __acquire_lock(self, key):
        self.__get_lock(key).acquire()

    def __release_lock(self, key):
        self.__get_lock(key).release()

    def __get_cache_file_name(self, cache_key):
        return '%s/%s' % (
            self.__get_dir(),
            _Cache.__get_hash(cache_key),
        )

    def __get_file_exists(self, key):
        return os.path.exists(self.__get_cache_file_name(key))

    def __get_from_file(self, key):
        data_json = filex.read(self.__get_cache_file_name(key))

        if data_json == '':
            return None
        packet = json.loads(data_json)
        return packet

    def __set(self, key, data):
        self.__acquire_lock(key)
        packet = {
            'data': data,
            'set_time': time.time(),  # TODO: Change this later to use timex
        }
        filex.write(
            self.__get_cache_file_name(key),
            json.dumps(packet, ensure_ascii=True),
        )
        self.__store[key] = packet
        self.__release_lock(key)

    def get(self, key_or_list, fallback):
        """Get data from cache if cache key exists, if not from fallback.

        Args:
            key_or_list (str or list): the cache key can be given as a string,
                or a list of strings, which are joined
            fallback (function): function to call of cache key not in cache

        Returns:
            data

        """
        if isinstance(key_or_list, list):
            key = ':'.join(key_or_list)
        else:
            key = key_or_list

        packet = None

        if key in self.__store:
            packet = self.__store[key]

        if not packet:
            if self.__get_file_exists(key):
                packet = self.__get_from_file(key)
                if packet is not None:
                    self.__store[key] = packet

        if packet:
            if 'set_time' in packet:
                min_set_time = time.time() - self.__timeout
                if packet['set_time'] > min_set_time:
                    return packet['data']

        data = fallback()
        if data is not None:
            self.__set(key, data)
        return data

    def flush_store(self):
        """Flush all cache."""
        self.__store = {}

    def flush(self, key):
        """Flush cache for a given cache key.

        Args:
            key (str): Cache key to flush
        """
        self.__acquire_lock(key)
        if self.__get_file_exists(key):
            os.remove(self.__get_cache_file_name(key))
        if key in self.__store:
            del self.__store[key]
        self.__release_lock(key)


def cache(cache_name, timeout=CACHE_DEFAULT_TIMEOUT):
    """Wrap class Cache as decorator.

    Args:
        cache_name (str): cache name
        timeout (int): timeout in seconds

    .. code-block:: python

        from utils.cache import cache

        @cache('test', 86400)
        def long_operation():
            import time
            time.sleep(100)
            return 1

        >>> long_operation() # takes >100s to run
        >>> long_operation() # runs almost instantly

    """

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
