#   coding: utf-8
#   This file is part of DancingCell.

#   DancingCell is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/06/22"


import unittest
import numpy as np
from dancingcell.utility.dcjson import array2d


class TestArray2d(unittest.TestCase):

    def setUp(self):
        self.positions = array2d(np.random.randn(4,3))

    def test_atom(self):
        a = self.positions.append([1, 2, 3])
        print(a.data)
        print(a.x)
        print(a.y)
        print(a.as_dict())
        print(a.to_json())
        print(len(a))
        print(a[2])

    def test_json(self):
        tmp_str = self.positions.to_json()
        print(tmp_str)
        tt = self.positions.from_json(tmp_str)
        print(tt)


if __name__ == '__main__':
    unittest.main()
