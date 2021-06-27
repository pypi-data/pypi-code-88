from typing import *

from . import EXPRESSION_STORAGE as ES
from . import VARIABLE_STORAGE as VS
from . import MagicGlobals as G
from .printer import *

__all__ = ["Scope"]


class Scope:
    def __init__(self, version: str, copy: Optional[str] = None):
        self.prev = G.cv
        self.version = version
        if version not in VS:
            new_version(version)
        if copy is not None:
            self.load(copy)

    @property
    def variables(self) -> Dict:
        return VS[self.version]

    @property
    def expressions(self) -> Dict:
        return ES[self.version]

    def load(self, other_version):
        duplicate(self.version, other_version)

    def __enter__(self):
        G.cv = self.version
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        G.cv = self.prev

    def __repr__(self) -> str:
        INDENT = G.repr_indent
        lines = []
        lines.append(f"Scope version: {self.version}")

        lines.append(" " * INDENT + "Variables:")

        for k, v in self.variables.items():
            lines.append(" " * INDENT * 2 + f"{latex_to_plain(k.name)} = {v}")
        lines.append(" " * INDENT + "Expressions:")
        for k, v in self.expressions.items():
            lines.append(" " * INDENT * 2 + f"{latex_to_plain(k)} = {v}")

        return "\n".join(lines)


def new_version(name: str):
    if name in VS:
        raise KeyError(f"Version name `{name}` already exists.")
    else:
        VS[name] = dict()
        ES[name] = dict()


def duplicate(new: str, old: str):
    VS[new] = {**VS[old]}
    ES[new] = dict()
