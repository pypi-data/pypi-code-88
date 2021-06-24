from amazondax import AttributeValueEncoder
from amazondax.CborDecoder import CborDecoder

import pytest
pytestmark = pytest.mark.perf

import sys; sys.path.append('tests')  # Relative to root directory
from Util import mktestkeys, av, _mkmore

TEST_KEYS = mktestkeys(('S', 'N', 'B'), ((16, 16), (128, 128), (512, 512), (2048, 1024)))
@pytest.mark.parametrize('item, schema', TEST_KEYS)
def test_encode_key_perf(benchmark, item, schema):
    if len(schema) == 2 and schema[1]['AttributeType'] == 'N':
        pytest.xfail('LexDecimal is not supported')
    benchmark(AttributeValueEncoder.encode_key, item, schema)

from test_AttributeValueEncoder import TEST_AV
@pytest.mark.parametrize('_,av', TEST_AV)
def test_encode_attribute_value_perf(benchmark, _, av):
    benchmark(lambda: AttributeValueEncoder.encode_attribute_value(av))

