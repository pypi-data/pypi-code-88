from amazondax.DynamoDbV1Converter import convert_request

import pytest
pytestmark = pytest.mark.perf

import sys; sys.path.append('tests')  # Relative to root directory

from test_DynamoDbV1Converter import TEST_V1V2
@pytest.mark.parametrize("ddb_request, method_id, _", TEST_V1V2)
def test_convert_request_perf(benchmark, ddb_request, method_id, _):
    benchmark(lambda: convert_request(ddb_request, method_id))

