#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2021/4/6 15:01:16

@author: laok
@copyright: Apache License, Version 2.0
'''
import sys
# ===============================================================================
# 
# ===============================================================================
__all__ = ['line_num', 'func_name']

def line_num(depth = 1):
    '''获取当前行号
    '''
    return sys._getframe(depth).f_lineno

def func_name(depth = 1):
    '''获取当前函数名字
    '''
    return sys._getframe(depth).f_code.co_name

