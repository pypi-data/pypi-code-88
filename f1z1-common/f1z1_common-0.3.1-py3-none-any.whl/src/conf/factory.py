# @Time     : 2021/5/31
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from .base import IReaderFactory
from .reader import IniReader, JsonReader
from ..utils import PathUtil


class ReaderFactory(IReaderFactory):

    @classmethod
    def create(cls, file, encoding=None, **kwargs):
        if cls.is_ini(file):
            return IniReader(file, encoding)
        elif cls.is_json(file):
            return JsonReader(file, encoding)
        else:
            raise ValueError(f"file ext name error, {file}")

    @staticmethod
    def is_json(file):
        return PathUtil.is_endswith_ext(file, [".json"])

    @staticmethod
    def is_ini(file):
        return PathUtil.is_endswith_ext(file, [".ini"])
