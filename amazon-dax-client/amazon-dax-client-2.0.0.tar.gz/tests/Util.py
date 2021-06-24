import time
import random
import string
import itertools
import six

from collections import OrderedDict
from decimal import Decimal

from amazondax.Constants import STRING_TYPES, BINARY_TYPES, NUMBER_TYPES, SEQ_TYPES
from amazondax.Tube import Tube
from amazondax.DaxCborDecoder import DaxCborDecoder
from amazondax.DaxCborTypes import DdbSet, DocumentPathOrdinal

import pytest

def _mkmore(data):
    def more(buf, n):
        if more.p >= len(data):
            return -1
        q = more.p+n
        buf += data[more.p:q]
        more.p = q
        return n
    more.p = 0

    return more

def av(v):
    if v is None:
        return {'NULL': True}
    if isinstance(v, bool):
        return {'BOOL': v}
    if isinstance(v, STRING_TYPES):
        return {'S': v}
    elif isinstance(v, BINARY_TYPES):
        return {'B': v}
    elif isinstance(v, NUMBER_TYPES):
        return {'N': str(v)}
    elif isinstance(v, SEQ_TYPES):
        return {'L': [av(e) for e in v]}
    elif isinstance(v, dict):
        return {'M': {k: av(w) for k, w in v.items()}}
    elif isinstance(v, set):
        values = list(sorted(v))
        v = values[0]
        if isinstance(v, STRING_TYPES):
            return {'SS': values}
        elif isinstance(v, NUMBER_TYPES):
            return {'NS': [str(n) for n in values]}
        elif isinstance(v, BINARY_TYPES):
            return {'BS': values}
        else:
            raise TypeError('Unknown set type: ' + type(v).__name__)
    elif isinstance(v, DdbSet):
        return {v.type: v.values}
    else:
        raise TypeError('Unknown value type: ' + type(v).__name__)

class mocket(object):
    ''' A mock socket. '''
    def __init__(self, recv_buf):
        self.send_buf = bytearray()
        self.recv_buf = bytearray(recv_buf)

    def close(self):
        pass

    def recv(self, n):
        if len(self.recv_buf) == 0:
            raise Exception('No data')

        data = self.recv_buf[:n]
        del self.recv_buf[:n]
        return data

    def send(self, data):
        self.send_buf += data

    def sendall(self, data):
        self.send_buf += data

class MockCredential(object):
    access_key = u'AKIAFOO'
    secret_key = u'BAR'

def mktube(data, clock=time.time, version=None, **kwargs):
    m = mocket(data)
    return Tube(m, version, MockCredential, u'test', clock=clock, **kwargs)

def mktestkeys(_key_types, _key_sizes):
    random.seed(0)
    return list(itertools.chain(
        (_mkkey(i[0], i[1][0:1]) for i in itertools.product(_key_types, _key_sizes)),
        (_mkkey(i[0] + i[1], i[2]) for i in itertools.product(_key_types, _key_types, _key_sizes))))

_names = ['attr' + str(i) for i in range(2)]
def _mkkey(schema, sizes):
    key_attrs = [ \
        ((nm, {ty: _mkkeyval(ty, sz)}), {'AttributeName': nm, 'AttributeType': ty})     \
        for ty, sz, nm in zip(schema, sizes, _names) \
    ]

    key = tuple(zip(*key_attrs))
    param_id = ':'.join(''.join(str(i) for i in u) for u in zip(schema, sizes))
    return pytest.param(dict(key[0]), key[1], id=param_id)

_random_str_stuff = string.ascii_lowercase + string.digits
_random_bytes_stuff = [chr(i) if six.PY2 else bytes([i]) for i in range(256)]

def _mkkeyval(_type, size):
    if _type == 'S':
        return random_str(size)
    elif _type == 'B':
        return random_bytes(size)
    elif _type == 'N':
       return random.randint(0, size)
    else:
        raise Exception('Unknown type ' + _type)

def random_str(size):
    return ''.join(random.choice(_random_str_stuff) for _ in range(size))

def random_bytes(size):
    return b''.join(random.choice(_random_bytes_stuff) for _ in range(size))

def sexp(data):
    dec = DaxCborDecoder(_mkmore(data))
    arr = dec.decode_array()
    if len(arr) == 2:
        # Projection Expr (no values)
        fmt, expr = arr
        values = []
    else:
        fmt, expr, values = arr

    return _format_sexp(expr), [av(v) for v in values]

from amazondax.CborSExprGenerator import Func, FUNCS, OPERATORS, ACTIONS
def _find_function(i):
    for k, v in FUNCS.items():
        if v == i:
            return k

    for k, v in OPERATORS.items():
        if v == i:
            return k

    for k, v in ACTIONS.items():
        if v == i:
            return k

    return str(i)

def _format_sexp(expr):
    if isinstance(expr, list):
        e = '('
        if isinstance(expr[0], list):
            # Usual case for projection, update expr
            e += _format_sexp(expr[0])
        else:
            e += _find_function(expr[0])

        if len(expr) > 1:
            e += ' '

        if expr[0] != Func.In:
            e += ' '.join(_format_sexp(a) for a in expr[1:])
        else:
            # 'In' is a special case where in an array do not start with function code
            e += _format_sexp(expr[1]) + ' '
            e += '(' + ' '.join(_format_sexp(a) for a in expr[2]) + ')'
        e += ')'
    else:
        if isinstance(expr, DocumentPathOrdinal):
            e = '[{}]'.format(expr.ordinal)
        else:
            e = str(expr)

    return e

def _idfn(val):
    if isinstance(val, (bytes, bytearray)) and len(val):
        data = val if isinstance(val[0], int) else [ord(v) for v in val]
        ids = ' '.join('{:02x}'.format(d) for d in data)
        return ids if len(ids) < 15 else ids[:12] + '...'
    elif isinstance(val, Decimal):
        return str(val)

class _dummy_periodic_task(object):
    def __call__(self, func, period, jitter=None):
        self._func = func
        self.cancelled = False
        return self

    def step(self):
        self._func()

    def cancel(self):
        self.cancelled = True
        pass


