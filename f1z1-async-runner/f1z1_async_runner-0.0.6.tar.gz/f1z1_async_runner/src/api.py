# @Time     : 2021/5/28
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from .runner.base import AbstractRunner
from .runner import AsyncRunner


def is_runner(value):
    return isinstance(value, AbstractRunner)


def create_runner(coro_or_func,
                  args=None,
                  kwargs=None):
    """
    runner factory
    :param coro_or_func: coroutine, async function or function
    :param args: tuple or None
    :param kwargs: kwargs or None
    :return:
    """
    return AsyncRunner(
        coro_or_func,
        args=args,
        kwargs=kwargs
    )


def start(runner: AbstractRunner):
    if not is_runner(runner):
        raise ValueError(f"runner need IRunner instance, but got {type(runner).__name__}")
    return runner.run()
