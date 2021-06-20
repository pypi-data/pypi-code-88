
#   coding: utf-8
#   This file is part of DancingCell.

#   DancingCell is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/06/19"

class Poscar():
    """
    Object for representing the data in a POSCAR or CONTCAR file.
    Please note that this current implementation. Most attributes can be set
    directly.

    .. attribute:: structure

        Associated Structure.

    .. attribute:: comment

        Optional comment string.

    .. attribute:: true_names

        Boolean indication whether Poscar contains actual real names parsed
        from either a POTCAR or the POSCAR itself.

    .. attribute:: selective_dynamics

        Selective dynamics attribute for each site if available. A Nx3 array of
        booleans.

    .. attribute:: velocities

        Velocities for each site (typically read in from a CONTCAR). A Nx3
        array of floats.

    .. attribute:: predictor_corrector

        Predictor corrector coordinates and derivatives for each site; i.e.
        a list of three 1x3 arrays for each site (typically read in from a MD
        CONTCAR).

    .. attribute:: predictor_corrector_preamble

        Predictor corrector preamble contains the predictor-corrector key,
        POTIM, and thermostat parameters that precede the site-specic predictor
        corrector data in MD CONTCAR

    .. attribute:: temperature

        Temperature of velocity Maxwell-Boltzmann initialization. Initialized
        to -1 (MB hasn"t been performed).
    """

    def __init__(
        self,
        structure: Structure,
        comment: str = None,
        selective_dynamics=None,
        true_names: bool = True,
        velocities=None,
        predictor_corrector=None,
        predictor_corrector_preamble=None,
        sort_structure: bool = False,
    ):
        """

        :param structure: Structure object.
        :param comment: Optional comment line for POSCAR. Defaults to unit
            cell formula of structure. Defaults to None.
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
        :param sort_structure: Whether to sort structure. Useful if species
            are not grouped properly together.
        """
        if structure.is_ordered:
            site_properties = {}
            if selective_dynamics:
                site_properties["selective_dynamics"] = selective_dynamics
            if velocities:
                site_properties["velocities"] = velocities
            if predictor_corrector:
                site_properties["predictor_corrector"] = predictor_corrector
            structure = Structure.from_sites(structure)
            self.structure = structure.copy(site_properties=site_properties)
            if sort_structure:
                self.structure = self.structure.get_sorted_structure()
            self.true_names = true_names
            self.comment = structure.formula if comment is None else comment
            self.predictor_corrector_preamble = predictor_corrector_preamble
        else:
            raise ValueError(
                "Structure with partial occupancies cannot be " "converted into POSCAR!"
            )

        self.temperature = -1

    @property
    def velocities(self):
        """Velocities in Poscar"""
        return self.structure.site_properties.get("velocities")

    @property
    def selective_dynamics(self):
        """Selective dynamics in Poscar"""
        return self.structure.site_properties.get("selective_dynamics")

    @property
    def predictor_corrector(self):
        """Predictor corrector in Poscar"""
        return self.structure.site_properties.get("predictor_corrector")

    @velocities.setter  # type: ignore
    def velocities(self, velocities):
        """Setter for Poscar.velocities"""
        self.structure.add_site_property("velocities", velocities)

    @selective_dynamics.setter  # type: ignore
    def selective_dynamics(self, selective_dynamics):
        """Setter for Poscar.selective_dynamics"""
        self.structure.add_site_property("selective_dynamics", selective_dynamics)

    @predictor_corrector.setter  # type: ignore
    def predictor_corrector(self, predictor_corrector):
        """Setter for Poscar.predictor_corrector"""
        self.structure.add_site_property("predictor_corrector", predictor_corrector)

    @property
    def site_symbols(self):
        """
        Sequence of symbols associated with the Poscar. Similar to 6th line in
        vasp 5+ POSCAR.
        """
        syms = [site.specie.symbol for site in self.structure]
        return [a[0] for a in itertools.groupby(syms)]

    @property
    def natoms(self):
        """
        Sequence of number of sites of each type associated with the Poscar.
        Similar to 7th line in vasp 5+ POSCAR or the 6th line in vasp 4 POSCAR.
        """
        syms = [site.specie.symbol for site in self.structure]
        return [len(tuple(a[1])) for a in itertools.groupby(syms)]

    def __setattr__(self, name, value):
        if name in ("selective_dynamics", "velocities"):
            if value is not None and len(value) > 0:
                value = np.array(value)
                dim = value.shape
                if dim[1] != 3 or dim[0] != len(self.structure):
                    raise ValueError(
                        name + " array must be same length as" + " the structure."
                    )
                value = value.tolist()
        super().__setattr__(name, value)

    @staticmethod
    def from_file(filename, check_for_POTCAR=True, read_velocities=True):
        """
        Reads a Poscar from a file.

        The code will try its best to determine the elements in the POSCAR in
        the following order:

        1. If check_for_POTCAR is True, the code will try to check if a POTCAR
        is in the same directory as the POSCAR and use elements from that by
        default. (This is the VASP default sequence of priority).
        2. If the input file is Vasp5-like and contains element symbols in the
        6th line, the code will use that if check_for_POTCAR is False or there
        is no POTCAR found.
        3. Failing (2), the code will check if a symbol is provided at the end
        of each coordinate.

        If all else fails, the code will just assign the first n elements in
        increasing atomic number, where n is the number of species, to the
        Poscar. For example, H, He, Li, ....  This will ensure at least a
        unique element is assigned to each site and any analysis that does not
        require specific elemental properties should work fine.

        Args:
            filename (str): File name containing Poscar data.
            check_for_POTCAR (bool): Whether to check if a POTCAR is present
                in the same directory as the POSCAR. Defaults to True.
            read_velocities (bool): Whether to read or not velocities if they
                are present in the POSCAR. Default is True.

        Returns:
            Poscar object.
        """
        dirname = os.path.dirname(os.path.abspath(filename))
        names = None
        if check_for_POTCAR:
            potcars = glob.glob(os.path.join(dirname, "*POTCAR*"))
            if potcars:
                try:
                    potcar = Potcar.from_file(sorted(potcars)[0])
                    names = [sym.split("_")[0] for sym in potcar.symbols]
                    [get_el_sp(n) for n in names]  # ensure valid names
                except Exception:
                    names = None
        with zopen(filename, "rt") as f:
            return Poscar.from_string(f.read(), names, read_velocities=read_velocities)

    @staticmethod
    def from_string(data, default_names=None, read_velocities=True):
        """
        Reads a Poscar from a string.

        The code will try its best to determine the elements in the POSCAR in
        the following order:

        1. If default_names are supplied and valid, it will use those. Usually,
        default names comes from an external source, such as a POTCAR in the
        same directory.

        2. If there are no valid default names but the input file is Vasp5-like
        and contains element symbols in the 6th line, the code will use that.

        3. Failing (2), the code will check if a symbol is provided at the end
        of each coordinate.

        If all else fails, the code will just assign the first n elements in
        increasing atomic number, where n is the number of species, to the
        Poscar. For example, H, He, Li, ....  This will ensure at least a
        unique element is assigned to each site and any analysis that does not
        require specific elemental properties should work fine.

        Args:
            data (str): String containing Poscar data.
            default_names ([str]): Default symbols for the POSCAR file,
                usually coming from a POTCAR in the same directory.
            read_velocities (bool): Whether to read or not velocities if they
                are present in the POSCAR. Default is True.

        Returns:
            Poscar object.
        """
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
        comment = lines[0]
        scale = float(lines[1])
        lattice = np.array([[float(i) for i in line.split()] for line in lines[2:5]])
        if scale < 0:
            # In vasp, a negative scale factor is treated as a volume. We need
            # to translate this to a proper lattice vector scaling.
            vol = abs(det(lattice))
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

        struct = Structure(
            lattice,
            atomic_symbols,
            coords,
            to_unit_cell=False,
            validate_proximity=False,
            coords_are_cartesian=cart,
        )

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

    def get_string(self, direct=True, vasp4_compatible=False, significant_figures=6):
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
        latt = self.structure.lattice
        if np.linalg.det(latt.matrix) < 0:
            latt = Lattice(-latt.matrix)

        format_str = "{{:.{0}f}}".format(significant_figures)
        lines = [self.comment, "1.0"]
        for v in latt.matrix:
            lines.append(" ".join([format_str.format(c) for c in v]))

        if self.true_names and not vasp4_compatible:
            lines.append(" ".join(self.site_symbols))
        lines.append(" ".join([str(x) for x in self.natoms]))
        if self.selective_dynamics:
            lines.append("Selective dynamics")
        lines.append("direct" if direct else "cartesian")

        selective_dynamics = self.selective_dynamics
        for (i, site) in enumerate(self.structure):
            coords = site.frac_coords if direct else site.coords
            line = " ".join([format_str.format(c) for c in coords])
            if selective_dynamics is not None:
                sd = ["T" if j else "F" for j in selective_dynamics[i]]
                line += " %s %s %s" % (sd[0], sd[1], sd[2])
            line += " " + site.species_string
            lines.append(line)

        if self.velocities:
            try:
                lines.append("")
                for v in self.velocities:
                    lines.append(" ".join([format_str.format(i) for i in v]))
            except Exception:
                warnings.warn("Velocities are missing or corrupted.")

        if self.predictor_corrector:
            lines.append("")
            if self.predictor_corrector_preamble:
                lines.append(self.predictor_corrector_preamble)
                pred = np.array(self.predictor_corrector)
                for col in range(3):
                    for z in pred[:, col]:
                        lines.append(" ".join([format_str.format(i) for i in z]))
            else:
                warnings.warn(
                    "Preamble information missing or corrupt. "
                    "Writing Poscar with no predictor corrector data."
                )

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
        with zopen(filename, "wt") as f:
            f.write(self.get_string(**kwargs))

    def as_dict(self):
        """
        :return: MSONable dict.
        """
        return {
            "@module": self.__class__.__module__,
            "@class": self.__class__.__name__,
            "structure": self.structure.as_dict(),
            "true_names": self.true_names,
            "selective_dynamics": np.array(self.selective_dynamics).tolist(),
            "velocities": self.velocities,
            "predictor_corrector": self.predictor_corrector,
            "comment": self.comment,
        }

    @classmethod
    def from_dict(cls, d):
        """
        :param d: Dict representation.
        :return: Poscar
        """
        return Poscar(
            Structure.from_dict(d["structure"]),
            comment=d["comment"],
            selective_dynamics=d["selective_dynamics"],
            true_names=d["true_names"],
            velocities=d.get("velocities", None),
            predictor_corrector=d.get("predictor_corrector", None),
        )

    def set_temperature(self, temperature):
        """
        Initializes the velocities based on Maxwell-Boltzmann distribution.
        Removes linear, but not angular drift (same as VASP)

        Scales the energies to the exact temperature (microcanonical ensemble)
        Velocities are given in A/fs. This is the vasp default when
        direct/cartesian is not specified (even when positions are given in
        direct coordinates)

        Overwrites imported velocities, if any.

        Args:
            temperature (float): Temperature in Kelvin.
        """
        # mean 0 variance 1
        velocities = np.random.randn(len(self.structure), 3)

        # in AMU, (N,1) array
        atomic_masses = np.array(
            [site.specie.atomic_mass.to("kg") for site in self.structure]
        )
        dof = 3 * len(self.structure) - 3

        # scale velocities due to atomic masses
        # mean 0 std proportional to sqrt(1/m)
        velocities /= atomic_masses[:, np.newaxis] ** (1 / 2)

        # remove linear drift (net momentum)
        velocities -= np.average(
            atomic_masses[:, np.newaxis] * velocities, axis=0
        ) / np.average(atomic_masses)

        # scale velocities to get correct temperature
        energy = np.sum(1 / 2 * atomic_masses * np.sum(velocities ** 2, axis=1))
        scale = (temperature * dof / (2 * energy / const.k)) ** (1 / 2)

        velocities *= scale * 1e-5  # these are in A/fs

        self.temperature = temperature
        try:
            del self.structure.site_properties["selective_dynamics"]
        except KeyError:
            pass

        try:
            del self.structure.site_properties["predictor_corrector"]
        except KeyError:
            pass
        # returns as a list of lists to be consistent with the other
        # initializations

        self.structure.add_site_property("velocities", velocities.tolist())

