from decimal import Decimal
from typing import (
    Sequence,
    Mapping,
    Any,
    Callable
)


def deserialize(data: Any, recursive=False) -> Any:
    """
    For objects that are `almost` a duck, but not quite
    This keeps json decoder from blowing up
    """
    res = None
    if isinstance(data, Mapping) and not isinstance(data, dict):
        if recursive:
            res = deserialize(dict(data), recursive=recursive)
        else:
            res = dict(data)
    elif isinstance(data, Sequence) and not isinstance(data, str):
        if recursive:
            res = []
            for x in data:
                res.append(deserialize(x, recursive=recursive))
        else:
            res = list(data)
    elif isinstance(data, dict):
        if recursive:
            res = {}
            for k, v in data.items():
                res[k] = deserialize(v, recursive=recursive)
        else:
            res = data
    elif isinstance(data, Callable):
        res = str(data)
    elif isinstance(data, Decimal):
        res = float(data)

    return res


def deserialize_recursive(data: Any) -> Any:
    return deserialize(data, reccursive=True)