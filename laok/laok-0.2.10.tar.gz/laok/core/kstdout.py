#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2021/3/15 19:48:37

@author: LiuKuan
@copyright: Apache License, Version 2.0
'''
import sys, contextlib
#===============================================================================
# 
#===============================================================================
__all__ = ['StdoutRedirect', 'stdout_redirect']


class _NullOutput:
    def __init__(self):
        pass

    def write(self, *args, **kws):
        pass

    def close(self):
        pass


class StdoutRedirect:
    def __init__(self, obj=None):
        '''
        :param obj:
            None, 表示空对象
            str, 表示文件名字
            否则, 其他类文件对象
        '''
        if obj is None:
            self._f = _NullOutput()
        elif isinstance(obj, str):
            self._f = open(obj, 'w')
        else:
            self._f = obj

    def __enter__(self):
        return self.doEnter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.doExit()

    def doEnter(self):
        self._old = sys.stdout
        sys.stdout = self._f
        return self

    def doExit(self):
        sys.stdout = self._old
        if hasattr(self._f, 'close'):
            self._f.close()

@contextlib.contextmanager
def stdout_redirect(filename = None):
    with StdoutRedirect(filename):
        yield

