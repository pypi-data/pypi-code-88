#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2020/6/4 18:13:09

@author: LiuKuan
@copyright: Apache License, Version 2.0
'''
import inspect, sys, contextlib, types
#===============================================================================
# 
#===============================================================================

__all__ = ['dump_description_help']

@contextlib.contextmanager
def _stdout_file(filename):
    org = sys.stdout
    try:
        with open(filename , 'w') as f:
            sys.stdout = f
            yield
    finally:
        sys.stdout = org


_obj = object()

def dump_description_help(obj, help_file=False, skip_object = True):
    if obj is None:
        print('None')
        return

    if help_file:
        with _stdout_file('help-%s.txt' % _get_name(obj) ):
            help(obj)

    allFunc = []
    allBuiltIn = []
    allAttr = []
    allClass = []
    allModules = []
    allWMethWrapper = []

    print('\n# -----', type(obj))

    for k,v in _get_attr_pair(obj):

        if k.startswith('_') and not k.startswith('__'):
            continue

        if skip_object and hasattr(_obj, k) and k != '__init__':
            continue

        if inspect.isroutine(v):
            if inspect.isbuiltin(v):
                if not k.startswith("_"):
                    allBuiltIn.append((k, v))
            elif isinstance(k, types.MethodWrapperType):
                if k == "__init__":
                    allWMethWrapper.insert(0, (k,v))
                else:
                    allWMethWrapper.append((k,v))
            else:
                allFunc.append((k,v))
        else:
            if inspect.isclass(v):
                allClass.append((k,v))
            elif inspect.ismodule(v):
                allModules.append((k,v))
            else:
                allAttr.append((k, v))

    if allModules:
        print('# module ---->')
        for k,v in allModules:
            print('\t# %s [%s]' %(k, _get_doc(v)) )

    if allClass:
        print('# class ---->')
        for k,v in allClass:
            print('\t# %s [%s]' %(k, _get_doc(v)) )

    if allAttr:
        print('# attr ---->')
        for k,v in allAttr:
            try:
                if k == '__builtins__':
                    print('\t#%s [%s]' %(k, _get_doc(v)) )
                else:
                    print('\t#%s[%s] [%s]' %(k, v, _get_doc(v)) )
            except Exception as e:
                print('\t#%s [%s]' % (k, _get_doc(v)))

    if allWMethWrapper:
        print('# methoid-wrapper ---->')
        for k,v in allWMethWrapper:
            try:
                print('\t#%s[%s] [%s]' %(k, v, _get_doc(v)) )
            except Exception as e:
                print('\t#%s [%s]' % (k, _get_doc(v)))

    if allBuiltIn:
        print('# builtin ---->')
        for k,v in allBuiltIn:
            print('\t# %s [%s]' %(k, _get_doc(v)) )

    if allFunc:
        print('# func ---->')
        for k,v in allFunc:
            print('\t# %s%s [%s]' %(k, _get_signature(v), _get_doc(v)) )

    print()


def _get_doc(v):
    if isinstance(v, str):
        return  '`str`'
    if isinstance(v, bytes):
        return  '`bytes`'
    elif isinstance(v, int):
        return  '`integer`'
    elif isinstance(v, dict):
        return  '`dict`'
    elif isinstance(v, set):
        return  '`set`'
    elif isinstance(v, frozenset):
        return '`fronzenset`'
    elif isinstance(v, float):
        return '`float`'
    elif isinstance(v, tuple):
        return '`tuple`'
    elif isinstance(v, list):
        return '`list`'

    try:
        doc = inspect.getdoc(v)
        return doc.replace('\n', ' ')[0:250]
    except Exception as e:
        return  ''

def _get_signature(v):
    try:
        return str(inspect.signature(v)).replace(', /', '')
    except:
        return "(...)"

def _get_name(v):
    try:
        name = v.__name__
    except Exception:
        try:
            name = v.__class__.__name__
        except Exception:
            name = 'none'
    return name


def _getmembers(object, predicate=None):
    """Return all members of an object as (name, value) pairs sorted by name.
    Optionally, only return members that satisfy a given predicate."""
    if inspect.isclass(object):
        mro = (object,) + inspect.getmro(object)
    else:
        mro = ()

    results = []
    processed = set()
    names = dir(object)

    try:
        for base in object.__bases__:
            for k, v in base.__dict__.items():
                if isinstance(v, types.DynamicClassAttribute):
                    names.append(k)
    except AttributeError:
        pass

    for key in names:
        try:
            value = getattr(object, key)
            # handle the duplicate key
            if key in processed:
                raise AttributeError
        except AttributeError:
            for base in mro:
                if key in base.__dict__:
                    value = base.__dict__[key]
                    break
            else:
                # could be a (currently) missing slot member, or a buggy
                # __dir__; discard and move on
                continue
        except Exception:
            pass

        if not predicate or predicate(value):
            results.append((key, value))
        processed.add(key)
    results.sort(key=lambda pair: pair[0])
    return results

def _get_attr_pair(obj):
    '''
    获取可能的属性列表
    '''
    datalist = []
    if hasattr(obj, '__all__'):
        for k in getattr(obj, '__all__'):
            if hasattr(obj, k):
                datalist.append( (k, getattr(obj, k)) )
        datalist.sort(key=lambda kv: kv[0])
    else:
        datalist = _getmembers(obj)
    return datalist
