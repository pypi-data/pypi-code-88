from amazondax import AttributeValueDecoder
from amazondax.CborDecoder import CborDecoder
from amazondax.DocumentPath import DocumentPath

import pytest
pytestmark = pytest.mark.perf

import sys; sys.path.append('tests')  # Relative to root directory
from Util import mktestkeys, av, _mkmore

def test_deanonymize_attribute_values(benchmark):
    item = {
        '_attr_list_id': 1,
        '_anonymous_attribute_values': [{'N': '1'}, {'S': 'foo'}]
    }
    attr_names = ['key', 'value']

    benchmark(lambda: AttributeValueDecoder.deanonymize_attribute_values(item.copy(), attr_names))

from test_AttributeValueDecoder import TEST_AV
@pytest.mark.parametrize('data,_', TEST_AV)
def test_decode_attribute_value_perf(benchmark, data, _):
    benchmark(lambda: AttributeValueDecoder._decode_attribute_value(CborDecoder(_mkmore(data))))

# TODO Combine all of the below into one group for comparison
def test_decode_stream_item(benchmark):
    data = b'\x02jRon Howard\xc4\x82 \x18K'
        
    benchmark(lambda: AttributeValueDecoder._decode_stream_item(CborDecoder(_mkmore(data))))

def test_decode_projection_perf(benchmark):
    data = b'\xbf\x00jRon Howard\x01\xc4\x82 \x18K\xff'
    proj_ordinals = [
        DocumentPath(['info', 'directors', 0]), 
        DocumentPath(['info', 'rating'])
    ]

    benchmark(lambda: AttributeValueDecoder._decode_projection(CborDecoder(_mkmore(data)), proj_ordinals))

@pytest.mark.skip(reason="Not implemented")
def test_scan_result_perf(benchmark):
    pass

