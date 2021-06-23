# @Time     : 2021/5/31
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from ..utils import EncodingTypes, StringsUtil
from ..validator.is_validators import (
    is_any_string,
    is_float,
    is_int,
    is_number,
    is_string
)


class ReaderUtil(object):

    @staticmethod
    def to_int(value):
        if is_int(value):
            return value
        elif is_number(value):
            return int(value)
        else:
            raise ValueError(f"value need float or int, but got {type(value).__name__}")

    @staticmethod
    def to_float(value):
        if is_float(value):
            return value
        elif is_number(value):
            return float(value)
        else:
            raise ValueError(f"value need float or int, but got {type(value).__name__}")

    @staticmethod
    def to_string(value):
        if is_string(value):
            return value
        elif is_any_string(value):
            return StringsUtil.anystr_to_string(value)
        return str(value)

    @staticmethod
    def to_encoding(encoding: EncodingTypes = None):
        return StringsUtil.to_encoding(encoding)
