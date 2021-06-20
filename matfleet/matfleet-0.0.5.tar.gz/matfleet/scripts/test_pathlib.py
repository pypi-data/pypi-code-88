#   coding:utf-8
#   This file is part of DancingCell.
#
#   DancingCell is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = " 09/04/2019"

import pathlib as pt

a = pt.Path('.')
for i in a.iterdir():
    print(i)

print(list(a.glob('*.txt')))

c = pt.Path('base.py')
# / 拼接路径
_ = c / 'fsdfs'
print(_.exists())
with c.open(encoding='UTF8') as f:
    print(f.readline())

_ = pt.PureWindowsPath('base.py')
print(_)

# print(pt.Path('base.py').absolute())
print(pt.Path(_).absolute())