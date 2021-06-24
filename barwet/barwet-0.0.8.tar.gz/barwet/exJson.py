#!/usr/bin/env python
# coding: utf-8

import os
import json
from typing import Any

def dump(obj: Any, fp: str, indent: int=4, **kwargs):
    """将数据转化为json字符串保存到文件中"""
    with open(fp, 'w') as w:
        json.dump(obj, w, indent=indent, **kwargs)

def dump_jstr(jstr: str, fp: str, indent: int=4, **kwargs):
    data = json.loads(jstr)
    dump(data, fp, indent=indent, **kwargs)

def dumps(obj: Any, indent: int=None,  **kwargs):
    """将数据转化为json字符串并返回字符串"""
    return json.dumps(obj, indent=indent, **kwargs)

def load(fp: str, **kwargs):
    """读取包含json内容的文件"""
    with open(fp) as r:
        data = json.load(r, **kwargs)
    return data

def loads(s: str, **kwargs):
    """读取包含json内容的字符串"""
    return json.loads(s, **kwargs)

def load_from_simple_yaml(fp: str, sep=':', header=False):
    data = {}
    with open(fp) as r:
        if header: next(r)
        for line in r:
            ls = line.strip().split(sep)
            data[ls[0].strip()] = ls[1].strip()
    return data