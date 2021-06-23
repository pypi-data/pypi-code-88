# @Time     : 2021/5/27
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from enum import Enum
from typing import Dict, Union

from ..utils import EnumUtil
from ..validator.is_validators import is_dict, is_enum_subclass, is_none

AllowedOptionsTypes = Union[Dict, Enum]


class IAllowedStatic(object):
    """
    allowed static options interface, this is descriptors
    """

    def __get__(self, instance, owner):
        raise NotImplementedError("NotImplemented .__get__(interface, owner)")

    def add(self, name, allowed) -> None:
        raise NotImplementedError("NotImplemented .add(name, allowed) -> None")

    def get(self, allowed):
        raise NotImplementedError("NotImplemented .get(allowed)")

    def has(self, allowed) -> bool:
        raise NotImplementedError("NotImplemented .has(allowed)")


def _un_dict(options: Dict):
    if not options:
        return {}
    return {k: v for k, v in options.items()}


def _un_enum_subclass(options: Enum):
    return EnumUtil.unenum_to_dict(options)


class Allowed(IAllowedStatic):

    def __init__(self, options: AllowedOptionsTypes):
        self._options = self._to_options(options)

    def __get__(self, interface, owner):
        return self

    def add(self, name, option) -> None:
        self[name] = option

    def get(self, option):
        return self[option]

    def has(self, option):
        return option in self._options

    def __setitem__(self, name, allowed):
        if any([is_none(name), is_none(allowed)]):
            raise ValueError(f"allowed options key or value is not None")
        self._options[name] = allowed

    def __getitem__(self, option):
        if not self.has(option):
            raise KeyError(f"not found allowed {option}, from allowed {self}")
        return self._options[option]

    def __str__(self) -> str:
        return self._to_string()

    def _to_string(self, split: str = ", "):
        return split.join([str(member) for _, member in enumerate(self._options)])

    def _to_options(self, options: AllowedOptionsTypes) -> dict:
        if is_dict(options):
            return _un_dict(options)
        elif is_enum_subclass(options):
            return _un_enum_subclass(options)
        else:
            raise ValueError(
                f"options need Enum or dict, but got {type(options).__name__}"
            )
