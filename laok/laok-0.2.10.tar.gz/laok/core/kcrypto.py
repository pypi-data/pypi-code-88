#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2021/4/9 10:53:36

@author: laok
@copyright: Apache License, Version 2.0
'''
import hashlib
# ===============================================================================
# 
# ===============================================================================
__all__ = ['file_md5']

def file_md5(fpath, chunk_size=1024 * 1024):
    md5 = hashlib.md5()
    with open(fpath, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            md5.update(chunk)
    return md5.hexdigest()
