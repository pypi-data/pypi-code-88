from collections.abc import Mapping, Sequence
from functools import singledispatch, wraps
from json import dump as _dump, load
from typing import Any

__all__ = (
    'dump',
    'load',
    'convert',
)


@singledispatch
def convert(obj: Any):
    return obj


@convert.register
def convert_mapping(obj: Mapping):
    return {
        key: convert(value)
        for key, value in obj.items()
    }


@convert.register(str)
@convert.register(int)
@convert.register(float)
@convert.register(bool)
@convert.register(type(None))
def supported(obj):
    return obj


@convert.register
def convert_sequence(obj: Sequence):
    return [
        convert(value)
        for value in obj
    ]


@wraps(_dump)
def dump(
    obj,
    *args,
    ensure_ascii=False,
    allow_nan=False,
    sort_keys=True,
    **kwargs,
):
    obj = convert(obj)

    return _dump(
        obj,
        *args,
        ensure_ascii=ensure_ascii,
        allow_nan=allow_nan,
        sort_keys=sort_keys,
        **kwargs,
    )
