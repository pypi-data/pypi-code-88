# @Time     : 2021/4/13
# @Project  : w8_project_py
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
import abc
import enum
import typing

from ..utils import TimestampUnit

T = typing.TypeVar("T")


class TimeoutStates(enum.Enum):
    """
    超时状态枚举
    """
    UN_TIMEOUT = 0
    TIMEOUT = 1


class RunStates(enum.Enum):
    """
    运行状态
    """
    UN_START = 0  # 停
    STARTED = 1  # 已开始
    PAUSE = 2  # 停止


class AbsMessageTimer(metaclass=abc.ABCMeta):
    """
    消息计时器
    """

    @abc.abstractmethod
    def unit(self) -> TimestampUnit:
        """
        time unit
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def is_timeout(self) -> bool:
        """
        is_timeout
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_current(self, **kwargs) -> T:
        """
        get current time
        :param kwargs:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def start(self, **kwargs) -> None:
        """
        start timer
        :param kwargs:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def restart(self, **kwargs) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def stop(self, **kwargs) -> None:
        """
        stop timer
        :param kwargs:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def clear(self) -> None:
        """
        clear timeout
        :return:
        """
        raise NotImplementedError()


class AbsMessageCounter(metaclass=abc.ABCMeta):
    """
    消息计数器
    """

    @abc.abstractmethod
    def get_current(self, **kwargs) -> T:
        """
        get current count
        :param kwargs:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def change(self, value: T, **kwargs) -> None:
        """
        update
        :param value:
        :param kwargs:
        :return:
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def clear(self, **kwargs) -> None:
        """
        clear
        :return:
        """
        raise NotImplementedError()
