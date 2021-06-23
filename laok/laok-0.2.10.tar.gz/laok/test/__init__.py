#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2020/6/4 14:41:10

@author: LiuKuan
@copyright: Apache License, Version 2.0
'''
from .dump_description import dump_description_help
from .lktest_runner import lktest_run
from pprint import pprint
import sys as _sys
#===============================================================================
# 
#===============================================================================

def print_eval(st):
    _frm = _sys._getframe(1)
    print( "{} [:] {}".format(st, eval(st, _frm.f_globals, _frm.f_locals)) )

def print_type(t):
    import inspect
    type_name = None
    if inspect.ismodule(t):
        type_name = 'ismodule'
    if inspect.isclass(t):
        type_name = "isclass"
    if inspect.ismethod(t):
        type_name = "ismethod"
    if inspect.isfunction(t):
        type_name = "isfunction"
    if inspect.isgeneratorfunction(t):
        type_name = "isgeneratorfunction"
    if inspect.isgenerator(t):
        type_name = "isgenerator"
    if inspect.iscoroutinefunction(t):
        type_name = "iscoroutinefunction"
    if inspect.iscoroutine(t):
        type_name = "iscoroutine"
    if inspect.isawaitable(t):
        type_name = "isawaitable"
    if inspect.isasyncgenfunction(t):
        type_name = "isasyncgenfunction"
    if inspect.isasyncgen(t):
        type_name = "isasyncgen"
    if inspect.istraceback(t):
        type_name = "istraceback"
    if inspect.isframe(t):
        type_name = "isframe"
    if inspect.iscode(t):
        type_name = "iscode"
    if inspect.isbuiltin(t):
        type_name = "isbuiltin"
    if inspect.isroutine(t):
        type_name = "isroutine"
    if inspect.isabstract(t):
        type_name = "isabstract"
    if inspect.ismethoddescriptor(t):
        type_name = "ismethoddescriptor"
    if inspect.isdatadescriptor(t):
        type_name = "isdatadescriptor"
    if inspect.isgetsetdescriptor(t):
        type_name = "isgetsetdescriptor"
    if inspect.ismemberdescriptor(t):
        type_name = "ismemberdescriptor"
    if type_name is None:
        type_name = f"{type(t)}"
    print(type_name)


def simple_description(obj):
    for i in dir(obj):
        if not i.startswith('_'):
            attr = getattr(obj,i)
            print(f"{i}={attr}")
