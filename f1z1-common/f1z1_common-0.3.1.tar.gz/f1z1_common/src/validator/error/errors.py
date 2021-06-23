# @Time     : 2021/6/1
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from .base import BaseError


class NotFunctionError(BaseError):
    pass


class NotAsyncFunctionError(BaseError):
    pass
