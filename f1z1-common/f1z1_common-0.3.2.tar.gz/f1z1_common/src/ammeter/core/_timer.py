# @Time     : 2021/4/13
# @Project  : w8_project_py
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
import time

from ...utils import TimestampUtil, TimestampUnit, TimestampTypes
from .. import AbsMessageTimer, RunStates


class MessageTimer(AbsMessageTimer):

    def __init__(self, unit: TimestampUnit, wait_time: TimestampTypes):

        self._state: RunStates = RunStates.UN_START  # 状态
        self._step_time: TimestampTypes = 0  # 间隔时间
        self._start_time: TimestampTypes = 0  # 开始时间
        self._unit: TimestampUnit = unit  # 时间单位
        self._wait_time = wait_time  # 超时时间

    @property
    def unit(self) -> TimestampUnit:
        return self._unit

    @property
    def is_started(self) -> bool:
        return self._state == RunStates.STARTED

    def is_timeout(self) -> bool:
        """
        is timeout
        :return:
        """
        self._set_step(self._get_step())
        return self._step_time >= self._wait_time

    def get_current(self, **kwargs) -> TimestampTypes:
        """
        get current
        :param kwargs:
        :return:
        """
        # return self._convert_time(time.time(), self.unit)
        return TimestampUtil.to_timestamp(time.time(), self.unit)

    def start(self, **kwargs) -> None:
        if self.is_started:
            return

        # update state, start time
        self._set_state(RunStates.STARTED)
        self._set_start(self.get_current())

    def restart(self, **kwargs) -> None:
        """
        restart timer
        :return:
        """
        self._set_start(self.get_current())
        self._set_step(0)

    def stop(self, **kwargs) -> None:
        # update state, step time
        self._set_state(RunStates.PAUSE)
        self._set_step(self._get_step())

    def clear(self) -> None:
        """
        clear timer
        :return:
        """
        self._set_state(RunStates.UN_START)
        self._set_start(0)

    def _set_start(self, current: TimestampTypes) -> None:
        if not isinstance(current, (int, float)):
            raise TypeError("current type error, int or float")
        self._start_time = abs(current)

    def _set_state(self, state: RunStates) -> None:
        if not isinstance(state, RunStates):
            state = RunStates.UN_START

        self._state = state

    def _set_step(self, step: TimestampTypes) -> None:
        if step < 0:
            self._step_time = 0
        else:
            self._step_time = step

    def _get_step(self) -> TimestampTypes:
        return self.get_current() - self._start_time
