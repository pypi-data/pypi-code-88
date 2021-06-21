import re
import sys
import time
import collections
from difflib import SequenceMatcher

def print_duration(method):
    '''Prints out the runtime duration of a method in seconds
    usage:

    from zwutils.comm import print_duration

    @print_duration
    def test_func():
        pass

    test_func()
    '''
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%s cost %2.2f second(s)' % (method.__name__, te - ts))
        return result
    return timed

def list_intersection(a, b, ordered=False):
    if ordered:
        return [i for i, j in zip(a, b) if i == j]
    else:
        return list(set(a).intersection(b)) # choose smaller to a or b?

def list_split(arr, num):
    ''' split list into several parts
    '''
    rtn = []
    arrlen = len(arr)
    step = int(arrlen / num) + 1
    for i in range(0, arrlen, step):
        rtn.append(arr[i:i+step])
    return rtn

def list_uniqify(arr):
    '''Remove duplicates from provided list but maintain original order.
        Derived from http://www.peterbe.com/plog/uniqifiers-benchmark
    '''
    seen = {}
    result = []
    for item in arr:
        if item.lower() in seen:
            continue
        seen[item.lower()] = 1
        result.append(item.title())
    return result

def list_compare(a, b):
    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    return compare(a, b)
