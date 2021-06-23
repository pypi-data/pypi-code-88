# @Time     : 2021/5/27
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from enum import Enum
from typing import Any

from ..validator.is_validators import is_enum, is_enum_subclass


class EnumUtil(object):

    @classmethod
    def unenum_to_dict(cls, enum_subclass: Enum) -> dict:
        if not is_enum_subclass(enum_subclass):
            raise ValueError(f"enum klass not Enum subclass, got {type(enum_subclass).__name__}")
        unenum = cls.unenum
        return {member: unenum(member, "value") for _, member in enumerate(enum_subclass)}

    @classmethod
    def unenum(cls, any_or_member: Enum, name_or_value: str = "value"):
        method = {
            "name": cls._to_name,
            "value": cls._to_value
        }.get(name_or_value, "value")
        return method(any_or_member)

    @staticmethod
    def _to_value(any_or_member: Enum) -> Any:
        return any_or_member.value if is_enum(any_or_member) else any_or_member

    @staticmethod
    def _to_name(any_or_member: Enum) -> str:
        return any_or_member.name if is_enum(any_or_member) else any_or_member
