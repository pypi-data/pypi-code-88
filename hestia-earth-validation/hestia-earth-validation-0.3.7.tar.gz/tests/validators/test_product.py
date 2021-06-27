import json

from tests.utils import fixtures_path
from hestia_earth.validation.validators.product import validate_economicValueShare, validate_value


def test_validate_economicValueShare_valid():
    # no products should be valid
    assert validate_economicValueShare([])

    with open(f"{fixtures_path}/product/economicValueShare/valid.json") as f:
        data = json.load(f)
    assert validate_economicValueShare(data.get('nodes')) is True


def test_validate_economicValueShare_invalid():
    with open(f"{fixtures_path}/product/economicValueShare/invalid.json") as f:
        data = json.load(f)
    assert validate_economicValueShare(data.get('nodes')) == {
        'level': 'error',
        'dataPath': '.products',
        'message': 'economicValueShare should sum to 100 or less across all products',
        'params': {
            'sum': 110
        }
    }


def test_validate_value_valid():
    # no products should be valid
    assert validate_value([])

    with open(f"{fixtures_path}/product/value/valid.json") as f:
        data = json.load(f)
    assert validate_value(data.get('nodes')) is True


def test_validate_value_warning():
    with open(f"{fixtures_path}/product/value/warning.json") as f:
        data = json.load(f)
    assert validate_value(data.get('nodes')) == {
        'level': 'warning',
        'dataPath': '.products[1].value',
        'message': 'may not be 0'
    }
