"""Parameters for the compartments of a metabolic network.
"""

from pathlib import Path
from typing import Dict, Union

import pandas as pd
import pkg_resources

from .constants import Q, default_I, default_pH, default_phi, default_pMg, default_T
from .utils import get_path

any_compartment = '__any__'
"""Pseudo-identifier representing any compartment.
"""


class CompartmentParameters:
    """Parameters for the compartments of a metabolic network.

    Parameters
    ----------
    compartment_pH : Dict[str, Q], optional
        Mapping from compartment identifiers to the pH of the compartment.
    compartment_pMg : Dict[str, Q], optional
        Mapping from compartment identifiers to the pMg of the compartment.
    compartment_I : Dict[str, Q], optional
        Mapping from compartment identifiers to the ionic strength of the compartment.
    compartment_phi : Dict[str, Q], optional
        Mapping from compartment identifiers to the electrostatic potential of the
        compartment.
    T : Q, optional
        Temperature of the system (temperature must be the same for all compartments).
    """

    def __init__(
        self,
        compartment_pH: Dict[str, Q] = {any_compartment: default_pH},
        compartment_pMg: Dict[str, Q] = {any_compartment: default_pMg},
        compartment_I: Dict[str, Q] = {any_compartment: default_I},
        compartment_phi: Dict[str, Q] = {any_compartment: default_phi},
        T: Q = default_T
    ):
        self._pH = compartment_pH
        self._pMg = compartment_pMg
        self._I = compartment_I
        self._phi = compartment_phi
        self._T = T

    def pH(self, compartment: str) -> Q:
        """Gets the pH of a compartment."""
        pH = self._pH.get(compartment)
        if pH is None:
            pH = self._pH.get(any_compartment)
        if pH is None:
            raise ValueError(f'Unspecified pH for compartment {compartment}')
        return pH

    def pMg(self, compartment: str) -> Q:
        """Gets the pMg of a compartment."""
        pMg = self._pMg.get(compartment)
        if pMg is None:
            pMg = self._pMg.get(any_compartment)
        if pMg is None:
            raise ValueError(f'Unspecified pMg for compartment {compartment}')
        return pMg

    def I(self, compartment: str) -> Q:
        """Gets the ionic strength of a compartment."""
        I = self._I.get(compartment)
        if I is None:
            I = self._I.get(any_compartment)
        if I is None:
            raise ValueError(f'Unspecified ionic strength for compartment '
                             '{compartment}')
        return I

    def phi(self, compartment: str) -> Q:
        """Gets the electrostatic potential of a compartment."""
        phi = self._phi.get(compartment)
        if phi is None:
            phi = self._phi.get(any_compartment)
        if phi is None:
            raise ValueError(f'Unspecified electrostatic potential for '
                             'compartment {compartment}')
        return phi

    def T(self) -> Q:
        """Gets the temperature of the system."""
        return self._T

    @staticmethod
    def load(params_file: Union[Path, str]) -> "CompartmentParameters":
        """Loads the compartment parameters from a .csv file.

        Parameters
        ----------
        params_file : Union[Path, str]
            Path to the file containing the parameter values or name of a builtin
            parameter set (any file present in data/compartment_parameters/, e.g.
            'e_coli' or 'human').

        Returns
        -------
        CompartmentParameters
            New instance of this class, containing the parameters loaded from the file.
        """
        # If the user passed the name of a parameter set, try to load it from the data
        # folder. Otherwise, assume the user specified a file and try to load it.
        if isinstance(params_file, str) and not '.' in params_file:
            params_file = pkg_resources.resource_filename(
                'pta', f'data/compartment_parameters/{params_file}.csv')
        params_file = get_path(params_file)
        if not params_file.is_file() or not params_file.exists():
            raise FileNotFoundError(
                f'Could not find parameter file {params_file}')

        compartment_pH: Dict[str, Q] = {}
        compartment_pMg: Dict[str, Q] = {}
        compartment_I: Dict[str, Q] = {}
        compartment_phi: Dict[str, Q] = {}
        T: Q = None

        # Read compartment parameters from the file.
        params_df = pd.read_csv(params_file, comment='#')
        for _, row in params_df.iterrows():
            compartment = row['Compartment']
            compartment_pH[compartment] = Q(row['pH'])
            compartment_pMg[compartment] = Q(row['pMg'])
            compartment_I[compartment] = Q(row['I'], 'M')
            compartment_phi[compartment] = Q(row['phi'], 'V')

            if T is None:
                T = Q(row['T'], 'K')
            else:
                assert T is None or T.m == row[5], 'All compartments ' \
                    'must the same temperature'

        return CompartmentParameters(
            compartment_pH,
            compartment_pMg,
            compartment_I,
            compartment_phi,
            T
        )
