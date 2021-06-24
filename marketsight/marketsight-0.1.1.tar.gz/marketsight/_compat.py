"""
######################
marketsight._compat
######################

This module handles import compatibility issues between Python 2 and Python 3.
"""
# pylint: disable=invalid-name,redefined-builtin,no-member,missing-docstring,unused-import,undefined-variable,used-before-assignment

import math
import sys
from decimal import Decimal

import chardet

_ver = sys.version_info

#: Python 2.x?
is_py2 = _ver[0] == 2

#: Python 3.x?
is_py3 = _ver[0] == 3

try:
    import simplejson as json
except ImportError:
    import json

# ---------
# Specifics
# ---------

if is_py2:
    from StringIO import StringIO  # pylint: disable=import-error
    from urllib3.packages.ordered_dict import (
        OrderedDict,
    )  # pylint: disable=import-error,E0611
    import urllib as base_urllib

    builtin_str = str
    bytes = str
    str = unicode
    basestring = basestring
    numeric_types = (int, long, float, Decimal)
    integer_types = (int, long)
    long = long
    xrange = xrange
    INFINITY = float("+inf")
    NEGATIVE_INFINITY = float("-inf")


elif is_py3:
    from io import StringIO
    from collections import OrderedDict
    import urllib.parse as base_urllib

    builtin_str = str
    str = str
    bytes = bytes
    basestring = (str, bytes)
    numeric_types = (int, float, Decimal)
    integer_types = (int,)
    long = int
    xrange = range
    INFINITY = math.inf
    NEGATIVE_INFINITY = -math.inf


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class metaclass(type):
        # pylint: disable=unused-argument

        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)

        @classmethod
        def __prepare__(cls, name, this_bases):
            return meta.__prepare__(name, bases)

    return type.__new__(metaclass, "temporary_class", (), {})


def add_metaclass(metaclass):
    """Class decorator for creating a class with a metaclass."""

    def wrapper(cls):
        orig_vars = cls.__dict__.copy()
        slots = orig_vars.get("__slots__")
        if slots is not None:
            if isinstance(slots, str):
                slots = [slots]
            for slots_var in slots:
                orig_vars.pop(slots_var)
        orig_vars.pop("__dict__", None)
        orig_vars.pop("__weakref__", None)

        return metaclass(cls.__name__, cls.__bases__, orig_vars)

    return wrapper
