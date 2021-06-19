from abc import ABC
from functools import partial, wraps

from attr import define as _define, resolve_types


class Attr(ABC):
    pass


@wraps(_define)
def define(maybe_cls=None, **kwargs):
    if maybe_cls is None:
        return partial(define, **kwargs)
    else:
        cls = resolve_types(_define(maybe_cls, **kwargs))
        Attr.register(cls)
        return cls
