# @Time     : 2021/4/13
# @Project  : w8_project_py
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from .. import AbsMessageCounter


class MessageCounter(AbsMessageCounter):

    def __init__(self, count: int):
        self._count = 0 if not isinstance(count, int) else abs(count)

    def get_current(self, **kwargs) -> int:
        return self._count

    def change(self, value: int, **kwargs) -> None:
        """
        update count
        :param value:
        :param kwargs:
        :return:
        """
        self._change(value)
        if self._count < 0:
            self.clear()

    def clear(self, **kwargs) -> None:
        """
        clear count
        :param kwargs:
        :return:
        """
        self._count = 0

    def _change(self, value: int) -> None:
        if not isinstance(value, int):
            value = 0

        self._count += value
