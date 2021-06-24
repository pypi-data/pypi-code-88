#!/usr/bin/env Python
# coding=utf-8
#作者： tony

import types
from functools import wraps
class BindFunction(object):
    def __init__(self, func):
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, obj, objtype=None):
        "Simulate func_descr_get() in Objects/funcobject.c"
        if obj is None:
            return self
        return types.MethodType(self, obj)