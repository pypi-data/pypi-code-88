# @Time     : 2021/6/1
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from typing import List

from .base import IValidatorManager, ValidatorTypes
from ..validators import AbstractValidator
from ..is_validators import is_function

ValidatorList = List[ValidatorTypes]


class ValidatorManager(IValidatorManager):

    def __init__(self):
        self._validators: ValidatorList = []

    @property
    def validators(self):
        return self._validators

    @property
    def length(self) -> int:
        return len(self.validators)

    def empty(self):
        return not self.length

    def add(self, validator):
        if not self._is_validator(validator):
            return self.length

        if not self._is_exists(validator):
            self.validators.append(validator)

        return self.length

    def remove(self, validator):
        if self.empty():
            return self.length
        idx = self._find(validator)
        if idx > -1:
            self.validators.pop(idx)
        return self.length

    def is_validate(self, value, **kwargs) -> bool:
        return all(validator(value) for validator in self)

    def __iter__(self):
        if not self.empty():
            for _, validator in enumerate(self.validators):
                yield validator

    def _is_validator(self, value):
        return any([
            is_function(value),
            isinstance(value, AbstractValidator)
        ])

    def _find(self, validator: ValidatorTypes) -> int:
        if not self._is_exists(validator):
            return -1
        return self.validators.index(validator)

    def _is_exists(self, validator: ValidatorTypes) -> bool:
        if self.empty():
            return False
        return validator in self.validators
