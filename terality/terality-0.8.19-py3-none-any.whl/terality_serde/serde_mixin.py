from __future__ import annotations
import base64
from enum import Enum
import zlib
from dataclasses import dataclass
import inspect
import json
import sys
from typing import Any, ClassVar, Dict, List, Optional, Type

from . import ExternalTypeSerializer, all_external_types


class SerdeMixin:
    subclasses = []  # type: ignore

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    @property
    def class_name(self) -> str:
        return self.__class__.__name__

    @classmethod
    def _cached_properties_names(cls):
        from functools import cached_property

        return {k for k, v in inspect.getmembers(cls) if isinstance(v, cached_property)} | {
            # betterproto internal fields
            "_unknown_fields",
            "_serialized_on_wire",
            "_group_map",
        }

    @property
    def dict(self) -> dict:
        if sys.version_info[1] >= 8:
            dict_ = {
                k: v for k, v in self.__dict__.items() if k not in self._cached_properties_names()
            }
        else:
            dict_ = dict(self.__dict__)
        return dict_

    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**kwargs)


class SerializableEnum(SerdeMixin, Enum):
    """An Enum that is also serializable.

    Usage:
    >>> class MySerializableEnum(SerializableEnum):
            VARIANT_1 = "VARIANT_1"
            VARIANT_2 = "VARIANT_2"
    """

    @property
    def dict(self) -> Dict:
        dict_ = {"name": self.name}
        return dict_

    @classmethod
    def from_dict(cls, name: str) -> SerializableEnum:  # type: ignore
        return cls[name]


@dataclass
class SerdeConfig:
    _internal_type_attribute: ClassVar[str] = "!terality:internal_type"
    _external_type_attribute: ClassVar[str] = "!terality:external_type"
    _external_types_serializer: ClassVar[List[ExternalTypeSerializer]] = all_external_types  # type: ignore
    _external_types: ClassVar[Dict[Type, ExternalTypeSerializer]] = {
        ex.class_: ex for ex in all_external_types  # type: ignore
    }
    _external_types_serde: ClassVar[Dict[Type, ExternalTypeSerializer]] = {
        ex.class_name: ex for ex in all_external_types  # type: ignore
    }
    _whitelisted_types: Optional[List[Type[SerdeMixin]]] = None
    # mappings derived from previous, could be changed to properties or cached properties
    # _external_types: Dict[Type, ExternalTypeSerializer] = field(init=False)
    # _external_types_serde: Dict[str, ExternalTypeSerializer] = field(init=False)
    # self._external_types_serializer =
    # self._external_types =
    # self.
    #
    # def __post_init__(self):

    @classmethod
    def serialize(cls, obj):
        if isinstance(obj, SerdeMixin):
            dict_ = obj.dict
            dict_[cls._internal_type_attribute] = obj.class_name
            encoded = dict_
        elif type(obj) in cls._external_types:
            external_type = cls._external_types[type(obj)]
            dict_ = external_type.to_json(obj)
            dict_[cls._external_type_attribute] = external_type.class_name
            encoded = dict_
        else:
            encoded = obj

        if isinstance(encoded, list):  # pylint: disable=no-else-return
            return [cls.serialize(elt) for elt in encoded]
        elif isinstance(encoded, dict):
            return {cls.serialize(k): cls.serialize(v) for k, v in encoded.items()}
        else:
            return encoded

    @property
    def _internal_types(self) -> Dict[str, Type[SerdeMixin]]:
        # Put in a property so that it gets computed at runtime at the last minute before it is needed
        # We do this because the problem of the subclasses registration is that it only happens if the subclass gets
        # imported in an __init__ somewhere, so we compute this function at the latest moment to give a chance for
        # the subclasses to have be imported
        return {internal.__name__: internal for internal in SerdeMixin.subclasses}

    def deserialize(self, obj):
        if self._internal_type_attribute in obj:
            internal_type_name = obj.pop(self._internal_type_attribute)
            internal_type = self._internal_types[internal_type_name]
            # if self._whitelisted_types is not None and internal_type not in self._whitelisted_types:
            #     raise ValueError(f'Trying to deserialize a {internal_type} which is not permitted')
            return internal_type.from_dict(**obj)
        if self._external_type_attribute in obj:
            external_type_name = obj.pop(self._external_type_attribute)
            deserializer = self._external_types_serde[external_type_name]
            return deserializer.from_json(**obj)
        return obj


# pylint: disable=invalid-name
def dumps(o: Any, compressed: bool = False) -> str:
    o = SerdeConfig.serialize(o)
    result = json.dumps(o)
    if compressed:
        result = base64.encodebytes(zlib.compress(result.encode("utf-8"))).decode("utf-8")
    return result


# pylint: disable=invalid-name
def loads(
    s: str,
    whitelisted_types: Optional[List[Type[SerdeMixin]]] = None,
    compressed: bool = False,
) -> Any:
    if compressed:
        s = zlib.decompress(base64.decodebytes(s.encode("utf-8"))).decode("utf-8")
    serde_config = SerdeConfig(_whitelisted_types=whitelisted_types)
    return json.loads(s, object_hook=serde_config.deserialize)
