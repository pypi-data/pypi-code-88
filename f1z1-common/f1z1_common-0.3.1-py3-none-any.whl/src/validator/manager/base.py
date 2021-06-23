# @Time     : 2021/6/1
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from typing import Callable, Union

from ..validators.base import AbstractValidator

ValidatorTypes = Union[AbstractValidator, Callable]


class IValidatorManager(object):

    def add(self, validator: ValidatorTypes) -> int:
        raise NotImplementedError("NotImplemented .add() -> int")

    def remove(self, validator: ValidatorTypes) -> int:
        raise NotImplementedError("NotImplemented .remove() -> int")

    def is_validate(self, value, **kwargs) -> bool:
        raise NotImplementedError("NotImplemented .is_validate() -> bool")
