from typing import Dict, Optional

from . import EXPRESSION_STORAGE as ES
from . import VARIABLE_STORAGE as VS
from . import MagicGlobals as G
from .printer import latex_to_plain

__all__ = ["Scope"]


class Scope:
    "Scope: alias `note`"

    def __init__(self, version: str = "default", copy: Optional[str] = None):
        self.prev = G.cv
        self.version = version
        if version not in VS:
            new_version(version)
        if copy is not None:
            self.load(copy)

    @property
    def variables(self) -> Dict:
        return {latex_to_plain(k.name): v for k, v in VS[self.version].items()}

    @property
    def expressions(self) -> Dict:
        return {latex_to_plain(k): v for k, v in ES[self.version].items()}

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
            lines.append(" " * INDENT * 2 + f"{k} = {v}")
        lines.append(" " * INDENT + "Expressions:")
        for k, v in self.expressions.items():
            lines.append(" " * INDENT * 2 + f"{k} = {v}")

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
