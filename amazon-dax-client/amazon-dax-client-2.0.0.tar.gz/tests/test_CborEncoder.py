# coding: utf-8
from __future__ import unicode_literals

from amazondax.CborEncoder import *
from amazondax.CborDecoder import CborDecoder

from tests.Util import _mkmore, _idfn

import pytest

from decimal import Decimal

# Taken from standard CBOR test vectors
TEST_INT = [
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
]
@pytest.mark.parametrize("expected,val", TEST_INT, ids=_idfn)
def test_encode_int(expected, val):
    enc = CborEncoder()

    result = enc.append_int(val).as_bytes()
    assert result == expected

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
@pytest.mark.parametrize("expected,val", TEST_FLOAT, ids=_idfn)
def test_encode_float(expected, val):
    enc = CborEncoder()

    result = enc.append_float(val).as_bytes()

    # Decode both results as floats to check results
    # We always use FLOAT_64 for Python
    expected_f = CborDecoder(_mkmore(expected)).decode_float()
    result_f = CborDecoder(_mkmore(result)).decode_float()

    assert result_f == expected_f

TEST_BOOL = [
    (b'\xf4', False),
    (b'\xf5', True),
]
@pytest.mark.parametrize("expected,val", TEST_BOOL, ids=_idfn)
def test_encode_bool(expected, val):
    enc = CborEncoder()

    result = enc.append_boolean(val).as_bytes()
    assert result == expected

def test_encode_null():
    enc = CborEncoder()

    expected = b'\xf6'
    result = enc.append_null().as_bytes()
    assert result == expected

def test_encode_break():
    enc = CborEncoder()

    expected = b'\xff'
    result = enc.append_break().as_bytes()
    assert result == expected

TEST_STRING = [
    (b'`', ''),
    (b'aa', 'a'),
    (b'dIETF', 'IETF'),
    (b'b"\\', '"\\'),
    (b'b\xc3\xbc', 'ü'),
    (b'c\xe6\xb0\xb4', '水'),
    (b'd\xf0\x90\x85\x91', '𐅑'),
]
@pytest.mark.parametrize("expected,val", TEST_STRING, ids=_idfn)
def test_encode_string(expected, val):
    enc = CborEncoder()

    result = enc.append_string(val).as_bytes()
    assert result == expected

TEST_DECIMAL = [
    (b'\xc4\x82\x00\x00', Decimal(0)),
    (b'\xc4\x82\x00\x01', Decimal(1)),
    (b'\xc4\x82\x00\x20', Decimal(-1)),
    (b'\xc4\x82\x21\x19\x6a\xb3', Decimal('273.15')),
    (b'\xc4\x82\x05\x02', Decimal('2e5')),
    (b'\xc4\x82\x24\x02', Decimal('2e-5')),
    (b"\xc4\x822\xc2O\x08\x97\x16T\xc4\xb6\x93\r\x94\xa4\x91|'\xd3\xe5", Decimal('4460278797255780.6064989229208294373')),
]
@pytest.mark.parametrize("expected,val", TEST_DECIMAL, ids=_idfn)
def test_encode_decimal(expected, val):
    enc = CborEncoder()

    result = enc.append_decimal(val).as_bytes()
    assert result == expected

def test_encode_decimal_wrong_type():
    enc = CborEncoder()
    with pytest.raises(TypeError):
        enc.append_decimal(None)

TEST_NUMBER_STRINGS = [
    (0, '0'),
    (Decimal('273.15'), '273.15'),
    (Decimal('2e-5'), '2e-5'),
]
@pytest.mark.parametrize("n,s", TEST_NUMBER_STRINGS, ids=_idfn)
def test_encode_number(n, s):
    enc = CborEncoder()

    expected = CborEncoder().append_number(n).as_bytes()
    result = enc.append_number(s).as_bytes()
    assert result == expected
