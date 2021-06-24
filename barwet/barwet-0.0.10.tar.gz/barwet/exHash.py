import os
import json

from hashlib import md5
from random import shuffle, randint

from typing import Any, Callable

def md5(string: str):
    from hashlib import md5 as HASH_FN
    return HASH_FN(string.encode()).hexdigest()

def hash_string(string: str, fn: Callable[[str, ], str]=None) -> str:
    """Generate unique ID for a string.
    """
    if fn is None:
        return md5(string.encode()).hexdigest()
    else:
        return fn(string)


## 对字典键值对的唯一性进行哈希
def to_str(data: Any) -> str:
    if isinstance(data, dict):
        ks = sorted(list(data.keys()))
        d = {k: to_str(data[k]) for k in ks}
        return json.dumps(d)
    else:
        return json.dumps(data)

def hash_dict_content(data: dict) -> str:
    s = to_str(data)
    return hash_string(s)

def random_id(length=64, use: str='NAa', chars=''):
    x = {
        'N': '1234567890',
        'a': 'abcdefghijklmnopqrstuvwxyz',
        'A': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'S': '~`!@#$%^&*()_-+=[]{}\|;:\'",.<>/?'
    }
    y = {'N': 10, 'a': 26, 'A': 26, 'S': 33}

    keys = []
    for k in x:
        if k in use:
            keys.append(k)
            chars += x[k]

    chars = [i for i in chars]
    shuffle(chars)

    seq = ''
    for i in range(length):
        seq += chars[randint(0, len(chars)-1)]

    return seq
