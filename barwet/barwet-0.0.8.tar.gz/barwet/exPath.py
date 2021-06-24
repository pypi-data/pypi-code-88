#!/usr/bin/env python
# coding: utf-8
import os
from os import PathLike
from os.path import exists, abspath
from pathlib import Path

## 检查文件是否存在
def if_file_exists(file_path, return_bool=False):
    if exists(file_path):
        return True if return_bool else file_path
    else:
        if return_bool:
            return False
        else:
            raise FileNotFoundError(file_path)

## 检查目录是否存在，不存在则创建，返回目录路径
def check_dir(dir_path: str, return_abspath=False):
    dir_path = Path(dir_path).as_posix()
    abs_path = Path(abspath(dir_path)).as_posix()
    if not os.path.exists(abs_path):
        os.makedirs(abs_path)
    return abs_path if return_abspath else dir_path

class FSPath(object):
    
    def __init__(self, x: PathLike) -> None:
        self._path_str = None
        self._path = None
        if isinstance(x, str):
            self._path_str = x
            self._path = Path(x)
        elif isinstance(x, Path):
            self._path = Path
            self._path_str = str(self._path)
        else:
            raise TypeError("Unsupported path type: %s" % type(x))

    def __str__(self) -> str:
        return self.as_posix()

    def as_posix(self) -> str:
        return self._path.as_posix()

    def as_instance(self) -> Path:
        return self._path

    @property
    def posix(self) -> str:
        return self.as_posix()

    @property
    def instance(self) -> Path:
        return self.as_instance()

    @property
    def basename(self) -> str:
        return os.path.basename(self._path)

    @property
    def dirname(self) -> str:
        return Path(os.path.dirname(self._path)).as_posix()

    @property
    def exists(self) -> bool:
        return self._path.exists()

    @property
    def not_exists(self) -> bool:
        return not self.exists

    @property
    def is_file(self) -> bool:
        return self._path.is_file()

    @property
    def is_not_file(self) -> bool:
        return not self.is_file

    @property
    def is_dir(self) -> bool:
        return self._path.is_dir()