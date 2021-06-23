from pysolaar.utils.exceptions import PySolaarException
from .camel_to_snake import camelToSnake

"""
How to encode fields for Solr:
"""


"""
{
    "pysolaar_type": cls.__name__,
    "id": f"{cls.__name__}{ID_SEPARATOR}{id_string}",
    "{cls.__name__}": ["values"],
    "doc_": [
        {
            "pysolaar_type": f"{parentcls.__name__}{ID_SEPARATOR}{cls.__name__}",
        },
    ],
}
"""


class PySolaarEncodingError(PySolaarException):
    pass


ID_SEPARATOR = "##########"
KEY_SEPARATOR = "______"


def encode_field_name(pysolaar_type, key):
    """Encodes a field name by prefixing with a pysolaar_type, separated by KEY_SEPARATOR,
    which is by default six underscores.

    Inserting the key into a string should be sufficient to catch any errors; as it's prefixed
    by the name of a Python class, that should be sufficient to make it valid as a Solr field name."""
    try:
        return f"{pysolaar_type}{KEY_SEPARATOR}{key}"
    except:
        raise PySolaarEncodingError(
            f"Could not encode field name {key}. This is probably because it is not a string."
        )


def decode_field_name(encoded_field_name):
    try:
        return encoded_field_name.split(KEY_SEPARATOR)[-1]
    except:
        return None


def encode_id(pysolaar_type, id):
    return f"{pysolaar_type}{ID_SEPARATOR}{id}"


def decode_id(id):
    return id.split(ID_SEPARATOR)[-1]


def encode_pysolaar_type(pysolaar_type):
    pass