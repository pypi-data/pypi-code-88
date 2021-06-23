"""Description of the flux space of a metabolic network.
"""

from typing import List

import numpy as np

import cobra
from cobra.util.array import create_stoichiometric_matrix


class FluxSpace:
    """Description of the flux space of a metabolic network.

    Parameters
    ----------
    S : np.array
        Stoichiometric matrix of the network.
    lb : np.array
        Vector of lower bounds on the reaction fluxes.
    ub : np.array
        Vector of upper bounds on the reaction fluxes.
    reaction_ids : List[str]
        Identifiers of the reactions in the network.
    metabolite_ids : List[str]
        Identifiers of the metabolites in the network.
    """

    def __init__(
        self,
        S: np.array,
        lb: np.array,
        ub: np.array,
        reaction_ids: List[str],
        metabolite_ids: List[str]
    ):
        self._S = S
        self._lb = lb
        self._ub = ub
        self._reaction_ids = reaction_ids
        self._metabolite_ids = metabolite_ids

    @property
    def S(self) -> np.array:
        """Gets the stoichiometric matrix of the network."""
        return self._S

    @S.setter
    def S(self, value: np.array):
        """Sets the stoichiometric matrix of the network."""
        self._S = value

    @property
    def lb(self) -> np.array:
        """Gets the vector of lower bounds on the reaction fluxes."""
        return self._lb

    @lb.setter
    def lb(self, value: np.array):
        """Sets the vector of lower bounds on the reaction fluxes."""
        self._lb = value

    @property
    def ub(self) -> np.array:
        """Gets the vector of upper bounds on the reaction fluxes."""
        return self._ub

    @ub.setter
    def ub(self, value: np.array):
        """Sets the vector of upper bounds on the reaction fluxes."""
        self._ub = value

    @property
    def reaction_ids(self) -> List[str]:
        """Gets the IDs of the reactions in the flux space."""
        return self._reaction_ids

    @property
    def metabolite_ids(self) -> List[str]:
        """Gets the IDs of the metabolites in the flux space."""
        return self._metabolite_ids

    @property
    def n_metabolites(self) -> int:
        """Gets the number of metabolites in the network."""
        return self._S.shape[0]

    @property
    def n_reactions(self) -> int:
        """Gets the number of reactions in the network."""
        return self._S.shape[1]

    def copy(self) -> "FluxSpace":
        """Create a copy of this object.

        Returns
        -------
        FluxSpace
            A copy of this object.
        """
        return FluxSpace(
            self.S.copy(),
            self.lb.copy(),
            self.ub.copy(),
            self.reaction_ids.copy(),
            self.metabolite_ids.copy()
        )

    @staticmethod
    def from_cobrapy_model(model: cobra.Model) -> "FluxSpace":
        """Creates an instance of this class from a cobrapy model.

        Parameters
        ----------
        model : cobra.Model
            The input model.

        Returns
        -------
        FluxSpace
            The constructed object.
        """
        return FluxSpace(
            create_stoichiometric_matrix(model),
            np.array([[r.lower_bound for r in model.reactions]]).T,
            np.array([[r.upper_bound for r in model.reactions]]).T,
            [r.id for r in model.reactions],
            [m.id for m in model.metabolites]
        )
