# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utility functions used for code generation."""
from typing import Any, Dict, List, Tuple, Type

import contextlib
import inspect
import sys


USE_SKLEARN_REPR = False


def indent_multiline_string(input_str: str, indent: int = 4) -> str:
    """
    Indent a multiline string to be used as a parameter value, except for the first line.

    :param input_str: The string to indent
    :return: The string with every line after the first being indented
    """
    lines = input_str.split("\n")
    if len(lines) == 1:
        return input_str

    new_lines = [lines[0]]
    for line in lines[1:]:
        new_lines.append(" " * indent + line)

    return "\n".join(new_lines)


def generate_repr_str(cls: "Type[Any]", params: Dict[str, Any], **kwargs: Any) -> str:
    """
    Generate an evaluatable string representation of this object.

    :param cls: The class of the object
    :param params: The parameters of the object (repr will be called on each value)
    :param kwargs: The parameters of the object (the value will be added as provided)
    :return: A string representation which can be executed to retrieve the same object
    """
    if len(params) == 0 and len(kwargs) == 0:
        return "{}()".format(cls.__name__)

    param_line = "    {}={}"

    assert set(kwargs.keys()).isdisjoint(set(params.keys()))

    init_params = [
        param_line.format(k, kwargs[k]) for k in kwargs
    ] + [
        param_line.format(k, override_repr(params[k], k)) for k in params
    ]

    init_params = [indent_multiline_string(line) for line in init_params]

    lines = [
        "{}(\n".format(cls.__name__),
        ",\n".join(init_params),
        "\n)"
    ]
    return "".join(lines)


def get_import(obj: Any) -> Tuple[str, str, Any]:
    """
    Get the information needed to import the class.

    :param obj: The object to get import information for
    :return: the module name, the class name, and the class object
    """
    # The provided object is already a callable
    if callable(obj):
        return obj.__module__, obj.__name__, obj

    # azureml.automl.runtime.shared.model_wrappers
    # LightGBMClassifier
    # LightGBMClassifier obj
    return obj.__class__.__module__, obj.__class__.__name__, obj.__class__


def generate_import_statements(imports: List[Tuple[str, str, Any]]) -> List[str]:
    return [
        "from {} import {}".format(x[0], x[1]) for x in imports
    ]


def _sklearn_repr(self: Any, N_CHAR_MAX: int = sys.maxsize) -> str:
    return generate_repr_str(self.__class__, self.get_params(deep=False))


def override_repr(obj: Any, key_name: str) -> str:
    """
    Generate an evaluatable string representation of this object, overriding __repr__() for sklearn BaseEstimators.

    :param obj: The object to generate a string for
    :param key_name: The parameter name for which this object is for
    :return: A string representation of the object
    """
    if "BaseEstimator.__repr__" in str(obj.__repr__):
        # This object uses sklearn's __repr__, we need to do magic because otherwise indentation will be messed up

        # We can either use sklearn's __repr__ with a higher character limit and then re-indent, or just use our own
        # implementation for __repr__ instead. If we use our own implementation, then indent will always be 4, else
        # we need to adjust based on the key name (key length + 1 for equal sign + 4 for tab stop)
        if USE_SKLEARN_REPR:
            obj_str = obj.__repr__(N_CHAR_MAX=sys.maxsize)
            indent = len(key_name) + 5
        else:
            indent = 0
            try:
                # Attempt to override BaseEstimator's __repr__ temporarily with our own implementation
                from sklearn.base import BaseEstimator
                old_repr = BaseEstimator.__repr__
                BaseEstimator.__repr__ = _sklearn_repr
                obj_str = repr(obj)
                BaseEstimator.__repr__ = old_repr
            except ImportError:
                obj_str = generate_repr_str(obj.__class__, obj.get_params(deep=False))

        return indent_multiline_string(obj_str, indent)
    elif obj.__class__.__name__ == "ndarray":
        # This object uses numpy ndarray, so just make sure indentation is correct.
        # Note that ndarrays are represented using numpy.array() in repr, so that must be imported instead of ndarray.
        return indent_multiline_string(repr(obj), len(key_name) + 1)

    # All other cases, no formatting should be needed
    return repr(obj)
