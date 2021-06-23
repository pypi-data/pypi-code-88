"""Interface for an estimator of Gibbs free energies"""

import abc
from typing import List, Tuple

import numpy as np

from ..commons import Q
from ..compartment_parameters import CompartmentParameters
from ..metabolite import Metabolite


class GibbsEstimatorInterface(metaclass=abc.ABCMeta):
    """Interface for a class implementing estimation of Gibbs free energies"""

    @classmethod
    def __subclasshook__(self, subclass):
        return (
            hasattr(subclass, "get_dfg0_prime")
            and callable(subclass.get_dfg0_prime)
            or NotImplemented
        )

    @abc.abstractmethod
    def get_dfg0_prime(
        self,
        S: np.array,
        metabolites: List[Metabolite],
        compartment_parameters: CompartmentParameters,
    ) -> Tuple[Q, Q]:
        """Estimates the standard Gibbs free energies for a reaction network

        Parameters
        ----------
        S : np.array
            n-by-m stoichiometric matrix of the reaction network.
        metabolites : List[Metabolite]
            A m-elements list describing the compounds in the network.
        compartment_parameters : CompartmentParameters
            The prior for the physiological parameters of each compartment, such
            as pH and ionic strength.

        Returns
        -------
        Tuple[Q, Q]
            A tuple, whose first element is the vector of the mean estimate, and
            the second is a square root :math:`Q` of the
            covariance matrix on the estimation uncertainty :math:`\Sigma`, such
            that :math:`QQ^\intercal = \Sigma`.

        Raises
        ------
        NotImplementedError
            An metaclass does not implement methods. Please use an
            implementation of this interface.
        """
        raise NotImplementedError
