# -*- coding: utf-8 -*-
__version__ = '1.0.8'
__license__ = 'MIT'

import time
import sys
import hashlib
import inspect
try:
    import cPickle as pickle
except:
    import pickle

from aio_tg_bot.etc.conf import settings
from functools import wraps
from aio_tg_bot.utils import module_loading
from .adapter.CacheException import CacheExpiredException
from .adapter.MemoryAdapter import MemoryAdapter



'''
wrapcache: wrap cache

A python Function / Method OUTPUT cache system base on function Decorators.

Auto cache the Funtion OUTPUT for sometime.
'''
def _from_file(function):
    if hasattr(function, '__code__'):
        return function.__code__.co_filename
    else:
        return ''

def _wrap_key(function, args, kws):
    '''
    get the key from the function input.
    '''
    return hashlib.md5(pickle.dumps((_from_file(function) + function.__name__, args, kws))).hexdigest()

def keyof(function, *args, **kws):
    '''
    get the function cache key
    '''
    return _wrap_key(function, args, kws)

def get(key):
    '''
    get the cache value
    '''
    adapter = module_loading.import_string(settings.WRAPCACHE_ADAPTER)
    try:
        return pickle.loads(adapter().get(key))
    except CacheExpiredException:
        return None

def remove(key):
    '''
    remove cache by key 
    '''
    adapter = module_loading.import_string(settings.WRAPCACHE_ADAPTER)
    return pickle.loads(adapter().remove(key))

def set(key, value, timeout = -1):
    '''
    set cache by code, must set timeout length
    '''
    adapter = module_loading.import_string(settings.WRAPCACHE_ADAPTER)
    if adapter(timeout = timeout).set(key, pickle.dumps(value)):
        return value
    else:
        return None

def flush():
    '''
    clear all the caches
    '''
    adapter = module_loading.import_string(settings.WRAPCACHE_ADAPTER)
    return adapter().flush()


def wrapcache(timeout = -1):
    '''
    the Decorator to cache Function.
    '''

    def _wrapcache(function):
        if inspect.iscoroutinefunction(function):
            wrap = async_wrapcache
        else:
            wrap = sync_wrapcache
        return wrap(function, timeout)

    return _wrapcache


def sync_wrapcache(function, timeout):
    @wraps(function)
    def _wrapcache(*args, **kws):
        hash_key = _wrap_key(function, args, kws)
        try:
            return get_value_and_pickle_loads(hash_key)
        except CacheExpiredException:
            # timeout
            value = function(*args, **kws)
            return set_and_return(hash_key, value, timeout)

    return _wrapcache


def async_wrapcache(function, timeout):
    @wraps(function)
    async def _wrapcache(*args, **kws):
        hash_key = _wrap_key(function, args, kws)
        try:
            return get_value_and_pickle_loads(hash_key)
        except CacheExpiredException:
            # timeout
            value = await function(*args, **kws)
            return set_and_return(hash_key, value, timeout)

    return _wrapcache


def get_value_and_pickle_loads(hash_key):
    adapter = module_loading.import_string(settings.WRAPCACHE_ADAPTER)

    adapter_instance = adapter()
    return pickle.loads(adapter_instance.get(hash_key))


def set_and_return(hash_key, value, timeout):
    set(hash_key, value, timeout)
    return value