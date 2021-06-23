#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2021/3/17 21:11:08

@author: LiuKuan
@copyright: Apache License, Version 2.0
'''
import time as _time
import sys
from contextlib import contextmanager as _context
from functools import wraps as _wraps
#===============================================================================
# 
#===============================================================================

__all__ = ['auto_timer', 'Timer']

@_context
def auto_timer(msg = '', need_print = True):
    t1 = _time.time()
    yield
    t2 = _time.time()
    if need_print:
        print(f'{msg} [time:{(t2-t1)*1000}(ms)]')

def deco_time(stream = None):
    '''
    装饰器,记录时间
    '''
    def _w1(func):
        @_wraps(func)
        def _w2(*args, **kwargs):
            start = _time.time()
            res = func(*args, **kwargs)
            stop = _time.time()
            if _time is None:
                stream = sys.stdout
            stream.write(f"[{ func.__name__ }] use time [{ 1000*(stop-start) }(ms)]\n")
            return res
        return _w2
    return _w1


class Timer:
    def __init__(self):
        self.restart()

    def restart(self):
        self._t1 = _time.time()

    def elapse(self):
        '''
        time in seconds since the Epoch
        :return:
        '''
        return _time.time() - self._t1

