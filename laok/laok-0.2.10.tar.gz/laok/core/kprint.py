#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2021/3/17 20:19:45

@author: LiuKuan
@copyright: Apache License, Version 2.0
'''
import inspect
#===============================================================================
# 实现特定格式数据的打印
#===============================================================================

__all__ = [ 'kprint']

def kprint(d, **kws):
    '''多态打印数据类型
    '''
    _kp_data.do_print(d, **kws)

# 打印配置
class _KPData:
    def __init__(self):
        self._print_funcs = {}

    ###################### 打印相关函数
    def do_print(self, d, **kws):
        t =  type(d)
        func = self._print_funcs[t] if t in self._print_funcs else self._def_print
        msg = func(d, **kws)
        print(msg)

    def register_print(self, name):
        def deco(f):
            self._print_funcs[name] = f
            return f
        return deco

    def unregister_print(self, name):
        if name in self._print_funcs:
            del self._print_funcs[name]

    def _def_print(self, d, **kws):
        msg = f'-----id:{id(d)} type:{type(d)}\n'
        msg += f'{d}'
        return msg

_kp_data = _KPData()