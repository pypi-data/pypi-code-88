# @Time     : 2021/5/27
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from .base import AbstractCallbackManager
from ..validator import check_function, check_async_function


class CallbackManager(AbstractCallbackManager):

    def check(self, value):
        return check_function(value)


class AsyncCallbackManager(AbstractCallbackManager):

    def check(self, value):
        return check_async_function(value)
