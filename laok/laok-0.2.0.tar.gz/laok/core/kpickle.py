#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2021/3/17 14:20:46

@author: LiuKuan
@copyright: Apache License, Version 2.0
'''
import pickle
import io
#===============================================================================
# 
#===============================================================================
__all__ = ['load']

def load(data):
    '''
    :param data: 支持从 bytes/filename/fileobj
    :return:
    '''
    if isinstance(data , bytes):
        return pickle.loads(data)
    elif isinstance(data, str):
        with open(data, 'rb') as f:
            return pickle.load(f)
    elif isinstance(data, io.FileIO) :
        return pickle.load(data)
