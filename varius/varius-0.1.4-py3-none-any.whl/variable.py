from typing import Any, Optional, Union

import sympy

from . import EXPRESSION_STORAGE as ES
from . import VARIABLE_STORAGE as VS
from . import MagicGlobals as G
from .printer import latex_to_plain

__all__ = ["Variable", "Expression"]


class Variable(sympy.Symbol):
    """An abstract variable that represents a numerical quantity."""

    def __new__(
        cls,
        name: str,
        value: Optional[Union[float, int]] = None,
        is_text: bool = True,
        **assumptions: Any,
    ):
        if is_text:
            name = r"\text{" + name + r"}"
        instance = super(Variable, cls).__new__(cls, name, **assumptions)

        if G.cv is not None and value is not None:
            VS[G.cv][instance] = value

        return instance

    @property
    def plain_name(self):
        return latex_to_plain(self.name)

    @property
    def value(self) -> Union[float, int]:
        if G.cv is not None:
            return self.__getitem__(G.cv)
        else:
            raise RuntimeError("Current version is `None`.")

    @value.setter
    def value(self, value: Union[float, int]):

        if G.cv is not None:
            self.__setitem__(G.cv, value)
        else:
            raise RuntimeError("Current version is `None`.")

    def __call__(self, value: Union[float, int]):
        self.value = value

    def __getitem__(self, version: str) -> Optional[Union[float, int]]:
        if version in VS:
            if self in VS[version]:
                return VS[version][self]
            else:
                return None
        else:
            raise KeyError(f"Version `{version}` does not exist.")

    def __setitem__(self, version: str, value: Union[float, int]):
        if not isinstance(value, (float, int)):
            raise TypeError(
                f"Assigned value should be float or int but get {type(value)}"
            )
        if version not in VS:
            VS[version] = dict()
            ES[version] = dict()

        VS[version][self] = value

    def __repr__(self) -> str:
        return self.plain_name

    __str__ = __repr__

    @property
    def latex_repr(self):
        try:
            v = self.value
            return sympy.latex(self) + f"= {v}"
        except KeyError:
            return sympy.latex(self)


def eval_expr(expr, version: str = G.cv):
    val = VS[version]
    return expr.subs(val)


class Expression:
    """Expression in symbolic variables."""

    def __init__(self, name: str, expr, is_text: bool = True):
        if is_text:
            name = r"\text{" + name + r"}"
        self.name = name
        self.expr = expr

    @property
    def plain_name(self):
        return latex_to_plain(self.name)

    @property
    def plain_expr(self):
        return latex_to_plain(r"{}".format(self.expr))

    def __call__(self, version: Optional[str] = None):
        if version is None:
            version = G.cv
        res = eval_expr(self.expr, version)
        ES[version][self.plain_name] = res

        return res

    @property
    def value(self):
        return self.__call__()

    def __repr__(self):
        return f"{self.plain_name} = {self.plain_expr}"

    __str__ = __repr__

    @property
    def latex_repr(self, evaluate: bool = True, version: Optional[str] = None):
        lhs = self.name
        rhs = sympy.latex(self.expr)
        eq = lhs + " = " + rhs
        if not evaluate:
            return eq
        res = sympy.latex(self.__call__(version))
        if res == rhs:
            return eq
        eq += " = " + res
        return eq
