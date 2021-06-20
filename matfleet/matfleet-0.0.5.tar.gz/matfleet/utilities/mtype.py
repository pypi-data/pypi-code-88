#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/01/14 21:28:53'

from collections import OrderedDict


def recursive_basic_type(obj):
    if isinstance(obj, dict):
        return {kk: recursive_basic_type(vv) for kk, vv in obj.items()}
    if isinstance(obj, OrderedDict):
        return OrderedDict({kk: recursive_basic_type(vv) for kk, vv in obj.items()})
    if isinstance(obj, (list or tuple)):
        return [recursive_basic_type(i) for i in obj]
    if isinstance(obj, (int, float)):
        return str(obj)
    if isinstance(obj, str):
        if obj.startswith('{') and obj.endswith('}'):
            return recursive_basic_type(eval(obj))
        if obj.startswith('[') and obj.endswith(']'):
            return recursive_basic_type(eval(obj))
        if obj.startswith('(') and obj.endswith(')'):
            return recursive_basic_type(eval(obj))
    return obj


class AlkDict(dict):
    
    def alkget(self, name, value):
        tmp = self.get(name, None)
        if tmp is not None:
            return tmp
        else:
            return value
        
        
if __name__ == '__main__':
    a = AlkDict({'a': None})
    print(a.alkget('a', 'sdfsdf'))
