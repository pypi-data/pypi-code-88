# @Time     : 2021/6/1
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from abc import ABCMeta, abstractmethod


class AbstractValidator(metaclass=ABCMeta):

    def __init__(self, error_message: str):
        self._message = error_message

    @property
    def error_message(self):
        return self._message

    @abstractmethod
    def is_validate(self, value, **kwargs) -> bool:
        raise NotImplementedError("NotImplemented .is_validate(value) -> bool")

    @abstractmethod
    def raise_error(self, message: str):
        raise NotImplementedError("NotImplemented .raise_error(message)")

    def __call__(self, value, **kwargs):
        result = self.is_validate(value, **kwargs)
        if not result:
            self.raise_error(self.error_message)
        return result
