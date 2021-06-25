import copy
import inspect
import typing

from bayes_optim import search_space
from bayes_optim.search_space import Variable


class Descriptor:
    """Base descriptor"""

    __slots__ = ("name", "private_name")

    def __set_name__(self, instance, name):
        self.name = name
        self.private_name = f"_{name}"

    def __get__(self, instance, instance_type=None):
        return getattr(instance, self.private_name, self)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)

    def __delete__(self, instance):
        if hasattr(instance, self.private_name):
            delattr(instance, self.private_name)


# TODO: this class should be abstract
class OperatorField(Descriptor):
    """A field of ``AbstractOperator`` class"""

    __slots__ = ("default_value",)

    def __init__(self, default_value=inspect.Parameter.empty):
        self.default_value = default_value

    def __set__(self, instance, value):
        # cutomized `__set__` declared in the class containing this field
        if f"set_{self.name}" in dir(instance):
            getattr(instance, f"set_{self.name}")(value)
        else:
            super().__set__(instance, value)

    def get(self, instance, attribute: str = None):
        """get the value of the field or its attribute"""
        value = self.__get__(instance)
        if attribute:
            value = getattr(self, attribute, None) or getattr(
                instance, f"{self.private_name}_{attribute}", None
            )
        return value

    def set(self, instance, value, attribute: str = None):
        """set the value of the field or its attribute"""
        if attribute:
            setattr(instance, f"{self.private_name}_{attribute}", value)
        else:
            super().__set__(instance, value)


# TODO: to discuss whether we need constraint the types of admissible value
class Parameter(OperatorField):
    """Ordinary parameter which should not be configured"""


# TODO: maybe we should also check if the value is in its range
# TODO: this class should be abstract
class HyperParameter(OperatorField):
    """A hyper-parameter field presenting in the ``AbstractOperator`` class"""

    _var_cls: Variable = Variable

    def __init__(
        self,
        bounds: typing.Tuple = (),
        default_value: typing.Union[int, float, str] = None,
        **kwargs,
    ):
        super().__init__(default_value if default_value is not None else inspect.Parameter.empty)
        # the search variable pertaining to this hyper-parameter
        self._default_variable: Variable = self._var_cls(
            bounds=bounds, name="foo", default_value=default_value, **kwargs
        )

    def __set_name__(self, instance, name):
        super().__set_name__(instance, name)
        variable = copy.deepcopy(self._default_variable)
        variable.name = name  # update the variable's name
        setattr(instance, f"{self.private_name}_variable", variable)

    def act_on_conditions(self, instance):
        var = getattr(instance, f"{self.private_name}_variable")
        func = var.action
        if func:
            self.__set__(instance, func(self.__get__(instance)))


class RealHyperParameter(HyperParameter):
    _var_cls = search_space.Real


class IntegerHyperParameter(HyperParameter):
    _var_cls = search_space.Integer


class OrdinalHyperParameter(HyperParameter):
    _var_cls = search_space.Ordinal


class DiscreteHyperParameter(HyperParameter):
    _var_cls = search_space.Discrete


class BoolHyperParameter(HyperParameter):
    _var_cls = search_space.Bool

    def __init__(self, default_value: bool = False):
        super().__init__(default_value=default_value)
