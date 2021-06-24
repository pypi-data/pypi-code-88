from __future__ import unicode_literals

from amazondax import Assemblers

from tests.Util import mktube

def test_defineKeySchema_hash():
    data = b'\x80\xa1ckeyaS'
    expected = [
        {'AttributeName': 'key', 'AttributeType': 'S'}
    ]

    tube = mktube(data)
    tube.skip() #  Throw away the empty error header
    result = Assemblers.defineKeySchema_N742646399_1(None, tube)

    assert result == expected

def test_defineKeySchema_hash_range():
    data = b'\x80\xa2dkey1aSdkey2aN'
    expected = [
        {'AttributeName': 'key1', 'AttributeType': 'S'},
        {'AttributeName': 'key2', 'AttributeType': 'N'}
    ]

    tube = mktube(data)
    tube.skip() #  Throw away the empty error header
    result = Assemblers.defineKeySchema_N742646399_1(None, tube)

    assert result == expected

def test_defineAttributeList():
    data = b'\x80\x82cfoocbar'
    expected = ['foo', 'bar']

    tube = mktube(data)
    tube.skip() #  Throw away the empty error header
    result = Assemblers.defineAttributeList_670678385_1(None, tube)

    assert result == expected

def test_defineAttributeListId():
    data = b'\x80\x02'
    expected = 2

    tube = mktube(data)
    tube.skip() #  Throw away the empty error header
    result = Assemblers.defineAttributeListId_N1230579644_1(None, tube)

    assert result == expected

def test_getItem():
    data = b'\x80\xa1\x00F\x02cfoo\x07'
    expected = {
        'Item': {
            '_attr_list_id': 2,
            '_anonymous_attribute_values': [{'S': 'foo'}, {'N': '7'}]
        }
    }

    request = {}

    tube = mktube(data)
    tube.skip() #  Throw away the empty error header
    result = Assemblers.getItem_263244906_1(request, tube)

    assert result == expected

