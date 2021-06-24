import pytest

from amazondax.RequestValidator import RequestValidator
from amazondax.DaxError import DaxValidationError


def test_validate_item():
    # for empty binary set
    assert_validation_error({':updateVal': {'BS': []}})
    # for empty string set
    assert_validation_error({':updateVal': {'SS': []}})
    # for null string in SS
    assert_validation_error({':updateVal': {'SS': ['abc', None]}})
    # for empty number set
    assert_validation_error({':updateVal': {'NS': []}})

    # for empty string
    assert_no_error({':updateVal': {'S': ''}})
    # for empty binary
    assert_no_error({':updateVal': {'B': bytes()}})


def assert_validation_error(attr_value):
    with pytest.raises(DaxValidationError, match='One or more parameter values were invalid'):
        RequestValidator.validate_expr_attr_values(attr_value)


def assert_no_error(attr_value):
    try:
        RequestValidator.validate_expr_attr_values(attr_value)
    except DaxValidationError as e:
        pytest.fail('Unexpected error: {}'.format(e))
