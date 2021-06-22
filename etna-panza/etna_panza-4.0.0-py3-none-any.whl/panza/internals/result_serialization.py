"""
Module dealing with serialization / deserialization of job results
"""

import json
from typing import Any, Dict, IO

from quixote.inspection import Scope

from panza.errors import ResultLoadingError


def _scope_as_dict(scope):
    if isinstance(scope, Scope):
        return {
            "__type__": "Scope",
            "name": scope.name,
            "hidden": scope.hidden,
            "entries": [_scope_as_dict(e) for e in scope.entries],
        }
    return scope


class _ResultJSONEncoder(json.JSONEncoder):
    """
    JSON encoder (for the json module) used to serialize a job result
    """

    def default(self, o):
        if isinstance(o, Scope):
            return _scope_as_dict(scope=o)
        return o


def _result_json_object_hook(o: Dict):
    """
    JSON object hook (for the json module) used to deserialize a job result
    """
    if o.get("__type__") == "Scope":
        return Scope(name=o["name"], entries=o["entries"], hidden=o["hidden"])
    return o


def deserialize_result(fp: IO):
    """
    Deserialize a Quixote result from an IO
    """
    return json.load(fp, object_hook=_result_json_object_hook)


def serialize_result(data, fp: IO):
    """
    Serialize a Quixote result to an IO
    """
    json.dump(data, fp, indent=4, cls=_ResultJSONEncoder)


def load_result(path: str) -> Dict[str, Any]:
    """
    Load a Quixote result from a file
    """
    try:
        with open(path, 'r') as result_file:
            return deserialize_result(result_file)
    except (json.JSONDecodeError, OSError) as e:
        raise ResultLoadingError(e)
