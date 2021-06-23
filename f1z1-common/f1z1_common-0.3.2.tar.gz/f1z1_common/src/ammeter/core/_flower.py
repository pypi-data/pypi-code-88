# @Time     : 2021/4/14
# @Project  : w8_project_py
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
import abc
from functools import wraps
from typing import Callable

from ...utils import TimestampUnit, TimestampTypes
from ...validator import check_function

from . import (
    MessageCounter,
    MessageTimer
)

Function = Callable


class AbsMessageFlower(metaclass=abc.ABCMeta):
    """
    消息流
    """

    def __init__(self,
                 timeout_callback: Function,
                 wait_time: TimestampTypes,
                 unit: TimestampUnit = TimestampUnit.MILLISECOND):
        self._message_counter = MessageCounter(0)
        self._message_timer = MessageTimer(unit, wait_time)

        check_function(timeout_callback)
        self._timeout_callback = timeout_callback

    @property
    def message_timer(self):
        """
        timer
        :return:
        """
        return self._message_timer

    @property
    def message_counter(self):
        """
        counter
        :return:
        """
        return self._message_counter

    @property
    def timeout_callback(self) -> Function:
        """
        timeout callback
        :return:
        """
        return self._timeout_callback

    @abc.abstractmethod
    def tracking(self, func: Function) -> Function:
        raise NotImplementedError()

    def auto_increment(self, value: int) -> None:
        """
        auto increment
        :param value:
        :return:
        """
        self.message_counter.change(value)

    def _restart(self) -> None:
        """
        restart
        :return:
        """
        self.message_timer.restart()
        self.message_counter.clear()

    def trigger(self, callback: Function) -> None:
        if self.message_timer.is_timeout():
            callback(self.message_counter.get_current())
            self._restart()


class SyncMessageFlower(AbsMessageFlower):
    """
    同步消息计流器
    """

    def tracking(self, func: Function) -> Function:
        flower = self

        @wraps(func)
        def decorating_function(*args, **kwargs):
            flower.message_timer.start()
            result = func(*args, **kwargs)
            flower.auto_increment(1)
            flower.trigger(flower.timeout_callback)
            return result

        return decorating_function


class AsyncMessageFlower(AbsMessageFlower):
    """
    异步消息计流器
    """

    def tracking(self, func: Function) -> Function:
        flower = self

        @wraps(func)
        async def decorating_function(*args, **kwargs):
            flower.message_timer.start()
            result = await func(*args, **kwargs)

            flower.auto_increment(1)
            flower.trigger(flower.timeout_callback)
            return result

        return decorating_function
