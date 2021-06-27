# Copyright (c) 2021, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Provide a concrete molecule implementation that wraps ChemAxon."""


from __future__ import annotations

import logging
from typing import Optional

from ..abstract_molecule import AbstractMolecule
from . import ChemAxonError
from .chemaxon_manager import ChemAxonManager


NativeChemAxonMolecule = ChemAxonManager.get_instance().chemaxon.struc.Molecule


logger = logging.getLogger(__name__)


class ChemAxonMolecule(AbstractMolecule):
    """Define the RDKit molecule adapter."""

    _importer = ChemAxonManager.get_instance().chemaxon.formats.MolImporter
    _FormatError = ChemAxonManager.get_instance().chemaxon.formats.MolFormatException
    _exporter = ChemAxonManager.get_instance().chemaxon.formats.MolExporter
    _ExportError = ChemAxonManager.get_instance().chemaxon.marvin.io.MolExportException

    def __init__(self, *, molecule: NativeChemAxonMolecule, **kwargs):
        """Initialize the ChemAxonMolecule from a native instance."""
        super().__init__(molecule=molecule, **kwargs)

    @classmethod
    def from_mol_block(cls, mol: str) -> Optional[ChemAxonMolecule]:
        """Return an ChemAxonMolecule instance from an MDL MOL block."""
        return ChemAxonMolecule(molecule=cls._importer.importMol(mol, "mol"))

    @classmethod
    def from_inchi(cls, inchi: str) -> Optional[ChemAxonMolecule]:
        """Return an ChemAxonMolecule instance from an InChI string."""
        return ChemAxonMolecule(molecule=cls._importer.importMol(inchi, "inchi"))

    @classmethod
    def from_smiles(cls, smiles: str) -> Optional[ChemAxonMolecule]:
        """Return an ChemAxonMolecule instance from a SMILES string."""
        return ChemAxonMolecule(molecule=cls._importer.importMol(smiles, "smiles"))

    def get_inchi(self) -> str:
        """Return an InChI representation of the molecule."""
        try:
            aux_inchi = str(self._exporter.exportToFormat(self.native, "inchi"))
        except self._ExportError as error:
            raise ChemAxonError() from error
        # ChemAxon adds a second line with `AuxInfo=` which we drop here.
        return aux_inchi.split("\n")[0]

    def get_inchi_key(self) -> str:
        """Return an InChIKey representation of the molecule."""
        try:
            inchi_key = str(self._exporter.exportToFormat(self.native, "inchikey"))
        except self._ExportError as error:
            raise ChemAxonError() from error
        # Remove the non-standard prefix.
        return inchi_key[len("InChIKey=") :]

    def get_smiles(self) -> str:
        """Return a SMILES representation of the molecule."""
        try:
            return str(self._exporter.exportToFormat(self.native, "smiles"))
        except self._ExportError as error:
            raise ChemAxonError() from error

    def get_chemical_formula(self) -> str:
        """Return a chemical formula of the molecule."""
        raise NotImplementedError()

    def get_molecular_mass(self) -> float:
        """
        Return the molecular mass of the molecule in dalton (Da or u).

        This takes into account the average atom mass based on isotope frequency.
        """
        raise NotImplementedError()

    def get_charge(self) -> int:
        """Return the molecule's formal charge."""
        raise NotImplementedError()
