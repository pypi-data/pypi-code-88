from amazondax.CborSExprGenerator import encode_condition_expression, encode_projection_expression, encode_update_expression

import pytest
pytestmark = pytest.mark.perf

import sys; sys.path.append('tests')  # Relative to root directory

from test_CborSExprGenerator import TEST_CONDITION
@pytest.mark.parametrize('data,_', TEST_CONDITION)
def test_condition_expression_perf(benchmark, data, _):
    benchmark(lambda: encode_condition_expression(*data))

from test_CborSExprGenerator import TEST_PROJECTION
@pytest.mark.parametrize('data,_', TEST_PROJECTION)
def test_projection_expression_perf(benchmark, data, _):
    benchmark(lambda: encode_projection_expression(*data))

from test_CborSExprGenerator import TEST_UPDATE
@pytest.mark.parametrize('data,_', TEST_UPDATE)
def test_update_expression_perf(benchmark, data, _):
    benchmark(lambda: encode_update_expression(*data))

