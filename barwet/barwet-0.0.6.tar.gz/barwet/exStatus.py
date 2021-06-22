#!/usr/bin/env python
# coding: utf-8

import os
from typing import Any, Union
from .exJson import load, dump, dumps

BaseType = Union[bool, int, float, str]

class JStatus:
    """存取json文件中的变量值，只存储基本类型的变量
    """
    def __init__(self, fp: str):
        self._stfile = fp
        self._data = load(fp) if os.path.exists(fp) else {}

    def __str__(self) -> str:
        return dumps(self._data)

    def __save__(self):
        dump(self._data, self._stfile)

    def set(self, key: str, val: BaseType):
        self._data[key] = val
        self.__save__()

    def get(self, key: str):
        return self._data.get(key)
