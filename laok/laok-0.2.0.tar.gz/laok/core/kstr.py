#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2020/8/7 14:20:19

@author: LiuKuan
@copyright: Apache License, Version 2.0
'''

#===============================================================================
# 
#===============================================================================

class ChainName(object):
    '''用于实现一个 支持级联调用的 魔法类
    '''
    def __init__(self, prefix, callback, sep = "/"):
        self._prefix = prefix
        self._callback = callback
        self._sep = sep

    def __getattr__(self, item):
        next_prefix = self._prefix + self._sep + item
        return ChainName(next_prefix, self._callback)

    def __call__(self, *kargs, **kwargs):
        self._callback(self._prefix, *kargs, **kwargs)

    def __getitem__(self,item):
        self._prefix = item
        return self

    def get_prefix(self):
        return self._prefix


def index_list(s, sep, escape = None):
    '''获取索引
    :param s:
    :param sep:
    :return:
    '''
    ret = []
    idx = -1
    while 1:
        _i = s.find(sep, idx+1)
        if _i == -1:
            break

        if escape and _i > 0 and s[_i-1] == escape:
            continue

        idx = _i
        ret.append(idx)
    return ret

def index_list_remove_in_range(s, idx_list, range_start, range_end):
    '''删除范围内的索引
    :param s:
    :param idx_list: 索引列表
    :param range_start: 起始符号
    :param range_end: 结束符号
    :return: 剔除了不需要的索引
    '''
    if not idx_list:
        return idx_list
    ret_list = idx_list[:]
    i_start = -1
    i_end = -1

    while 1:
        i_start = s.find(range_start, i_start+1)
        i_end = s.find(range_end, i_end+1)

        if i_start == -1 or i_end == -1:
            break

        for i in range(len(ret_list) - 1, -1, -1):
            if i_start < ret_list[i] < i_end:
                ret_list.pop(i)

    return ret_list


def index_list_to_substrs(s, idx_list):
    '''将索引分割成子串列表
    :param s:
    :param idx_list:
    :return:
    '''
    substrs = []
    lastIdx = -1
    for idx in idx_list:
        substrs.append(s[lastIdx+1:idx])
        lastIdx = idx
    substrs.append(s[lastIdx+1:])
    return substrs
