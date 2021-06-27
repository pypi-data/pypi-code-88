import json

from tests.utils import fixtures_path
from hestia_earth.validation.validators.input import validate_must_include_id


def test_validate_must_include_id_valid():
    # no inputs should be valid
    assert validate_must_include_id([]) is True

    with open(f"{fixtures_path}/input/mustIncludeId/valid.json") as f:
        data = json.load(f)
    assert validate_must_include_id(data.get('nodes')) is True

    with open(f"{fixtures_path}/input/mustIncludeId/valid-multiple-ids.json") as f:
        data = json.load(f)
    assert validate_must_include_id(data.get('nodes')) is True


def test_validate_must_include_id_invalid():
    with open(f"{fixtures_path}/input/mustIncludeId/invalid.json") as f:
        data = json.load(f)
    assert validate_must_include_id(data.get('nodes')) == {
        'level': 'error',
        'dataPath': '.inputs[0]',
        'message': 'should add missing inputs: potassiumNitrateAsK2O'
    }
