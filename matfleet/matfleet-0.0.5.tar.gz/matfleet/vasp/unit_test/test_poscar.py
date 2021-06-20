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
from dancingcell.vasp.poscar import Poscar
import numpy as np
from dancingcell.core.cell import Cell
from dancingcell.utility.dcjson import array2d


class TestPoscar(unittest.TestCase):

    def setUp(self):
        np.random.seed(1)
        positions = array2d(np.random.randn(4, 3))
        forces = array2d(np.random.randn(4, 3))
        energies = np.random.random(4)
        species = ['Sb'] * 1 + ['Te'] * 3
        lattice = np.random.randn(3, 3)

        self.cell = Cell(positions, species, forces=forces, energies=energies, lattice=lattice, labels='sdfsdfsd')
        self.atom = Poscar(self.cell, comment='111')
        self.stttt = self.atom.get_string()

    def test_get_str(self):
        # print(self.stttt)
        pass

    def test_from_str(self):
        print('--------1-------------')
        pos = Poscar.from_str(self.stttt)
        print(pos.get_string(direct=True, each_line_symbol=False))
        # print(pos.cell.as_dict())

    def test_fromfile(self):
        print('--------2-------------')
        pos = Poscar.from_file('CONTCAR', comment='fififififif')
        # print(pos)
        # print(pos.cell.labels)
        # ttt = pos.cell.symbols
        # ttt.append('Sb')
        # print(ttt)
        # import itertools
        # for a in itertools.groupby(ttt):
        #     print(list(a), list(a[1]))
        # [len(tuple(a[1])) for a in itertools.groupby(syms)]

if __name__ == '__main__':
    unittest.main()