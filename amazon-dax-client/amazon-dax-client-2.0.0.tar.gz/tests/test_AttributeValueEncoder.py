from __future__ import unicode_literals

from amazondax import AttributeValueEncoder
from amazondax.DocumentPath import DocumentPath
from amazondax.DaxClient import Request

import pytest
import six

from collections import OrderedDict

from tests.Util import av

TYPES = {
    six.text_type: 'S',
    bytes: 'B',
    int: 'N'
}

if six.PY2:
    TYPES[long] = 'N'

def combo(h, r_e, e=None):
    if e is None:
        item, schema, expected = mkitem(h), mkschema(h), r_e
    else:
        item, schema, expected = mkitem(h, r_e), mkschema(h, r_e), e

    _id = ''.join(key['AttributeType'] for key in schema)
    return pytest.param(item, schema, expected, id=_id)

def mkitem(h, r=None):
    result = {'hash': {TYPES[type(h)]: h}}
    if r is not None:
        result['range'] = {TYPES[type(r)]: r}

    return result

def mkschema(h, r=None):
    result = [
        {'AttributeName': 'hash', 'AttributeType': TYPES[type(h)]}
    ]

    if r is not None:
        result.append({'AttributeName': 'range', 'AttributeType': TYPES[type(r)]})

    return result

KEY_COMBOS = [
    # HASH S
    combo('foo', b'foo'),
    
    # HASH S, RANGE S
    combo('foo', b'foo'),
    
    # HASH S, RANGE B
    combo('foo', 'bar', b'cfoobar'),

    # HASH S, RANGE N
    combo('foo', 25, b'cfoo\xc2\x41\x80\x10'),
    combo('foo', 1034, b'cfoo\xc4\x1c\xd9\xc0\x00'),
    combo('foo', 2**16 + 1034, b'cfoo\xc5\xa9\x6c\x80\x04'),
    combo('foo', 2**32 + 1034, b'cfoo\xca\x6e\x5f\xcd\x34\x0c\x00\x00'),

    # HASH B
    combo(b'foo', b'foo'),

    # HASH B, RANGE S
    combo(b'foo', 'bar', b'Cfoobar'),

    # HASH B, RANGE B
    combo(b'foo', b'bar', b'Cfoobar'),

    # HASH B, RANGE N
    combo(b'foo', 25, b'Cfoo\xc2\x41\x80\x10'),

    # HASH N
    combo(7, b'\x07'),
    combo(25, b'\x18\x19'),
    combo(1034, b'\x19\x04\x0a'),
    combo(2**16 + 1034, b'\x1a\x00\x01\x04\x0a'),
    combo(2**32 + 1034, b'\x1b\x00\x00\x00\x01\x00\x00\x04\x0a'),

    # HASH N, RANGE S tests
    combo(7, 'foo', b'\x07foo'),
    # HASH N, RANGE B tests
    combo(7, b'bar', b'\x07bar'),
    # HASH N, RANGE N tests
    combo(7, 1034, b'\x07\xc4\x1c\xd9\xc0\x00'),
    combo(25, 1034, b'\x18\x19\xc4\x1c\xd9\xc0\x00'),
]

@pytest.mark.parametrize('item, schema, expected', KEY_COMBOS)
def test_encode_key(item, schema, expected):
    result = AttributeValueEncoder.encode_key(item, schema)

    assert result == expected

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
@pytest.mark.parametrize('expected,av', TEST_AV)
def test_encode_attribute_value(expected, av):
    result = AttributeValueEncoder.encode_attribute_value(av)
    assert result == expected

def test_encode_expressions():
    request = Request({
        'ConditionExpression': '#a < :b', 
        # TODO Add KeyConditionExpression when fixed
        'FilterExpression': 'b <= c',
        'UpdateExpression': 'SET a = a - :b',
        'ProjectionExpression': 'a.b.#c, #d',
        'ExpressionAttributeNames': {'#a': 'c', '#c': 'g', '#d': 'e.f'},
        'ExpressionAttributeValues': {':b': av(5)}
    })

    expected = b'\x04M\x83\x01\x83\x02\x82\x12ac\x82\x11\x00\x81\x05' + \
            b'\x0aM\x83\x01\x83\x05\x82\x12ab\x82\x12ac\x80' + \
            b'\x08U\x83\x01\x81\x83\x13\x82\x12aa\x83\x18\x1a\x82\x12aa\x82\x11\x00\x81\x05' + \
            b'\x00Q\x82\x01\x82\x84\x12aaabag\x82\x12ce.f' + \
            b'\x01\xa3b#aacb#cagb#dce.f' + \
            b'\x05\xa1b:b\x05'
    expected_proj_ords = [
        DocumentPath(['a', 'b', 'g']), 
        DocumentPath(['e.f'])
    ]

    result = AttributeValueEncoder.encode_expressions(request)
    assert request['_projection_ordinals'] == expected_proj_ords
    assert result == expected

def test_encode_compound_key():
    key = {
        "hash": {"S": "foo"},
        "range": {"N": "42"}
    }
    key = OrderedDict(sorted(key.items()))

    expected = b'\xbfdhashcfooerange\x18*\xff'

    result = AttributeValueEncoder.encode_compound_key(key)
    assert result == expected

def test_get_canonical_attribute_list():
    schema = [
        {'AttributeName': 'pk', 'KeyType': 'HASH'},
        {'AttributeName': 'sk', 'KeyType': 'RANGE'}
    ]

    item = {
        'pk': {'N': '123'},
        'pk': {'N': '425'},
        'someData': {'S': 'FOO'},
        'moreData': {'S': 'BAR'},
    }

    # The response must be a string type, in sorted order
    expected = (u'moreData', u'someData')

    result = AttributeValueEncoder._get_canonical_attribute_list(item, schema)

    assert result == expected

