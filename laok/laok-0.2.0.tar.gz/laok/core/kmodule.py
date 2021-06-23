#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2020/8/12 10:06:00

@author: LiuKuan
@copyright: Apache License, Version 2.0
'''
import importlib, os.path, sys
#===============================================================================
#
#===============================================================================

# 将文件当成模块,然后加载
def dy_load_module(codefile, reload = False):
    '''
    动态加载模块
    '''
    if not isinstance(codefile, str):
        return codefile

    try:
        pthDir = None
        pthDir, pthFile = os.path.split(codefile)
        if pthDir:
            sys.path.insert(0, pthDir)
        fName, fExt = os.path.splitext(pthFile)
        mod = importlib.import_module(fName)
        if reload:
            importlib.reload(mod)
    finally:
        if pthDir:
            sys.path.pop(0)
    return mod


def dy_load_module_attr(modfile, search_attrs = None, reload = False):
    ''' 动态加载 mod 里的属性
    :param modfile: 输入模块名字,可以是内置模块,也可以py文件
    :param search_attrs:  搜索相应的属性,支持 列表/字符串
    :param reload: 是否需要 reload
    :return:
    '''
    if not isinstance(modfile, str):
        return modfile

    try:
        #搜索是否存在路径
        pthDir = None
        if modfile.find('/') != -1 or modfile.find('\\') != -1:
            pthDir, pthFile = os.path.split(modfile)
        else:
            pthFile = modfile

        #插入路径
        if pthDir:
            sys.path.insert(0, pthDir)

        #读取模块名字
        module_str, _ = os.path.splitext(pthFile)

        #动态导入模块
        mod = importlib.import_module(module_str)
        if reload:
            importlib.reload(mod)
        #加载属性名字
        instance = mod
        if isinstance(search_attrs, str):
            # 搜索 属性
            for attr_str in search_attrs.split("."):
                instance = getattr(instance, attr_str)

        elif isinstance(search_attrs, (list, tuple) ):
            # 搜索列表中某一个属性
            for attrs in search_attrs:
                attr_list = attrs.split(".")
                if hasattr(instance, attr_list[0]): #如果搜索到 attr1.attr2.…… 级联模式
                    for attr_str in attr_list:
                        instance = getattr(instance, attr_str)
                    break

        return instance
    finally:
        #删除路径
        if pthDir:
            sys.path.pop(0)