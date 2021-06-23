#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2021/3/31 15:46:44

@author: LiuKuan
@copyright: Apache License, Version 2.0
'''

#===============================================================================
# 
#===============================================================================

def file_read_lines(fname, encoding=None, skip_empty = False):
    retList = []
    with open(fname, 'r', encoding=None) as f:
        for line in f:
            line = line.strip()
            if skip_empty and not line:
                continue
            retList.append(line)
    return retList

def file_write_lines(fname, lines, encoding=None):
    with open(fname, 'w', encoding=encoding) as f:
        for line in lines:
            f.write(line)
            f.write('\n')
