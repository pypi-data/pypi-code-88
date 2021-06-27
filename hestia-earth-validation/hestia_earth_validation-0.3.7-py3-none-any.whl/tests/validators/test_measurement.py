import json

from tests.utils import fixtures_path
from hestia_earth.validation.validators.measurement import (
    validate_soilTexture, validate_depths, validate_value_min_max, validate_term_unique
)


def test_validate_soilTexture_invalid():
    # 90% on same depthUpper / depthLower
    with open(f"{fixtures_path}/measurement/soilTexture/low-value.json") as f:
        data = json.load(f)
    assert validate_soilTexture(data.get('nodes')) == {
        'level': 'error',
        'dataPath': '.measurements',
        'message': 'sum not equal to 100% for sandContent, siltContent, clayContent'
    }

    # remove all depthUpper / depthLower
    with open(f"{fixtures_path}/measurement/soilTexture/no-depth-high-value.json") as f:
        data = json.load(f)
    assert validate_soilTexture(data.get('nodes')) == {
        'level': 'error',
        'dataPath': '.measurements',
        'message': 'sum not equal to 100% for sandContent, siltContent, clayContent'
    }

    # invalid percent
    with open(f"{fixtures_path}/measurement/soilTexture/percent-invalid.json") as f:
        data = json.load(f)
    assert validate_soilTexture(data.get('nodes')) == {
        'level': 'error',
        'dataPath': '.measurements',
        'message': 'is outside the allowed range',
        'params': {
            'term': {'@id': 'sandContent', '@type': 'Term'},
            'range': {'min': 86, 'max': 100}
        }
    }


def test_validate_soilTexture_valid():
    # no measurements should be valid
    assert validate_soilTexture([]) is True

    # missing element same depthUpper / depthLower
    with open(f"{fixtures_path}/measurement/soilTexture/missing-soil.json") as f:
        data = json.load(f)
    assert validate_soilTexture(data.get('nodes')) is True

    # simple no depth
    with open(f"{fixtures_path}/measurement/soilTexture/no-depth-valid.json") as f:
        data = json.load(f)
    assert validate_soilTexture(data.get('nodes')) is True

    # missing at least 1 value
    with open(f"{fixtures_path}/measurement/soilTexture/missing-values.json") as f:
        data = json.load(f)
    assert validate_soilTexture(data.get('nodes')) is True

    # valid percent
    with open(f"{fixtures_path}/measurement/soilTexture/percent-valid.json") as f:
        data = json.load(f)
    assert validate_soilTexture(data.get('nodes')) is True

    # missing value - cannot validate
    with open(f"{fixtures_path}/measurement/soilTexture/percent-missing-value.json") as f:
        data = json.load(f)
    assert validate_soilTexture(data.get('nodes')) is True


def test_validate_depths_valid():
    # no measurements should be valid
    assert validate_depths([]) is True

    with open(f"{fixtures_path}/measurement/depths/valid.json") as f:
        data = json.load(f)
    assert validate_depths(data.get('nodes')) is True


def test_validate_depths_invalid():
    with open(f"{fixtures_path}/measurement/depths/invalid.json") as f:
        data = json.load(f)
    assert validate_depths(data.get('nodes')) == {
        'level': 'error',
        'dataPath': '.measurements[2].depthLower',
        'message': 'must be greater than depthUpper'
    }


def test_validate_measurement_value_valid():
    # no measurements should be valid
    assert validate_value_min_max([]) is True

    with open(f"{fixtures_path}/measurement/min-max/value-valid.json") as f:
        data = json.load(f)
    assert validate_value_min_max(data.get('nodes')) is True


def test_validate_measurement_value_invalid():
    with open(f"{fixtures_path}/measurement/min-max/value-above.json") as f:
        data = json.load(f)
    assert validate_value_min_max(data.get('nodes')) == {
        'level': 'error',
        'dataPath': '.measurements[0].value',
        'message': 'should be below 25000.0'
    }

    with open(f"{fixtures_path}/measurement/min-max/value-below.json") as f:
        data = json.load(f)
    assert validate_value_min_max(data.get('nodes')) == {
        'level': 'error',
        'dataPath': '.measurements[0].value',
        'message': 'should be above 0.0'
    }


def test_validate_term_unique_valid():
    # no measurements should be valid
    assert validate_term_unique([]) is True

    with open(f"{fixtures_path}/measurement/unique/valid.json") as f:
        data = json.load(f)
    assert validate_term_unique(data.get('nodes')) is True


def test_validate_term_unique_invalid():
    with open(f"{fixtures_path}/measurement/unique/invalid.json") as f:
        data = json.load(f)
    assert validate_term_unique(data.get('nodes')) == [{
        'level': 'error',
        'dataPath': '.measurements[0].term.name',
        'message': 'must be unique'
    }, {
        'level': 'error',
        'dataPath': '.measurements[1].term.name',
        'message': 'must be unique'
    }]
