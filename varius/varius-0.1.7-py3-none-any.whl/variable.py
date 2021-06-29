from typing import Any, Dict, List, Optional, Union

import sympy

from . import EXPRESSION_STORAGE as ES
from . import VARIABLE_STORAGE as VS
from . import MagicGlobals as G
from .printer import latex_to_plain

__all__ = ["Variable", "Expression"]


class Variable(sympy.Symbol):
    """An abstract variable that represents a numerical quantity."""

    _registry: Dict = dict()

    @classmethod
    def list(cls) -> List:
        return list(cls._registry.keys())

    @classmethod
    def list_items(cls) -> List:
        return list(cls._registry.values())

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
            VS[G.cv][instance] = sympy.Float(value, G.float_digit)

        cls._registry[instance.plain_name] = instance

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

        VS[version][self] = sympy.Float(value, G.float_digit)

    def __repr__(self) -> str:
        return self.plain_name

    __str__ = __repr__

    @property
    def latex_repr(self):
        try:
            v = sympy.latex(self.value)
            return sympy.latex(self) + f"= {v}"
        except KeyError:
            return sympy.latex(self)


def eval_expr(expr, version: str = G.cv):
    val = VS[version]
    return sympy.Float(expr.subs(val), G.float_digit)


class Expression:
    """Expression in symbolic variables."""

    _registry: Dict = dict()

    @classmethod
    def list(cls) -> List:
        return list(cls._registry.keys())

    @classmethod
    def list_items(cls) -> List:
        return list(cls._registry.values())

    def __init__(self, name: str, expr, is_text: bool = True):
        if is_text:
            name = r"\text{" + name + r"}"
        self.name = name
        self.expr = expr

        self._registry[self.plain_name] = self

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

    def grad(
        self, *args: Variable, evaluate: bool = True, version: Optional[str] = None
    ) -> Dict:
        if len(args) > 0:
            grads = {x: Gradient(self, x) for x in args}
        else:
            grads = {x: Gradient(self, x) for x in Variable._registry.values()}

        if evaluate:
            grads = {v: g(version) for v, g in grads.items()}

        return grads

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


class Gradient(Expression):
    def __init__(self, expression: Expression, variable: Variable):
        assert isinstance(
            expression, (Expression, Variable, sympy.Symbol)
        ), f"The type of expression `{type(expression)}` should be `Expression`."
        assert isinstance(
            variable, (Variable, sympy.Symbol)
        ), f"The type of variable `{type(variable)}` should be `Variable`."
        name = (
            r"\partial \left["
            + expression.name
            + r"\right] / \partial \left["
            + variable.name
            + r"\right]"
        )
        expr = expression.expr.diff(variable)
        super().__init__(name, expr, is_text=False)
