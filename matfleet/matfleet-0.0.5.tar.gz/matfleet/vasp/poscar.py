#   coding: utf-8
#   This file is part of DancingCell.

#   DancingCell is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/06/19"

import re
import numpy as np
import warnings

from dancingcell.utility.io_file import clean_lines
from dancingcell.core.element import Element
from dancingcell.core.cell import Cell
from dancingcell.utility.dcjson import array2d
from dancingcell.utility.io_file import gopen
from dancingcell.core.lattice import Lattice


class Poscar():

    def __init__(
        self,
        cell: Cell,
        comment: str = None,
        selective_dynamics=None,
        true_names: bool = True,
        velocities=None,
        predictor_corrector=None,
        predictor_corrector_preamble=None,
        sort_structure: bool = False,
    ):
        """

        :param cell: Structure object.
        :param comment: Optional comment line for POSCAR. Defaults to unit
            cell formula of cell. Defaults to None.
        :param selective_dynamics: bool values for selective dynamics,
            where N is number of sites. Defaults to None.
        :param true_names: Set to False if the names in the POSCAR are not
            well-defined and ambiguous. This situation arises commonly in
            vasp < 5 where the POSCAR sometimes does not contain element
            symbols. Defaults to True.
        :param velocities: Velocities for the POSCAR. Typically parsed
            in MD runs or can be used to initialize velocities.
        :param predictor_corrector: Predictor corrector for the POSCAR.
            Typically parsed in MD runs.
        :param predictor_corrector_preamble: Preamble to the predictor
            corrector.
        :param sort_structure: Whether to sort cell. Useful if species
            are not grouped properly together.
        """
        assert isinstance(cell, Cell)
        self.cell = cell
        if not self.cell.is_ordered:
            raise ValueError("Can't relize atom occupy != 1 ")

        site_properties = {}
        if selective_dynamics:
            site_properties["selective_dynamics"] = selective_dynamics
        if velocities:
            site_properties["velocities"] = velocities
        if predictor_corrector:
            site_properties["predictor_corrector"] = predictor_corrector

        self.true_names = true_names
        self.comment = cell.formula if comment is None else comment
        self.predictor_corrector_preamble = predictor_corrector_preamble

        self.temperature = -1

    @property
    def natoms(self):
        return self.cell.natoms_split_by_symbol

    @staticmethod
    def from_str(data, comment=None, default_names=None, read_velocities=True):

        # "^\s*$" doesn't match lines with no whitespace
        chunks = re.split(r"\n\s*\n", data.rstrip(), flags=re.MULTILINE)
        try:
            if chunks[0] == "":
                chunks.pop(0)
                chunks[0] = "\n" + chunks[0]
        except IndexError:
            raise ValueError("Empty POSCAR")

        # Parse positions
        lines = tuple(clean_lines(chunks[0].split("\n"), False))
        comment = comment if comment else lines[0]
        scale = float(lines[1])
        lattice = np.array([[float(i) for i in line.split()] for line in lines[2:5]])
        if scale < 0:
            # In vasp, a negative scale factor is treated as a volume. We need
            # to translate this to a proper lattice vector scaling.
            vol = abs(np.linalg.det(lattice))
            lattice *= (-scale / vol) ** (1 / 3)
        else:
            lattice *= scale

        vasp5_symbols = False
        try:
            natoms = [int(i) for i in lines[5].split()]
            ipos = 6
        except ValueError:
            vasp5_symbols = True
            symbols = lines[5].split()

            """
            Atoms and number of atoms in POSCAR written with vasp appear on
            multiple lines when atoms of the same type are not grouped together
            and more than 20 groups are then defined ...
            Example :
            Cr16 Fe35 Ni2
               1.00000000000000
                 8.5415010000000002   -0.0077670000000000   -0.0007960000000000
                -0.0077730000000000    8.5224019999999996    0.0105580000000000
                -0.0007970000000000    0.0105720000000000    8.5356889999999996
               Fe   Cr   Fe   Cr   Fe   Cr   Fe   Cr   Fe   Cr   Fe   Cr   Fe   Cr   Fe   Ni   Fe   Cr   Fe   Cr
               Fe   Ni   Fe   Cr   Fe
                 1   1   2   4   2   1   1   1     2     1     1     1     4     1     1     1     5     3     6     1
                 2   1   3   2   5
            Direct
              ...
            """
            nlines_symbols = 1
            for nlines_symbols in range(1, 11):
                try:
                    int(lines[5 + nlines_symbols].split()[0])
                    break
                except ValueError:
                    pass
            for iline_symbols in range(6, 5 + nlines_symbols):
                symbols.extend(lines[iline_symbols].split())
            natoms = []
            iline_natoms_start = 5 + nlines_symbols
            for iline_natoms in range(
                    iline_natoms_start, iline_natoms_start + nlines_symbols
            ):
                natoms.extend([int(i) for i in lines[iline_natoms].split()])
            atomic_symbols = list()
            for i in range(len(natoms)):
                atomic_symbols.extend([symbols[i]] * natoms[i])
            ipos = 5 + 2 * nlines_symbols

        postype = lines[ipos].split()[0]

        sdynamics = False
        # Selective dynamics
        if postype[0] in "sS":
            sdynamics = True
            ipos += 1
            postype = lines[ipos].split()[0]

        cart = postype[0] in "cCkK"
        nsites = sum(natoms)

        # If default_names is specified (usually coming from a POTCAR), use
        # them. This is in line with Vasp"s parsing order that the POTCAR
        # specified is the default used.
        if default_names:
            try:
                atomic_symbols = []
                for i in range(len(natoms)):
                    atomic_symbols.extend([default_names[i]] * natoms[i])
                vasp5_symbols = True
            except IndexError:
                pass

        if not vasp5_symbols:
            ind = 3 if not sdynamics else 6
            try:
                # Check if names are appended at the end of the coordinates.
                atomic_symbols = [
                    l.split()[ind] for l in lines[ipos + 1: ipos + 1 + nsites]
                ]
                # Ensure symbols are valid elements
                if not all([Element.is_valid_symbol(sym) for sym in atomic_symbols]):
                    raise ValueError("Non-valid symbols detected.")
                vasp5_symbols = True
            except (ValueError, IndexError):
                # Defaulting to false names.
                atomic_symbols = []
                for i in range(len(natoms)):
                    sym = Element.from_Z(i + 1).symbol
                    atomic_symbols.extend([sym] * natoms[i])
                warnings.warn(
                    "Elements in POSCAR cannot be determined. "
                    "Defaulting to false names %s." % " ".join(atomic_symbols)
                )

        # read the atomic coordinates
        coords = []
        selective_dynamics = list() if sdynamics else None
        for i in range(nsites):
            toks = lines[ipos + 1 + i].split()
            crd_scale = scale if cart else 1
            coords.append([float(j) * crd_scale for j in toks[:3]])
            if sdynamics:
                selective_dynamics.append([tok.upper()[0] == "T" for tok in toks[3:6]])
        struct = Cell(positions=array2d(coords),
                      species=atomic_symbols,
                      lattice=lattice,
                      coords_are_cartesian=cart,
                      labels=comment)

        if read_velocities:
            # Parse velocities if any
            velocities = []
            if len(chunks) > 1:
                for line in chunks[1].strip().split("\n"):
                    velocities.append([float(tok) for tok in line.split()])

            # Parse the predictor-corrector data
            predictor_corrector = []
            predictor_corrector_preamble = None

            if len(chunks) > 2:
                lines = chunks[2].strip().split("\n")
                # There are 3 sets of 3xN Predictor corrector parameters
                # So can't be stored as a single set of "site_property"

                # First line in chunk is a key in CONTCAR
                # Second line is POTIM
                # Third line is the thermostat parameters
                predictor_corrector_preamble = (
                    lines[0] + "\n" + lines[1] + "\n" + lines[2]
                )
                # Rest is three sets of parameters, each set contains
                # x, y, z predictor-corrector parameters for every atom in orde
                lines = lines[3:]
                for st in range(nsites):
                    d1 = [float(tok) for tok in lines[st].split()]
                    d2 = [float(tok) for tok in lines[st + nsites].split()]
                    d3 = [float(tok) for tok in lines[st + 2 * nsites].split()]
                    predictor_corrector.append([d1, d2, d3])
        else:
            velocities = None
            predictor_corrector = None
            predictor_corrector_preamble = None

        return Poscar(
            struct,
            comment,
            selective_dynamics,
            vasp5_symbols,
            velocities=velocities,
            predictor_corrector=predictor_corrector,
            predictor_corrector_preamble=predictor_corrector_preamble,
        )

    @staticmethod
    def from_file(filename, comment=None, read_velocities=True):
        """
        Reads a Poscar from a file.

        Args:
            filename (str): File name containing Poscar data.
            comment(str): cell.labels
            check_for_POTCAR (bool): Whether to check if a POTCAR is present
                in the same directory as the POSCAR. Defaults to True.
            read_velocities (bool): Whether to read or not velocities if they
                are present in the POSCAR. Default is True.

        Returns:
            Poscar object.
        """
        with gopen(filename, "rt") as f:
            return Poscar.from_str(f.read(), comment=comment, default_names=None,
                                   read_velocities=read_velocities)

    def get_string(self, direct=True, significant_figures=6, each_line_symbol=False):
        """
        Returns a string to be written as a POSCAR file. By default, site
        symbols are written, which means compatibility is for vasp >= 5.

        Args:
            direct (bool): Whether coordinates are output in direct or
                cartesian. Defaults to True.
            vasp4_compatible (bool): Set to True to omit site symbols on 6th
                line to maintain backward vasp 4.x compatibility. Defaults
                to False.
            significant_figures (int): No. of significant figures to
                output all quantities. Defaults to 6. Note that positions are
                output in fixed point, while velocities are output in
                scientific format.

        Returns:
            String representation of POSCAR.
        """

        # This corrects for VASP really annoying bug of crashing on lattices
        # which have triple product < 0. We will just invert the lattice
        # vectors.
        latt = self.cell.lattice
        if np.linalg.det(latt.matrix) < 0:
            latt = Lattice(-latt.matrix)

        format_str = "{{:.{0}f}}".format(significant_figures)
        lines = [self.comment, "1.0"]
        for v in latt.matrix:
            lines.append(" ".join([format_str.format(c) for c in v]))

        if not each_line_symbol:
            lines.append(" ".join([x[0] for x in self.cell.species_and_accord_numbers()]))

        lines.append(" ".join([str(x) for x in self.natoms]))

        lines.append("direct" if direct else "cartesian")

        for (i, site) in enumerate(self.cell):
            coords = site.frac_coords if direct else site.coords
            line = '    ' + " ".join([format_str.format(c) for c in coords])
            if each_line_symbol:
                line += " " + site.get('symbol')
            lines.append(line)

        return "\n".join(lines) + "\n"

    def __repr__(self):
        return self.get_string()

    def __str__(self):
        """
        String representation of Poscar file.
        """
        return self.get_string()

    def write_file(self, filename, **kwargs):
        """
        Writes POSCAR to a file. The supported kwargs are the same as those for
        the Poscar.get_string method and are passed through directly.
        """
        with gopen(filename, "wt") as f:
            f.write(self.get_string(**kwargs))

    def as_dict(self):
        """
        :return: MSONable dict.
        """
        d = self.cell.as_dict()
        d['*mod'] = self.__class__.__module__
        d['*clas'] = self.__class__.__name__
        d['true_names'] = self.true_names
        d['comment'] = self.comment
        d['format'] = 'poscar'
        return d



