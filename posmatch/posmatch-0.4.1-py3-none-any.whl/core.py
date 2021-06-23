"""
Enable positional sub-pattern matching for objects of a custom class by
setting the `__match_args__` class attribute.

This module provides the following functions and classes:

  pos_match       -    class decorator setting the `__match_args__`
                       attribute
  PosMatchMeta    -    metaclass setting the `__match_args__` attribute
"""

import inspect


def pos_match(cls=None, /, *, force=False):
    """Decorator setting the `__match_args__` class attribute.

    `__match_args__` will contain a sequence of names equal to
    parameter names in the signature of `cls.__init__` (not including
    `self`).

    If `cls` already has the `__match_args__` attribute (inherited or
    defined on its own) it will not be set, unless `force` is set to
    True.
    """
    if cls:
        # @pos_match usage
        if not hasattr(cls, '__match_args__'):
            _set_match_args(cls)
        return cls

    if force:
        # @pos_match(force=True) or equivalent usage
        return _set_match_args

    # @pos_match(), @pos_match(force=False) or equivalent usage
    return pos_match


def _set_match_args(cls):
    init_params = inspect.signature(cls.__init__).parameters
    param_names = tuple(init_params.keys())

    # exclude the first parameter (self)
    setattr(cls, '__match_args__', param_names[1:])
    return cls


class PosMatchMeta(type):
    """Metaclass setting the `__match_args__` class attribute."""

    def __new__(mcs, name, bases, dct):
        cls = super().__new__(mcs, name, bases, dct)
        if not hasattr(cls, '__match_args__'):
            _set_match_args(cls)
        return cls
