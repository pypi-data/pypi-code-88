# @Time     : 2021/6/1
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from .base import AbstractValidator
from ..error import NotAsyncFunctionError
from ..is_validators import is_async_function


class AsyncFunctionValidator(AbstractValidator):

    def is_validate(self, value, **kwargs) -> bool:
        return is_async_function(value)

    def raise_error(self, message: str):
        raise NotAsyncFunctionError(message)
