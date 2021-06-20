#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/01/14 18:35:22'

import json


class MatFleetJson(object):
    
    @classmethod
    def load_file(cls, filename, encoding='utf-8'):
        with open(filename, 'r', encoding=encoding) as f:
            return json.load(f)
    
    @classmethod
    def dumps(cls, *args, **kwargs):
        return json.dumps(*args, **kwargs)
    
    @classmethod
    def dump(cls, *args, **kwargs):
        return json.dump(*args, **kwargs)
    
    @classmethod
    def load(cls, *args, **kwargs):
        return json.load(*args, **kwargs)
    
    @classmethod
    def loads(cls, *args, **kwargs):
        return json.loads(*args, **kwargs)

