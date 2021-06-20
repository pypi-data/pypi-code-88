#   coding: utf-8
#   This file is part of DancingCell.

#   DancingCell is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/06/24"

import re
import  numpy as np

from dancingcell.utility.io_file import clean_lines
from dancingcell.core.lattice import Lattice
from dancingcell.core.cellsite import CellSite
from dancingcell.core.cell import Cell

class Xsf:
    """class Xsf to read info from file defined in .Xsf format.

    Attributes:
        cell: Cell
    """

    def __init__(self, cell: Cell):
        self.cell = cell

    def to_string(self):
        """
        Returns a string with the structure in XSF format
        See http://www.xcrysden.org/doc/XSF.html
        """
        content = list([])
        content.append("#total energy = %.8f eV" % self.cell.total_energy)
        content.append("")
        content.append("CRYSTAL")
        content.append("# Primitive lattice vectors in Angstrom")
        content.append("PRIMVEC")
        cell = self.cell.lattice.matrix
        for i in range(3):
            content.append(' %12.8f %12.8f %12.8f' % tuple(cell[i]))

        cart_coords = self.cell.cartesian.data
        forces = self.cell.forces.data
        content.append("# Cartesian coordinates in Angstrom.")
        content.append("PRIMCOORD")
        content.append(" %d 1" % len(cart_coords))

        for a in range(len(cart_coords)):
            sp = "%s" % self.cell.symbols[a]
            content.append(sp + ' %12.6f %12.6f %12.6f' % tuple(cart_coords[a]) +
                         ' %12.6f %12.6f %12.6f' % tuple(forces[a]))

        return "\n".join(content)

    @classmethod
    def from_str(cls, xsf_content, labels=None):
        line = xsf_content.split('\n')

        _pattern_total_energy = re.compile('#total energy =(.*) eV')
        _pattern_primvec = re.compile("PRIMVEC")
        _pattern_primcoord = re.compile("PRIMCOORD")

        etot = 0
        pbc = [True] * 3
        lattice = np.zeros((3, 3))

        for i in range(len(line)):

            if _pattern_total_energy.search(line[i]):
                _te = _pattern_total_energy.search(line[i])
                etot = float(_te.group(1))

            if _pattern_primvec.search(line[i]):
                pbc = [True] * 3
                # print([[float(m) for m in x.replace().split()]
                #                    for x in line[i+1 : i+4]])
                # exit()
                lattice = Lattice([[float(m) for m in x.split()]
                                   for x in list(clean_lines(line[i+1 : i+4], remove_return=True))])

            if _pattern_primcoord.search(line[i]):
                natom = int(line[i+1].split()[0])
                atom_info = clean_lines(line[i+2 : i+2+natom])
                _eatom_ener = etot/natom

                cell = Cell.from_cellsite([CellSite.from_str(atom_info=i, cell=lattice,
                                                             atom_ene=_eatom_ener, is_frac=False)
                                           for i in atom_info], pbc=pbc)
                cell.labels = labels
                return cls(cell)

    def as_dict(self):
        d = self.cell.as_dict()
        d['format'] = 'xsf'
        return d
