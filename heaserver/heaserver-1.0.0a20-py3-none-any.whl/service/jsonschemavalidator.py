from jsonschema.validators import validator_for as _validator_for
from jsonschema import validate, ValidationError


def compile(schema: dict):
    return _validator_for(schema)(schema)
