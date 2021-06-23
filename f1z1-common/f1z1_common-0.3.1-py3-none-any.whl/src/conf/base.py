# @Time     : 2021/5/30
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
"""
conf module interfaces
"""
from abc import ABCMeta, abstractmethod

from ..utils import EncodingTypes, PathTypes
from . import ReaderUtil


class AbstractConfReader(metaclass=ABCMeta):
    """
    config reader abc class
    """

    def __init__(self, file: PathTypes, encoding: EncodingTypes = None):
        self._file = file
        self._encoding = ReaderUtil.to_encoding(encoding)

    @property
    def file(self):
        return self._file

    @property
    def encoding(self):
        return self._encoding

    @abstractmethod
    def has_node(self, node) -> bool:
        raise NotImplementedError("NotImplemented .has_node(node) -> bool")

    @abstractmethod
    def get_int(self, node: str, option) -> int:
        raise NotImplementedError("NotImplemented .get_int(node, option) -> int")

    @abstractmethod
    def get_float(self, node: str, option) -> float:
        raise NotImplementedError("NotImplemented .get_float(node, option) -> float")

    @abstractmethod
    def get_string(self, node: str, option) -> str:
        raise NotImplementedError("NotImplemented .get_string(node, option) -> str")


class IReaderFactory(object):

    @classmethod
    def create(cls, file: PathTypes, encoding: EncodingTypes, **kwargs) -> AbstractConfReader:
        raise NotImplementedError("NotImplemented .create() -> AbstractConfReader")
