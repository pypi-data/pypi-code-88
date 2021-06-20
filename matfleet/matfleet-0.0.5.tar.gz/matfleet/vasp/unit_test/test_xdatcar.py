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
from dancingcell.vasp.xdatcar import XDATCAR
import numpy as np

from dancingcell.core.cell import Cell
from dancingcell.utility.dcjson import array2d


class TestXdatcar(unittest.TestCase):

    def setUp(self):
        np.random.seed(1)
        positions = array2d(np.random.randn(4, 3))
        forces = array2d(np.random.randn(4, 3))
        energies = np.random.random(4)
        species = ['Sb'] * 1 + ['Te'] * 3
        lattice = np.random.randn(3, 3)

        self.cell = Cell(positions, species, forces=forces, energies=energies, lattice=lattice, labels='sdfsdfsd')
        # self.atom = Poscar(self.cell, comment='111')
        # self.stttt = self.atom.get_string()
        with open('XDATCAR', 'r') as f:
            content = ''.join(f.readlines())

        self.xdatcar = XDATCAR.from_str(content)

    def test_from_str(self):
        print('--------1-------------')
        print(self.xdatcar)
        print(self.xdatcar._index)
        print(self.xdatcar.natoms)

    def test_to_str(self):
        lines = self.xdatcar.to_str('1, 3, 2', have_head_info=False, set_all_num=[8, 10])
        # print(lines)

    def test_xdatcar(self):
        all_cells = {i:self.cell for i in range(3)}
        xdatcar = XDATCAR(cells=all_cells, natoms=self.cell.atom_numbers)
        print('---------2-------------')
        print(xdatcar.to_str())

    def test_todb(self):
        update_dic = {}
        for i in list(self.xdatcar.all_cell.keys()):
            update_dic[i] = i + 100
        self.xdatcar.update_key(update_dic)
        self.xdatcar.to_db(xdatcar_labels='test1sbte', need_init=False, update_label=True)

        # self.xdatcar.to_db(xdatcar_labels='test1sbte', need_init=False, update_label=False)
        # self.xdatcar.to_db(xdatcar_labels='test2sbte', need_init=False, update_label=False)



if __name__ == '__main__':
    unittest.main()