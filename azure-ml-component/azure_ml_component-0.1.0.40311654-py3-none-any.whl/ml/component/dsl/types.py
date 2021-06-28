# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""This file includes the type annotations which could be used in dsl.pipeline.

.. remarks::
    This is a preview feature.
    The following pseudo-code shows how to create a pipeline with such annotations.

    .. code-block:: python

        @dsl.pipeline()
        def some_pipeline(
            int_param: Integer(min=0),
            str_param: String() = 'abc',
        ):
            pass

"""

import math

from typing import Optional, Union, Sequence, Iterable
from enum import EnumMeta
from ._component._exceptions import DSLComponentDefiningError
from ._utils import logger


class Input:
    """Define an input of a component."""

    def __init__(self, type='path', description=None, optional=False):
        """Define an input definition for a component."""
        # As an annotation, it is not allowed to initialize the name.
        # The name will be updated by the annotated variable name.
        self._name = None
        self._type = type
        self._description = description
        self._optional = optional

    @property
    def name(self) -> str:
        """Return the name of the input."""
        return self._name

    @property
    def type(self) -> str:
        """Return the type of the input."""
        return self._type

    @property
    def description(self) -> str:
        """Return the description of the input."""
        return self._description

    @property
    def optional(self) -> bool:
        """Return whether the input is optional."""
        return self._optional

    def _to_dict(self, remove_name=True):
        """Convert the Input object to a dict."""
        keys = ['name', 'type', 'description', 'optional']
        if remove_name:
            keys.remove('name')
        result = {key: getattr(self, key) for key in keys}
        return _remove_empty_values(result)

    def _to_python_code(self):
        """Return the representation of this parameter in annotation code, used in code generation."""
        parameters = []
        if self._type is not None and self._type != 'path':
            parameters.append('type={!r}'.format(self._type))
        if self._description is not None:
            parameters.append('description={!r}'.format(self._description))
        if self._optional is not None:
            parameters.append('optional={}'.format(self._optional))
        return "{type_name}({parameters})".format(
            type_name=self.__class__.__name__, parameters=', '.join(parameters))


class Path(Input):
    """Define an input path of a component."""

    def __init__(self, description=None, optional=False):
        """Define an input path for a component."""
        super().__init__(type='path', description=description, optional=optional)


class Output:
    """Define an output of a component."""

    def __init__(self, type='path', description=None):
        """Define an output of a component."""
        # As an annotation, it is not allowed to initialize the name.
        # The name will be updated by the annotated variable name.
        self._name = None
        self._type = type
        self._description = description

    @property
    def name(self) -> str:
        """Return the name of the output."""
        return self._name

    @property
    def type(self) -> str:
        """Return the type of the output."""
        return self._type

    @property
    def description(self) -> str:
        """Return the description of the output."""
        return self._description

    def _to_dict(self, remove_name=True):
        """Convert the Output object to a dict."""
        keys = ['name', 'type', 'description']
        if remove_name:
            keys.remove('name')
        result = {key: getattr(self, key) for key in keys}
        return _remove_empty_values(result)

    def _to_python_code(self):
        """Return the representation of this parameter in annotation code, used in code generation."""
        parameters = []
        if self._type is not None and self._type != 'path':
            parameters.append('type={!r}'.format(self._type))
        if self._description is not None:
            parameters.append('description={!r}'.format(self._description))
        return "{type_name}({parameters})".format(
            type_name=self.__class__.__name__, parameters=', '.join(parameters))


class _Param:
    """This is the base class of component parameters.

    The properties including name/type/default/options/optional/min/max will be dumped in component spec.
    When invoking a component, param.parse_and_validate(str_val) is called to parse the command line value.
    """

    DATA_TYPE = None  # This field is the corresponding python type of the class, e.g. str/int/float.
    TYPE_NAME = None  # This field is the type name of the parameter, e.g. string/integer/float.

    def __init__(
        self, name=None, description=None, default=None, enum=None, optional=False, min=None, max=None,
    ):
        """Define a parameter of a component."""
        self._name = name
        self._type = self.TYPE_NAME
        self._description = description
        self._default = default
        self._enum = enum
        self._optional = optional
        self._min = min
        self._max = max
        self._allowed_types = ()
        # TODO: Maybe a parameter could have several allowed types? For example, json -> List/Dict?
        if self.DATA_TYPE:
            self._allowed_types = (self.DATA_TYPE,)
        self._update_default(default)

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> Optional[str]:
        return self._type

    @property
    def description(self) -> Optional[str]:
        return self._description

    @property
    def optional(self) -> bool:
        """Return whether the parameter is optional."""
        return self._optional

    @property
    def default(self) -> Optional[Union[str, int, float]]:
        """Return the default value of the parameter."""
        return self._default

    @property
    def enum(self) -> Optional[Sequence[str]]:
        """Return the enum values of the parameter for an enum parameter."""
        return self._enum

    @property
    def max(self) -> Optional[Union[int, float]]:
        """Return the maximum value of the parameter for a numeric parameter."""
        return self._max

    @property
    def min(self) -> Optional[Union[int, float]]:
        """Return the minimum value of the parameter for a numeric parameter."""
        return self._min

    def _to_dict(self, remove_name=True) -> dict:
        """Convert the Param object to a dict."""
        keys = ['name', 'type', 'description', 'min', 'max', 'enum', 'default', 'optional']
        if remove_name:
            keys.remove('name')
        result = {key: getattr(self, key) for key in keys}
        return _remove_empty_values(result)

    def _parse(self, str_val: str):
        """Parse str value passed from command line.

        :param str_val: The input string value from the command line.
        :return: The parsed value.
        """
        return str_val

    def _parse_and_validate(self, str_val):
        """Parse the str_val passed from the command line and validate the value.

        :param str_val: The input string value from the command line.
        :return: The parsed value, an exception will be raised if the value is invalid.
        """
        str_val = self._parse(str_val) if isinstance(str_val, str) else str_val
        self._validate_or_throw(str_val)
        return str_val

    def _update_name(self, name):
        self._name = name

    def _update_default(self, default_value):
        """Update provided default values.

        Here we need to make sure the type of default value is allowed or it could be parsed..
        """
        if default_value is not None and not isinstance(default_value, self._allowed_types):
            try:
                default_value = self._parse(default_value)
            except Exception as e:
                if self.name is None:
                    msg = "Default value of %s cannot be parsed, got '%s', type = %s." % (
                        type(self).__name__, default_value, type(default_value)
                    )
                else:
                    msg = "Default value of %s '%s' cannot be parsed, got '%s', type = %s." % (
                        type(self).__name__, self.name, default_value, type(default_value)
                    )
                raise DSLComponentDefiningError(cause=msg) from e
        self._default = default_value

    def _validate_or_throw(self, value):
        """Validate input parameter value, throw exception if not as expected.

        It will throw exception if validate failed, otherwise do nothing.
        """
        if not self.optional and value is None:
            raise ValueError("Parameter %s cannot be None since it is not optional." % self.name)
        if self._allowed_types and value is not None:
            if not isinstance(value, self._allowed_types):
                raise TypeError(
                    "Unexpected data type for parameter '%s'. Expected %s but got %s." % (
                        self.name, self._allowed_types, type(value)
                    )
                )

    def _to_python_code(self):
        """Return the representation of this parameter in annotation code, used in code generation."""
        parameters = []
        if self._default is not None:
            parameters.append('default={!r}'.format(self._default))
        if self._optional:
            parameters.append('optional={}'.format(self._optional))
        if self._description is not None:
            parameters.append('description={!r}'.format(self._description))
        if self._min is not None:
            parameters.append('min={}'.format(self._min))
        if self._max is not None:
            parameters.append('max={}'.format(self._max))

        return "{type_name}({parameters})".format(
            type_name=self.__class__.__name__, parameters=', '.join(parameters))


class String(_Param):
    """String parameter passed the parameter string with its raw value."""

    DATA_TYPE = str
    TYPE_NAME = 'string'

    def __init__(
        self,
        description=None,
        optional=False,
        default=None,
    ):
        """Initialize a string parameter."""
        _Param.__init__(
            self,
            description=description,
            optional=optional,
            default=default,
        )


class _Numeric(_Param):
    """Numeric Parameter is an intermediate type which is used to validate the value according to min/max."""

    def _validate_or_throw(self, val):
        super()._validate_or_throw(val)
        if self._min is not None and val < self._min:
            raise ValueError("Parameter '%s' should not be less than %s." % (self.name, self._min))
        if self._max is not None and val > self._max:
            raise ValueError("Parameter '%s' should not be greater than %s." % (self.name, self._max))


class Integer(_Numeric):
    """Int Parameter parse the value to a int value."""

    DATA_TYPE = int
    TYPE_NAME = 'integer'

    def __init__(
        self,
        min=None,
        max=None,
        description=None,
        optional=False,
        default=None,
    ):
        """Initialize an integer parameter."""
        _Numeric.__init__(
            self,
            optional=optional,
            description=description,
            default=default,
            min=min,
            max=max,
        )

    def _parse(self, val) -> int:
        """Parse the integer value from a string value."""
        return int(val)


class Float(_Numeric):
    """Float Parameter parse the value to a float value."""

    DATA_TYPE = float
    TYPE_NAME = 'float'

    def __init__(
        self,
        min=None,
        max=None,
        description=None,
        optional=False,
        default=None,
    ):
        """Initialize a float parameter."""
        _Numeric.__init__(
            self,
            optional=optional,
            description=description,
            default=default,
            min=min,
            max=max,
        )

    def _parse(self, val) -> float:
        """Parse the float value from a string value."""
        return float(val)

    def _update_default(self, default_value):
        """Update the default value of a float parameter, note that values such as nan/inf is not allowed."""
        if isinstance(default_value, float) and not math.isfinite(default_value):
            # Since nan/inf cannot be stored in the backend, just ignore them.
            logger.warning("Float default value %r is not allowed, ignored." % default_value)
            return
        return super()._update_default(default_value)


class Boolean(_Param):
    """Bool Parameter parse the value to a bool value."""

    DATA_TYPE = bool
    TYPE_NAME = 'boolean'

    def __init__(
        self,
        description=None,
        optional=True,
        default=False,
    ):
        """Initialize a bool parameter."""
        _Param.__init__(
            self,
            name=None,
            optional=optional,
            description=description,
            default=default,
        )

    def _parse(self, val) -> bool:
        """Parse the bool value from a string value."""
        lower_val = str(val).lower()
        if lower_val not in {'true', 'false'}:
            raise ValueError("Bool parameter '%s' only accept True/False, got %s." % (self.name, val))
        return True if lower_val == 'true' else False


class Enum(_Param):
    """Enum parameter parse the value according to its enum values."""

    TYPE_NAME = 'enum'

    def __init__(
        self,
        enum: Union[EnumMeta, Sequence[str]] = None,
        description=None,
        optional=False,
        default=None,
    ):
        """Initialize an enum parameter, the options of an enum parameter are the enum values."""
        enum_values = self._assert_enum_valid(enum)
        # This is used to parse enum class instead of enum str value if a enum class is provided.
        if isinstance(enum, EnumMeta):
            self._enum_class = enum
            self._str2enum = {v: e for v, e in zip(enum_values, enum)}
        else:
            self._enum_class = None
            self._str2enum = {v: v for v in enum_values}
        super().__init__(
            name=None,
            optional=optional,
            description=description,
            enum=enum_values,
        )
        self._allowed_types = (str, ) if not self._enum_class else (self._enum_class, str, )
        self._update_default(default)

    @classmethod
    def _assert_enum_valid(cls, enum):
        """Check whether the enum is valid and return the values of the enum."""
        if isinstance(enum, EnumMeta):
            enum_values = [str(option.value) for option in enum]
        elif isinstance(enum, Iterable):
            enum_values = list(enum)
        else:
            raise ValueError("enum must be a subclass of Enum or an iterable.")

        if len(enum_values) <= 0:
            raise ValueError("enum must have enum values.")

        if any(not isinstance(v, str) for v in enum_values):
            raise ValueError("enum values must be str type.")

        return enum_values

    def _parse(self, str_val: str):
        """Parse the enum value from a string value or the enum value."""
        if str_val is None:
            return str_val

        if self._enum_class and isinstance(str_val, self._enum_class):
            return str_val  # Directly return the enum value if it is the enum.

        if str_val not in self._str2enum:
            raise ValueError("Not a valid enum value: '%s', valid values: %s" % (str_val, ', '.join(self.enum)))
        return self._str2enum[str_val]

    def _update_default(self, default_value):
        """Enum parameter support updating values with a string value."""
        enum_val = self._parse(default_value)
        if self._enum_class and isinstance(enum_val, self._enum_class):
            enum_val = enum_val.value
        self._default = enum_val


# The following mappings are used to make it easier to find the corresponding class from a python type, vice versa.
_DATA_TYPE_MAPPING = {
    v.DATA_TYPE: v
    for v in globals().values() if isinstance(v, type) and issubclass(v, _Param) and v.DATA_TYPE
}

_DATA_TYPE_NAME_MAPPING = {
    **{
        v.DATA_TYPE.__name__: v
        for v in globals().values() if isinstance(v, type) and issubclass(v, _Param) and v.DATA_TYPE
    },
    **{
        v.__name__: v
        for v in globals().values() if isinstance(v, type) and issubclass(v, _Param) and v.DATA_TYPE
    }
}


def _get_annotation_by_type(t: type):
    return _DATA_TYPE_MAPPING.get(t)


def _remove_empty_values(data):
    if not isinstance(data, dict):
        return data
    return {k: v for k, v in data.items() if v is not None}
