from amazondax.Cache import *

import threading
import random
import time

from collections import defaultdict
from pprint import pprint

import pytest

LETTERS = {i: chr(i) for i in range(ord('A'), ord('Z')+1)}

def test_simple_cache():
    fetch = track_calls(lambda key, tube: LETTERS[key])
    cache = SimpleCache(1, fetch)

    result = cache.get(74, None)
    assert result == 'J'
    assert fetch.calls == 1

def test_simple_cache_reuse():
    fetch = track_calls(lambda key, tube: LETTERS[key])
    cache = SimpleCache(1, fetch)

    result = cache.get(74, None)
    assert result == 'J'

    result = cache.get(74, None)
    assert result == 'J'
    assert fetch.calls == 1
    assert len(cache._cache) == 1

def test_simple_cache_eviction():
    fetch = track_calls(lambda key, tube: LETTERS[key])
    cache = SimpleCache(1, fetch)

    result = cache.get(74, None)
    assert result == 'J'
    assert fetch.calls == 1
    
    result = cache.get(75, None)
    assert result == 'K'
    assert fetch.calls == 2
    assert len(cache._cache) == 1

    result = cache.get(74, None)
    assert result == 'J'
    assert fetch.calls == 3
    assert len(cache._cache) == 1

@pytest.mark.skip
def test_simple_cache_threading():
    cache = SimpleCache(10, lambda key, tube: LETTERS[key])
    running = True

    results = defaultdict(list)

    LETTER_KEYS = list(LETTERS.keys())
    def run_fetch():
        tid = threading.get_ident()
        print(tid, threading.current_thread().name)
        while running:
            n = random.choice(LETTER_KEYS)
            l = cache.get(n, None)
            results[tid].append((n, l))

    threads = [threading.Thread(target=run_fetch, name="SCThread" + str(i)) for i in range(10)]
    for thread in threads:
        thread.start()

    time.sleep(5)
    running = False

    for thread in threads:
        thread.join()

    # pprint(results)
    assert False

def test_refreshing_cache():
    fetch = track_calls(lambda key, tube: LETTERS[key])
    cache = RefreshingCache(1, fetch, 1000)

    result = cache.get(74, None)
    assert result == 'J'

def test_refreshing_cache_expiry():
    fetch = track_calls(lambda key, tube: LETTERS[key])
    clock = callable_seq([1, 1.5, 3, 4, 5])  # Clocks are in seconds, ttl in millis
    cache = RefreshingCache(1, fetch, ttl_millis=1000, clock=clock)

    result = cache.get(74, None)
    assert result == 'J'
    assert fetch.calls == 1

    result = cache.get(74, None)
    assert result == 'J'
    assert fetch.calls == 1

    result = cache.get(74, None)
    assert result == 'J'
    assert fetch.calls == 2

class track_calls(object):
    def __init__(self, f):
        self.f = f
        self.calls = 0
    
    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.f(*args, **kwargs)

def callable_seq(seq):
    it = iter(seq)
    return lambda: next(it)

