from decimal import Decimal
from typing import (
    Sequence,
    Mapping,
    Any,
    Callable
)


def deserialize(data: Any, recursive: bool = False) -> Any:
    """
    For objects that are `almost` a duck, but not quite
    This keeps json decoder from blowing up. Suitable for use
    as `default` keyword arg to json.dumps if `recursive` is set
    to False. An example of an almost duck is UserDict, which will
    behave like a dict in almost every way, but json.dumps doesn't know
    what to do with.
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

    # If recursive is set to True and we are running as the default decoder
    # for json.dumps then we will cause an error due to recursion by returning the
    # original response. But if we are running standalone then this is suitable so
    # that we don't return None for values that don't need to be decoded.
    elif recursive:
        res = data

    return res


def deserialize_recursive(data: Any) -> Any:
    return deserialize(data, reccursive=True)