#   coding: utf-8
#   This file is part of DancingCell.

#   DancingCell is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/06/19"

from dancingcell.utility.dcjson import DcJson, jsanitize

def recursive_as_dict(obj):
    if isinstance(obj, (list, tuple)):
        return [recursive_as_dict(it) for it in obj]
    if isinstance(obj, dict):
        return {kk: recursive_as_dict(vv) for kk, vv in obj.items()}
    if hasattr(obj, "as_dict"):
        return obj.as_dict()
    return obj

class aaa(DcJson):
    def __init__(self, a, b):
        self.c = [[1, 2, 3], [2, 3, [4, 5]]]
        self.b = b
        self.a = a

    def as_dict(self):
        return {i:self.a[i] for i in range(len(self.a))}

if __name__ == '__main__':
    ccc = {'a':[[1, 2, 3], [2, 3, [4, 5]]], 'b': [2, 3, [4, 5]]}
    # b = recursive_as_dict([1, aaa()])
    # print(b)
    b = aaa.from_dict(ccc)
    print(b.to_json())
    # print(b.unsafe_hash())
    # a = jsanitize(1, strict=True)
    # print(type(a))