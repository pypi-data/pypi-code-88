# -*- coding:utf-8 -*-

from enum import Enum, auto
import logging as log
from typing import Dict

from fameio.source.schema.exception import SchemaException
from fameio.source.time import FameTime
from fameio.source.tools import keys_to_lower


class AttributeType(Enum):
    """Specifies known types that Attributes can take"""
    INTEGER = auto()
    DOUBLE = auto()
    LONG = auto()
    TIME_STAMP = auto()
    STRING = auto()
    ENUM = auto()
    TIME_SERIES = auto()
    BLOCK = auto()

    def convert_string_to_type(self, value: str):
        """Converts a given string to this AttributeType's data format"""
        if self is AttributeType.INTEGER or self is AttributeType.LONG:
            return int(value)
        elif self is AttributeType.DOUBLE:
            return float(value)
        elif self is AttributeType.TIME_STAMP:
            return FameTime.convert_string_if_is_datetime(value)
        elif self is AttributeType.ENUM or self is AttributeType.STRING:
            return str(value)
        elif self is AttributeType.TIME_SERIES:
            return float(value)
        else:
            raise ValueError("String conversion not supported for AttributeType '{}'.".format(self.value))


class AttributeSpecs:
    """Schema Definition of a single Attribute (with possible inner Attributes) of an agent"""
    _MISSING_SPEC_DEFAULT = "Missing '{}' specification for Attribute '{}' - assuming {}."
    _MISSING_TYPE = "'AttributeType' not declare for Attribute '{}'."
    _INVALID_TYPE = "'{}' is not a valid type for an Attribute."
    _DEFAULT_NOT_LIST = "Attribute is list, but provided Default '{}' is not a list."
    _DEFAULT_INCOMPATIBLE = "Default '{}' can not be converted to AttributeType '{}'."
    _DEFAULT_DISALLOWED = "Default '{}' is not an allowed value."
    _LIST_DISALLOWED = "Attribute '{}' of type TIME_SERIES cannot be list."

    _KEY_MANDATORY = 'Mandatory'.lower()
    _KEY_LIST = 'List'.lower()
    _KEY_TYPE = 'AttributeType'.lower()
    _KEY_NESTED = 'NestedAttributes'.lower()
    _KEY_VALUES = 'Values'.lower()
    _KEY_DEFAULT = 'Default'.lower()

    def __init__(self, name: str, definition: dict):
        """Loads Attribute from given `definition` """
        self._full_name = name
        definition = keys_to_lower(definition)

        if AttributeSpecs._KEY_MANDATORY in definition:
            self.is_mandatory = definition[AttributeSpecs._KEY_MANDATORY]
        else:
            self.is_mandatory = True
            log.warning(AttributeSpecs._MISSING_SPEC_DEFAULT.format(AttributeSpecs._KEY_MANDATORY, name, True))

        if AttributeSpecs._KEY_LIST in definition:
            self.is_list = definition[AttributeSpecs._KEY_LIST]
        else:
            self.is_list = False
            log.warning(AttributeSpecs._MISSING_SPEC_DEFAULT.format(AttributeSpecs._KEY_LIST, name, False))

        if AttributeSpecs._KEY_TYPE in definition:
            self.type = AttributeSpecs._get_type_for_name(definition[AttributeSpecs._KEY_TYPE])
        else:
            log.error(AttributeSpecs._MISSING_TYPE.format(name))
            raise SchemaException(AttributeSpecs._MISSING_TYPE.format(name))

        if self.type == AttributeType.TIME_SERIES and self.is_list:
            raise SchemaException(AttributeSpecs._LIST_DISALLOWED.format(name))

        self.values = list()
        if AttributeSpecs._KEY_VALUES in definition:
            self.values = definition[AttributeSpecs._KEY_VALUES]

        self.default = None
        if AttributeSpecs._KEY_DEFAULT in definition:
            provided_value = definition[AttributeSpecs._KEY_DEFAULT]
            if self.is_list:
                self.default = self._convert_list(provided_value)
            else:
                self.default = self._convert_to_data_type(provided_value)

        self.nested = dict()
        if AttributeSpecs._KEY_NESTED in definition:
            for nested_name, nested_details in definition[AttributeSpecs._KEY_NESTED].items():
                full_name = name + "." + nested_name
                self.nested[nested_name] = AttributeSpecs(full_name, nested_details)

    def _convert_list(self, values) -> list:
        """Converts all entries in given `values` list to this Attributes data type and returns this new list"""
        if isinstance(values, list):
            return [self._convert_to_data_type(item) for item in values]
        else:
            raise SchemaException(AttributeSpecs._DEFAULT_NOT_LIST.format(values))

    def _convert_to_data_type(self, value: str):
        """Converts a given single `value` to this Attribute's data type"""
        try:
            converted = self.type.convert_string_to_type(value)
            if self.values and converted not in self.values:
                raise SchemaException(AttributeSpecs._DEFAULT_DISALLOWED.format(value))
            return converted
        except ValueError:
            raise SchemaException(AttributeSpecs._DEFAULT_INCOMPATIBLE.format(value, self.type))

    def get_attributes(self) -> Dict[str, 'AttributeSpecs']:
        """ Returns list of nested Attributes of this Attribute or an empty dict if no nested attributes are defined"""
        return self.nested

    def get_type(self) -> AttributeType:
        """Returns AttributeType of this attribute"""
        return self.type

    def has_nested_attributes(self) -> bool:
        """Returns True if nested attributes are defined"""
        return bool(self.nested)

    def has_default(self) -> bool:
        """Return True if a default value is available"""
        return self.default is not None

    @staticmethod
    def _get_type_for_name(name: str) -> 'AttributeType':
        """Returns the AttributeType matching the given `name` converted to upper case"""
        try:
            return AttributeType[name.upper()]
        except KeyError:
            raise SchemaException(AttributeSpecs._INVALID_TYPE.format(name))

    def get_full_name(self) -> str:
        """Returns name including name of enclosing parent attributes"""
        return self._full_name

    def __repr__(self) -> str:
        return self._full_name
