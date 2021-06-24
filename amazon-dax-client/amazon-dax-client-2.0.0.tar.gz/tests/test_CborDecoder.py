# coding: utf-8

from __future__ import unicode_literals

from amazondax.CborDecoder import CborDecoder

from tests.Util import _mkmore, _idfn

import pytest

from decimal import Decimal

# Standard CBOR test vectors
STD_VECTORS = [
    (b'\x00', 0),
    (b'\x01', 1),
    (b'\n', 10),
    (b'\x17', 23),
    (b'\x18\x18', 24),
    (b'\x18\x19', 25),
    (b'\x18d', 100),
    (b'\x19\x03\xe8', 1000),
    (b'\x1a\x00\x0fB@', 1000000),
    (b'\x1b\x00\x00\x00\xe8\xd4\xa5\x10\x00', 1000000000000),
    (b'\x1b\xff\xff\xff\xff\xff\xff\xff\xff', 18446744073709551615),
    (b'\xc2I\x01\x00\x00\x00\x00\x00\x00\x00\x00', 18446744073709551616),
    (b';\xff\xff\xff\xff\xff\xff\xff\xff', -18446744073709551616),
    (b'\xc3I\x01\x00\x00\x00\x00\x00\x00\x00\x00', -18446744073709551617),
    (b' ', -1),
    (b')', -10),
    (b'8c', -100),
    (b'9\x03\xe7', -1000),
    (b'\xf9\x00\x00', 0.0),
    (b'\xf9\x80\x00', -0.0),
    (b'\xf9<\x00', 1.0),
    (b'\xfb?\xf1\x99\x99\x99\x99\x99\x9a', 1.1),
    (b'\xf9>\x00', 1.5),
    (b'\xf9{\xff', 65504.0),
    (b'\xfaG\xc3P\x00', 100000.0),
    (b'\xfa\x7f\x7f\xff\xff', 3.4028234663852886e+38),
    (b'\xfb~7\xe4<\x88\x00u\x9c', 1e+300),
    (b'\xf9\x00\x01', 5.960464477539063e-08),
    (b'\xf9\x04\x00', 6.103515625e-05),
    (b'\xf9\xc4\x00', -4.0),
    (b'\xfb\xc0\x10ffffff', -4.1),
    (b'\xf4', False),
    (b'\xf5', True),
    (b'\xf6', None),
    (b'`', ''),
    (b'aa', 'a'),
    (b'dIETF', 'IETF'),
    (b'b"\\', '"\\'),
    (b'b\xc3\xbc', 'ü'),
    (b'c\xe6\xb0\xb4', '水'),
    (b'd\xf0\x90\x85\x91', '𐅑'),
    (b'\x80', []),
    (b'\x83\x01\x02\x03', [1, 2, 3]),
    (b'\x83\x01\x82\x02\x03\x82\x04\x05', [1, [2, 3], [4, 5]]),
    (b'\x98\x19\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x18\x18\x19', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),
    (b'\xa0', {}),
    (b'\xa2aa\x01ab\x82\x02\x03', {'a': 1, 'b': [2, 3]}),
    (b'\x82aa\xa1abac', ['a', {'b': 'c'}]),
    (b'\xa5aaaAabaBacaCadaDaeaE', {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E'}),
    (b'\x7festreadming\xff', 'streaming'),
    (b'\x5fEstreaDming\xff', b'streaming'),
    (b'\x9f\xff', []),
    (b'\x9f\x01\x82\x02\x03\x9f\x04\x05\xff\xff', [1, [2, 3], [4, 5]]),
    (b'\x9f\x01\x82\x02\x03\x82\x04\x05\xff', [1, [2, 3], [4, 5]]),
    (b'\x83\x01\x82\x02\x03\x9f\x04\x05\xff', [1, [2, 3], [4, 5]]),
    (b'\x83\x01\x9f\x02\x03\xff\x82\x04\x05', [1, [2, 3], [4, 5]]),
    (b'\x9f\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x18\x18\x19\xff', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),
    (b'\xbfaa\x01ab\x9f\x02\x03\xff\xff', {'a': 1, 'b': [2, 3]}),
    (b'\x82aa\xbfabac\xff', ['a', {'b': 'c'}]),
    (b'\xbfcFun\xf5cAmt!\xff', {'Fun': True, 'Amt': -2}),
    (b'\xc4\x82\x00\x00', Decimal(0)),
    (b'\xc4\x82\x00\x01', Decimal(1)),
    (b'\xc4\x82\x00\x20', Decimal(-1)),
    (b'\xc4\x82\x21\x19\x6a\xb3', Decimal('273.15')), 
    (b'\xc4\x82\x05\x02', Decimal('2e5')),
    (b'\xc4\x82\x24\x02', Decimal('2e-5')),
    (b"\xc4\x822\xc2O\x08\x97\x16T\xc4\xb6\x93\r\x94\xa4\x91|'\xd3\xe5", Decimal('4460278797255780.6064989229208294373')),
]

@pytest.mark.parametrize("data,expected", STD_VECTORS, ids=_idfn)
def test_decode_std_vectors(data, expected):
    dec = CborDecoder(_mkmore(data))

    actual = dec.decode_object()
    assert actual == expected

TEST_NEGINT = [
    (b' ', -1),
    (b')', -10),
    (b'8c', -100),
    (b'9\x03\xe7', -1000),
    (b';\xff\xff\xff\xff\xff\xff\xff\xff', -18446744073709551616),
]
@pytest.mark.parametrize("data,expected", TEST_NEGINT, ids=_idfn)
def test_decode_negint(data, expected):
    dec = CborDecoder(_mkmore(data))

    actual = dec.decode_int()
    assert actual == expected

TEST_FLOAT = [
    (b'\xf9\x00\x00', 0.0),
    (b'\xf9\x80\x00', -0.0),
    (b'\xf9<\x00', 1.0),
    (b'\xfb?\xf1\x99\x99\x99\x99\x99\x9a', 1.1),
    (b'\xf9>\x00', 1.5),
    (b'\xf9{\xff', 65504.0),
    (b'\xfaG\xc3P\x00', 100000.0),
    (b'\xfa\x7f\x7f\xff\xff', 3.4028234663852886e+38),
    (b'\xfb~7\xe4<\x88\x00u\x9c', 1e+300),
    (b'\xf9\x00\x01', 5.960464477539063e-08),
    (b'\xf9\x04\x00', 6.103515625e-05),
    (b'\xf9\xc4\x00', -4.0),
    (b'\xfb\xc0\x10ffffff', -4.1),
]
@pytest.mark.parametrize("data,expected", TEST_FLOAT, ids=_idfn)
def test_decode_float(data, expected):
    dec = CborDecoder(_mkmore(data))

    actual = dec.decode_float()
    assert actual == expected

TEST_BIGINT = [
    (b'\xc2I\x01\x00\x00\x00\x00\x00\x00\x00\x00', 18446744073709551616),
    (b'\xc3I\x01\x00\x00\x00\x00\x00\x00\x00\x00', -18446744073709551617),
]
@pytest.mark.parametrize("data,expected", TEST_BIGINT, ids=_idfn)
def test_decode_bigint(data, expected):
    dec = CborDecoder(_mkmore(data))

    actual = dec.decode_int()
    assert actual == expected

TEST_DECIMAL = [
    (b'\xc4\x82\x00\x00', Decimal(0)),
    (b'\xc4\x82\x00\x01', Decimal(1)),
    (b'\xc4\x82\x00\x20', Decimal(-1)),
    (b'\xc4\x82\x21\x19\x6a\xb3', Decimal('273.15')), 
    (b'\xc4\x82\x05\x02', Decimal('2e5')),
    (b'\xc4\x82\x24\x02', Decimal('2e-5')),
    (b"\xc4\x822\xc2O\x08\x97\x16T\xc4\xb6\x93\r\x94\xa4\x91|'\xd3\xe5", Decimal('4460278797255780.6064989229208294373')),
]
@pytest.mark.parametrize("data,expected", TEST_DECIMAL, ids=_idfn)
def test_decode_decimal(data, expected):
    dec = CborDecoder(_mkmore(data))

    actual = dec.decode_decimal()
    assert actual == expected

def test_decode_map_iter_fixed():
    data, expected = (b'\xa2aa\x01ab\x82\x02\x03', {'a': 1, 'b': [2, 3]})

    dec = CborDecoder(_mkmore(data))

    result = {}
    for _dec in dec.decode_map_iter():
        key = _dec.decode_object()
        value = _dec.decode_object()
        print(key, value)
        result[key] = value

    assert result == expected

def test_decode_map_iter_stream():
    data, expected = (b'\xbfaa\x01ab\x9f\x02\x03\xff\xff', {'a': 1, 'b': [2, 3]})

    dec = CborDecoder(_mkmore(data))

    result = {}
    for _dec in dec.decode_map_iter():
        key = _dec.decode_object()
        value = _dec.decode_object()
        print(key, value)
        result[key] = value

    assert result == expected

def test_decode_array_iter_fixed():
    data, expected = (b'\x83\x01\x82\x02\x03\x82\x04\x05', [1, [2, 3], [4, 5]])

    dec = CborDecoder(_mkmore(data))

    result = []
    for _dec in dec.decode_array_iter():
        value = _dec.decode_object()
        result.append(value)

    assert result == expected

def test_decode_array_iter_stream():
    data, expected = (b'\x9f\x01\x82\x02\x03\x9f\x04\x05\xff\xff', [1, [2, 3], [4, 5]])

    dec = CborDecoder(_mkmore(data))

    result = []
    for _dec in dec.decode_array_iter():
        value = _dec.decode_object()
        result.append(value)

    assert result == expected

def test_decode_cbor():
    data, expected = (b'I\xa2aa\x01ab\x82\x02\x03', {'a': 1, 'b': [2, 3]})
    
    dec = CborDecoder(_mkmore(data))
    _dec = dec.decode_cbor()
    result = _dec.decode_map()

    assert result == expected

