# @Time     : 2021/5/26
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from pathlib import Path
from typing import AnyStr, List, Union

from .strings import StringsUtil
from ..validator.is_validators import is_any_string, is_list, is_path

PathTypes = Union[AnyStr, Path]


class PathUtil(object):

    @classmethod
    def get_path_from_base_dir(cls, basename: PathTypes, *paths) -> Path:
        base_dir = cls.get_base_dir(basename)
        if not base_dir.exists():
            raise ValueError(f"base dir need Path, but got {type(base_dir).__name__}")
        return base_dir.joinpath(*paths)

    @classmethod
    def get_base_dir(cls, basename: PathTypes) -> Path:
        """
        get base path dir
        :param basename:
        :return:
        """
        base_path: Path = cls.to_path(basename)
        if not base_path.exists():
            return Path.cwd()

        if base_path.is_file():
            return base_path.cwd()

        return base_path

    @classmethod
    def is_endswith_ext(cls, path: PathTypes, ext_names: List[str] = None) -> bool:
        """
        is file by ext name
        :param path:
        :param ext_names:
        :return:
        """
        file = cls.to_path(path)
        if not file.exists():
            raise ValueError(f"not found file from {path}")

        extensions = []
        if cls.is_extension_names(ext_names):
            extensions = ext_names
        if not extensions:
            return True
        return file.suffix in extensions

    @staticmethod
    def is_extension_names(value):
        return is_list(value)

    @classmethod
    def to_absolute(cls, path: PathTypes) -> Path:
        """
        to absolute path
        :param path:
        :return:
        """
        return cls.to_path(path).absolute()

    @classmethod
    def to_resolve(cls, path: PathTypes) -> Path:
        """
        to resolve path
        :param path:
        :return:
        """
        return cls.to_path(path).resolve()

    @classmethod
    def to_path(cls, anystr_or_path: PathTypes) -> Path:
        """
        string or bytes to path
        :param anystr_or_path:
        :return:
        """
        path: Path = None
        if is_path(anystr_or_path):
            path = anystr_or_path
        elif is_any_string(anystr_or_path):
            path = Path(StringsUtil.anystr_to_string(anystr_or_path))
        else:
            raise ValueError(
                f"need a string, bytes or Path, but got {type(anystr_or_path).__name__}"
            )
        return path
