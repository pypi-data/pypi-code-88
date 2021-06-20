#   coding: utf-8
#   This file is part of DancingCell.

#   DancingCell is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/06/24"

import unittest
from dancingcell.vasp.xsf import Xsf
import numpy as np
from dancingcell.core.cell import Cell
from dancingcell.utility.dcjson import array2d


class TestXsf(unittest.TestCase):

    def setUp(self):
        with open('4163.xsf', 'r') as f:
            a = ''.join(f.readlines())
        self.xsf = Xsf.from_str(a, labels='4163.xsf')

    def test_get_str(self):
        # print(self.stttt)
        cell = self.xsf.cell
        # print(cell.as_dict())

    def test_to_str(self):
        a = self.xsf.to_string()
        print(a)

if __name__ == '__main__':
    unittest.main()