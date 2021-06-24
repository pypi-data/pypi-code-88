from __future__ import unicode_literals

import decimal

from amazondax import AttributeValueDecoder
from amazondax.DaxCborDecoder import DaxCborDecoder
from amazondax.DocumentPath import DocumentPath

from tests.Util import av, _mkmore, _idfn

import pytest

def _mkschema(schema):
    return [{'AttributeType': t, 'AttributeName': n} for t, n in zip(schema, ("hash", "range"))]

def test_deanonymize_attribute_values():
    item = {
        '_attr_list_id': 1,
        '_anonymous_attribute_values': [{'N': '1'}, {'S': 'foo'}]
    }
    attr_names = ['key', 'value']

    expected = {
        'key': {'N': '1'},
        'value': {'S': 'foo'},
    }

    result = AttributeValueDecoder.deanonymize_attribute_values(item, attr_names)

    assert result is item # Check that item is modified in place
    assert result == expected

def test_deanonymize_attribute_values_map():
    item = {
        '_attr_list_id': 1,
        '_anonymous_attribute_values': {0: {'N': '1'}, 1: {'S': 'foo'}}
    }
    attr_names = ['key', 'value']

    expected = {
        'key': {'N': '1'},
        'value': {'S': 'foo'},
    }

    result = AttributeValueDecoder.deanonymize_attribute_values(item, attr_names)

    assert result is item # Check that item is modified in place
    assert result == expected

def test_deanonymize_attribute_values_map_subset():
    item = {
        '_attr_list_id': 1,
        '_anonymous_attribute_values': {0: {'N': '1'}, 1: {'S': 'foo'}}
    }
    attr_names = ['key', 'value', 'data']

    expected = {
        'key': {'N': '1'},
        'value': {'S': 'foo'},
    }

    result = AttributeValueDecoder.deanonymize_attribute_values(item, attr_names)

    assert result is item # Check that item is modified in place
    assert result == expected

def test_reinsert_key():
    request = {'Key': {'year': av(1995), 'title': av('Apollo 13')}}
    item = {'item': av({})}

    expected = {
        'year': av(1995),
        'title': av('Apollo 13'),
        'item': av({})
    }

    AttributeValueDecoder._reinsert_key(item, request)
    assert item == expected

def test_reinsert_key_projection():
    request = {
        'Key': {'year': av(1995), 'title': av('Apollo 13')},
        '_projection_ordinals': []
    }
    item = {'item': av({})}

    expected = {
        'item': av({})
    }

    AttributeValueDecoder._reinsert_key(item, request)
    assert item == expected

TEST_AV = [
    pytest.param(b'\x00', av(0), id='posint'),
    pytest.param(b' ', av(-1), id='negint'),
    pytest.param(b'\xc2I\x01\x00\x00\x00\x00\x00\x00\x00\x00', av(18446744073709551616), id='posbigint'),
    pytest.param(b'\xc3I\x01\x00\x00\x00\x00\x00\x00\x00\x00', av(-18446744073709551617), id='posnegint'),
    pytest.param(b'\xf4', av(False), id='false'),
    pytest.param(b'\xf5', av(True), id='true'),
    pytest.param(b'\xf6', av(None), id='null'),
    pytest.param(b'aa', av('a'), id='utf8'),
    pytest.param(b'Aa', av(b'a'), id='bytes'),
    pytest.param(b'\x83\x01\x02\x03', av([1, 2, 3]), id='array'),
    pytest.param(b'\xa2aa\x01ab\x82\x02\x03', av({'a': 1, 'b': [2, 3]}), id='map'),
    pytest.param(b'\xd9\x0c\xf9\x83aaabac', av({'a', 'b', 'c'}), id='stringset'),
    pytest.param(b'\xd9\x0c\xfa\x83\x01\x02\x03', av({1, 2, 3}), id='numberset'),
    pytest.param(b'\xd9\x0c\xfb\x83AaAbAc', av({b'a', b'b', b'c'}), id='binaryset'),
]
@pytest.mark.parametrize("data,expected", TEST_AV)
def test_decode_attribute_value(data, expected):
    dec = DaxCborDecoder(_mkmore(data))

    result = AttributeValueDecoder._decode_attribute_value(dec)
    assert result == expected

TEST_KEY_BYTES = [
    ("S", b'Cfoo', ("foo",)),
    ("N", b'B\x18*', (42,)),
    ("B", b'Cbar', (b'bar',)),
    ("SS", b'Gcfoobaz', ("foo", "baz")),
    ("NS", b'E\x18*foo', (42, "foo")),
    ("BS", b'GCbarfoo', (b'bar', "foo")),
    ("SN", b'Hcfoo\xc2l\x00\x10', ("foo", 42)),
    ("SB", b'Gcfoobar', ("foo", b'bar')),
]
@pytest.mark.parametrize("schema,data,expected", TEST_KEY_BYTES, ids=_idfn)
def test_decode_key_bytes(schema, data, expected):
    key_schema = [{'AttributeType': t, 'AttributeName': n} for t, n in zip(schema, ("hash", "range"))]
    expected = {k: av(v) for v, k in zip(expected, ("hash", "range"))}

    dec = DaxCborDecoder(_mkmore(data))
    result = AttributeValueDecoder._decode_key_bytes(dec, key_schema)

    assert result == expected

def test_decode_compound_key():
    data = b'\xa2dhashcfooerange\x18*'
    expected = {
        "hash": {"S": "foo"},
        "range": {"N": "42"}
    }

    dec = DaxCborDecoder(_mkmore(data))
    result = AttributeValueDecoder._decode_compound_key(dec)

    assert result == expected

def test_decode_anonymous_streamed_values():
    data = b' aaAa'
    expected = [av(-1), av('a'), av(b'a')]

    dec = DaxCborDecoder(_mkmore(data))

    result = AttributeValueDecoder._decode_anonymous_streamed_values(dec)

    assert result == expected

def test_decode_stream_item():
    data = b'\x02jRon Howard\xc4\x82 \x18K'
    expected = {
        '_attr_list_id': 2,
        '_anonymous_attribute_values': [av("Ron Howard"), {"N": "7.5"}],
    }

    dec = DaxCborDecoder(_mkmore(data))
    result = AttributeValueDecoder._decode_stream_item(dec)

    assert result == expected

def test_decode_item_internal_anon_av():
    data = b'Q\x02jRon Howard\xc4\x82 \x18K'
    request = {'Key': {'year': av(1995), 'title': av('Apollo 13')}}
    expected = {
        'year': av(1995),
        'title': av('Apollo 13'),
        '_attr_list_id': 2,
        '_anonymous_attribute_values': [av("Ron Howard"), {"N": "7.5"}],
    }

    dec = DaxCborDecoder(_mkmore(data))
    result = AttributeValueDecoder._decode_item_internal(dec, request)

    assert result == expected

def test_decode_item_internal_projection():
    data = b'\xbf\x00jRon Howard\x01\xc4\x82 \x18K\xff'
    request = {
        'Key': {'year': av(1995), 'title': av('Apollo 13')},
        'ProjectionExpression': 'info.directors[0], info.rating',
        '_projection_ordinals': [
            DocumentPath(['info', 'directors', 0]),
            DocumentPath(['info', 'rating'])
        ]
    }
    expected = {
        'info': av({
            'directors': ["Ron Howard"],
            'rating': decimal.Decimal("7.5")
        })
    }

    dec = DaxCborDecoder(_mkmore(data))
    result = AttributeValueDecoder._decode_item_internal(dec, request)

    assert result == expected

def test_decode_item_internal_scan_result():
    data = b'\x82L\x19\x07\xcbApollo 13Q\x02jRon Howard\xc4\x82 \x18K'

    class Request(dict):
        def __init__(self):
            self.key_schema = [
                {'AttributeType': 'N', 'AttributeName': 'year'},
                {'AttributeType': 'S', 'AttributeName': 'title'},
            ]
            self['TableName'] = 'Movies'

    expected = {
        'year': av(1995),
        'title': av('Apollo 13'),
        '_attr_list_id': 2,
        '_anonymous_attribute_values': [av("Ron Howard"), {"N": "7.5"}]
    }

    dec = DaxCborDecoder(_mkmore(data))
    result = AttributeValueDecoder._decode_item_internal(dec, Request())

    assert result == expected

def test_decode_item_internal_null():
    data = b'\xf6'
    dec = DaxCborDecoder(_mkmore(data))

    result = AttributeValueDecoder._decode_item_internal(dec, {})
    assert result is None
