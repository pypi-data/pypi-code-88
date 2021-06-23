# @Time     : 2021/5/27
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from functools import partial

from .validators import AbstractValidator
from .validators.func import FunctionValidator
from .validators.afunc import AsyncFunctionValidator


def is_validator_subclass(klass):
    return issubclass(klass, AbstractValidator)


def _factory(subclass: AbstractValidator, message: str):
    if not is_validator_subclass(subclass):
        raise ValueError(f"need a {AbstractValidator.__name__} subclass, but got {type(subclass).__name__}")
    return partial(subclass, message)


def create(subclass: AbstractValidator, message: str, **kwargs) -> AbstractValidator:
    f = _factory(subclass, message)
    return f(**kwargs)


def checker(
        subclass: AbstractValidator,
        value,
        message: str,
        **kwargs
):
    validator = create(subclass, message)
    return validator(value)


def check_function(value):
    return checker(
        FunctionValidator,
        value,
        f"value need function or Callable, but got {type(value).__name__}"
    )


def check_async_function(value):
    return checker(
        AsyncFunctionValidator,
        value,
        f"value need async function, but got {type(value).__name__}"
    )
