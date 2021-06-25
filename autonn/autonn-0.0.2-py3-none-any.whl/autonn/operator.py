from __future__ import annotations

import abc
import collections
import copy
import functools
import inspect
import itertools
import types
import typing
import warnings

import dill

from .fields import Descriptor, HyperParameter, OperatorField, Parameter
from bayes_optim.search_space import SearchSpace

__authors__ = ["Jacob de Nobel", "Hao Wang"]


def rsetattr(obj, attr, val):
    """Set attributes recursively in the depth-first manner"""
    pre, _, post = attr.rpartition(".")
    return setattr(rgetattr(obj, pre) if pre else obj, post, val)


def rgetattr(obj, attr, *args, return_parent=False):
    def _getattr(obj, attr):
        if return_parent and not getattr(obj, attr, None):
            return obj
        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split("."))


class OperatorMeta(abc.ABCMeta):
    """Metaclass to control the creation of Operator instances.
    This class binds any descriptor objects found on the class body
    to a inspect.Signature object, in the same order as they were defined
    on the class body. This allows a class which takes this class
    as metaclass to bind a function to this Signature.

    Notes
    -----
    Suggested usage is to bind this to an __init__ function in the child class.
    """

    def __new__(
        cls: typing.Any, name: str, bases: typing.Tuple[type], namespace: dict
    ) -> typing.Any:
        """Controls the creation of a class of type ``cls``

        The calling signature of ``__init__`` is created by inspecting
        all ``OperatorField``-typed attributes

        Parameters
        ----------
        cls: object
            An instance of the metaclass
        name: str
            The name of the class to be created
        bases: typing.Tuple[type]
            A tuple of bases for the class to be created
        namespace: dict
            A namespace for the class to be created

        Returns
        -------
        The class to be created
        """
        obj = super().__new__(cls, name, bases, namespace)
        __signature__ = inspect.Signature(
            [
                inspect.Parameter(
                    name=name,
                    default=des.default_value,
                    kind=inspect.Parameter.POSITIONAL_OR_KEYWORD,
                )
                for name, des in obj._get_descriptors()
            ]
        )
        setattr(obj, "__signature__", __signature__)
        return obj


# TODO: Update documentation for positional arguments
class AbstractOperator(abc.ABC, metaclass=OperatorMeta):

    """Abstract class for all operators objects

    Notes
    -----
    Hereinafter, we refer to all preprocessing, machine learning, and validation
    modules as "operators" since those can be abstracted as parameterized
    operators of data sets. It is designed to subclass **configurable** modules
    in a way that:
        * all hyper-parameters should be declared using descriptors of type
          ``HyperParameter``, or its subtypes,
        * ordinary (public) parameters exposed to the user but excluded from
          the automated configuration should be declared using descriptors of type
          ``Parameter``, or its subtypes,
        * all remaining attributes required by the user can be defined
          in the usual way (on the spot or in the constructor),
          as either protected or private attributes.
    When declaring the (hyper-)parameters, you are allowed to create them without
    default values, which will become positional arguments of the constructor `__init__`
    (ones with default values become keyword arguments). Note that, the declaration of
    positional ones must come before any keyword ones, similarly to the argument ordering
    in `__init__`.

    By its design, we regulate the ``__init__`` function of its subclasses as follows:
    ```python
    > class MyOp(AbstractOperator):
    >   param = Parameter()              # without default values
    >   hyper_param1 = HyperParameter()  # without default values
    >   hyper_param2 = HyperParameter(default_value = 42)
    >
    >   def __init__(
    >       42,                          # assignment to positional argument
    >       hyper_param1 = 2333,         # by keywords
    >       hyper_param2 = 10            # change the default value
    >       ...
    >   ):
    >       # MUST pass the arguments to the parent, either manually or using tricks
    >       AbstractOperator.__init__(**locals())
    >       # all other customized procedures starts from here
    >       ...
    >
    >   def fit(self):                   # this method MUST be implemented
    >       pass
    ```

    The typical working flow of its subclasses is as follows:
    ```python
    > op = MyOp()
    > op.set_logger('log').set_random_seed(42)
    > op.logger = 'log'                  # ...equivalently
    > params = op.get_hyper_params()     # get hyper-parameters
    > ...                                # suppose param is modified
    > op.set_params(params)              # set hyper-parameters
    > cs = op.config_space               # get the current configuration space
    > cs.pop(1)                          # remove the first subspace/hyper-parameter
    > op.config_space = cs               # modify the configuration space
    > print(op.get_params())             # other non-hyper-parameters
    ```
    """

    def __init__(self, *args, **kwargs):
        """Initializer auotmatically sets all parameters
        defined in ``self.__signature__``
        """
        # NOTE: this should be deprecated in the future..
        kwargs = {k: v for k, v in kwargs.items() if k in self.__signature__.parameters.keys()}
        self.__bound__ = self.__signature__.bind(*args, **kwargs)
        self.__bound__.apply_defaults()

        # assign the arguments to descriptors
        for name, value in self.__bound__.arguments.items():
            setattr(self, name, value)

        # TODO: ad-hoc solution to make `self.save` work
        # since some values in `_signature` are not serializable
        self.__arguments__ = copy.deepcopy(self.__bound__.arguments)

        # Force call of set name
        for name, des in self._get_descriptors():
            des.__set_name__(self, name)

        self._disabled_vars: set = set()
        self._default_config_space: SearchSpace = self.config_space
        self._check_hyper_params()

    def _check_input_params(self, params: dict) -> dict:
        invalid_keys = set(params.keys()) - set(self._get_field_values().keys())
        if bool(invalid_keys):
            warnings.warn(f"Unkown parameters: {invalid_keys}!")

        invalid_keys |= self._disabled_vars & set(params.keys())
        for k in invalid_keys:
            del params[k]

        return params

    def _check_hyper_params(self):
        # check if the new value of some var. triggers the condition of other variables,
        # which are rendered invalid and thereby their values should be reset.
        # NOTE: `replace('.', '_')` is necessary to evaluate the string
        # `self._default_config_space` is necesary here since even if some hyperparameters
        # are removed from the configuration space, its value can still be affected by
        # its conditions
        env = {k.replace(".", "_"): v for k, v in self.get_hyper_params().items()}
        for var in self._default_config_space.data:
            if var.conditions is not None:
                if eval(var.conditions.replace(".", "_"), env):
                    pre, _, post = var.name.rpartition(".")
                    obj = rgetattr(self, pre) if pre else self
                    getattr(obj.__class__, post).act_on_conditions(obj)

    @classmethod
    def _get_descriptors(cls, dtype: Descriptor = OperatorField) -> typing.List[Descriptor]:
        """Finds all descriptors of type dtype on a cls body.

        Parameters
        ----------
        dtype: Descriptor
            The type of descriptors to find on the class

        Returns
        -------
        A list of descriptors, in the order they were defined on the class body
        """
        descriptors = filter(
            lambda x: isinstance(getattr(cls, x[0], None), dtype), inspect.getmembers(cls)
        )
        mro_members = list(
            itertools.chain(*map(lambda obj: obj.__dict__.keys(), reversed(inspect.getmro(cls))))
        )
        # Shift positional only parameters before parameters with defaults
        return sorted(
            descriptors,
            key=lambda x: mro_members.index(x[0])
            - (len(mro_members) * (x[1].default_value == inspect.Parameter.empty)),
        )

    def _get_hyper_param_names(self):
        return tuple(self._get_field_values(HyperParameter).keys())

    def _get_field_values(
        self, dtype: OperatorField = OperatorField, attr: str = None
    ) -> collections.OrderedDict:
        """Gets all the values for all descriptor Fields.

        Parameters
        ----------
        dtype: OperatorField
            The type of descriptor for which to fetch their values, by default
            OperatorField, which fectch all ``OperatorField`` instances.
        attr: str
            (Optional) The name of the descriptor attribute to fetch

        Returns
        -------
        An Ordered of key-value pairs for all decriptors of type ``dtype``
        """
        if not isinstance(dtype, OperatorField) and not issubclass(dtype, OperatorField):
            raise TypeError("dtype must be of type or subclass of OperatorField")

        out: collections.OrderedDict = collections.OrderedDict()
        for key, des in self._get_descriptors():
            value = des.get(self, attr)
            _recursion = getattr(getattr(self, key), "_get_field_values", None)
            if _recursion:
                out.update((f"{key}.{k}", v) for k, v in _recursion(dtype, attr).items())
            if isinstance(des, dtype) or (attr is not None and value is not None):
                out[key] = value
            # TODO: do we want to include the operator also?
        return out

    def get_variables(self, dtype: HyperParameter = HyperParameter) -> dict:
        return self._get_field_values(dtype, "variable")

    def get_params(self) -> dict:
        return self._get_field_values(Parameter)

    def get_hyper_params(self) -> dict:
        return self._get_field_values(HyperParameter)

    def set_params(self, params: dict) -> AbstractOperator:
        for key, value in self._check_input_params(params).items():
            rsetattr(self, key, value)

        self._check_hyper_params()
        return self

    def get_default_config_space(self) -> SearchSpace:
        return copy.deepcopy(self._default_config_space)

    @property
    def config_space(self):
        variables = []
        for k, v in self.get_variables().items():
            if k in self._disabled_vars:
                continue
            variable = copy.deepcopy(v)
            variable.name = k
            variables.append(variable)
        return SearchSpace(variables)

    @config_space.setter
    def config_space(self, cs: typing.Union[SearchSpace, dict]):
        """The user is supposed to only modified the range of hyperparameters
        in ``self._default_config_space``. Adding new hyperparameter or changing
        the type of existing ones are not allowed.

        Parameters
        ----------
        cs : typing.Union[SearchSpace, dict]
            The new search space instance
        """
        if isinstance(cs, dict):
            cs = SearchSpace.from_dict(cs)

        curr_vars = self.get_variables()
        self._disabled_vars = set(self._default_config_space.var_name)

        for var in cs.data:
            _var = curr_vars.get(var.name)
            if not _var:
                warnings.warn(f"Unkown hyper-parameter: {var.name} given to config_space")
                continue

            if not isinstance(var, type(_var)):
                raise TypeError(
                    f"{var.name} is not of the correct type. "
                    f"Got {type(var)}, expected: {type(_var)}"
                )
            self._disabled_vars.discard(var.name)
            _var.__dict__.update(**copy.deepcopy(var.__dict__))

    @classmethod
    def load(cls, filename: str):
        with open(filename + ".dump", "rb") as f:
            kwargs = dill.load(f)
        # some non-default field values are needed to create the class
        obj = cls(**kwargs["__arguments__"])
        # restore the parameter and hyper-parameter values
        obj.set_params(kwargs["field_values"])
        # restore user's attributes
        obj.__dict__.update(kwargs)
        return obj

    def save(self, filename: str, exclude: typing.List[str]):
        """Dump the operator to a file, excluding member vars `data_train` and
        `data_val` by default

        Parameters
        ----------
        filename : str
            The dump file name
        """
        # `__bound__` might contain iterators and we only need `__bound__.arguments`
        field_values = {k: v for k, v in self._get_field_values().items() if k not in exclude}
        exclude += ["_" + k for k in field_values.keys()] + ["__bound__"]
        field_values = dict(
            filter(lambda e: not isinstance(e[1], types.GeneratorType), field_values.items())
        )
        with open(filename + ".dump", "wb") as f:
            __dict__ = {k: v for k, v in self.__dict__.items() if k not in set(exclude)}
            __dict__.update({"field_values": field_values})
            dill.dump(__dict__, f)

    def __repr__(self):
        # TODO: add more printout here
        return self.__class__.__name__

    def __str__(self):
        return self.__repr__()
