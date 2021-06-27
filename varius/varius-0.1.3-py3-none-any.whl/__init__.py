from typing import Any, Dict

VARIABLE_STORAGE: Dict[str, Dict[str, float]] = {"default": dict()}
EXPRESSION_STORAGE: Dict[str, Dict[str, float]] = {"default": dict()}


class MagicGlobals:
    latex: bool = True  # use latex
    cv: str = "default"  # current version
    repr_indent: int = 2


def reset_version(version: str):
    if version not in VARIABLE_STORAGE:
        raise KeyError(f"The version `{version}` does not exist.")
    VARIABLE_STORAGE[version] = dict()
    EXPRESSION_STORAGE[version] = dict()
    if MagicGlobals.cv == version:
        MagicGlobals.cv == "default"


def reset_all():
    VARIABLE_STORAGE.clear()
    EXPRESSION_STORAGE.clear()
    VARIABLE_STORAGE["default"] = dict()
    EXPRESSION_STORAGE["default"] = dict()
    MagicGlobals.cv == "default"


from .printer import *
from .scope import Scope as note
from .variable import Expression, Variable


def set_latex(use: bool = True):
    MagicGlobals.latex = use
    if use:
        latex_use_cdot()


set_latex(use=is_ipython())


vr = Variable
ex = Expression

__all__ = ["note", "vr", "ex", "show"]

__version__ = "0.1.3"
