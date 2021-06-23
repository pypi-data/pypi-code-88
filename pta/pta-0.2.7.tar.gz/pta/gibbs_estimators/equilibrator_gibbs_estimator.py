import logging
from typing import Dict, List, Tuple, Union

import numpy as np
import numpy.linalg as la
import scipy.io as sio
from component_contribution.linalg import LINALG
from equilibrator_api import ComponentContribution, Reaction

from ..commons import Q
from ..compartment_parameters import CompartmentParameters
from ..constants import LOG10, F, R, default_rmse
from ..metabolite import Metabolite
from ..utils import qrvector, qvector
from .gibbs_estimator_interface import GibbsEstimatorInterface

_DEFAULT_INCORRECT_METABOLITES: List[str] = [
    # Glycogen has different composition in different models.
    "glycogen",
    "bigg.metabolite:glycogen",
]

logger = logging.getLogger(__name__)


class EquilibratorGibbsEstimator(GibbsEstimatorInterface):
    """Estimation of Gibbs free energies using `equilibrator_api`.

    Parameters
    ----------
    rmse_inf : Q, optional
        Uncertainty to use for unknown groups or compounds.
    """

    def __init__(self, rmse_inf: Q = default_rmse):
        assert rmse_inf.check("kJ/mol")
        self._eq_api = ComponentContribution(rmse_inf=rmse_inf)
        self._rmse_inf = rmse_inf
        self._incorrect_metabolites = _DEFAULT_INCORRECT_METABOLITES.copy()

    @property
    def eq_api(self):
        """Gets the equilibrator API object."""
        return self._eq_api

    @property
    def rmse_inf(self):
        """Gets the uncertainty used for unknown compounds or groups."""
        return self._rmse_inf

    @property
    def incorrect_metabolites(self) -> List[str]:
        """Gets the list of metabolites that are not correctly recognized by
        equilibrator."""
        return self._incorrect_metabolites

    @incorrect_metabolites.setter
    def incorrect_metabolites(self, value: List[str]):
        """Sets the list of metabolites that are not correctly recognized by
        equilibrator."""
        self._incorrect_metabolites = value

    def get_dfg0_prime(
        self,
        S: np.array,
        metabolites: List[Metabolite],
        parameters: CompartmentParameters,
    ) -> Tuple[Q, Q]:
        """Estimates the standard Gibbs free energies for a reaction network
        using `equilibrator_api`.

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
        """
        dfg0_prime_mean, dfg0_prime_cov_sqrt, unknowns_basis = self._get_dfg0(
            self._make_metabolite_keys(metabolites),
            qrvector([parameters.pH(m.compartment) for m in metabolites]),
            qrvector([parameters.pMg(m.compartment) for m in metabolites]),
            qrvector([parameters.I(m.compartment) for m in metabolites]),
            parameters.T(),
        )

        # Fit the estimates for unknown degrees of freedom.
        dfg0_prime_mean = self._fit_unknown_dfg0(S, dfg0_prime_mean, unknowns_basis)

        # Transform the formation energies according to the properties of their
        # compartment.
        dfg0_prime_correction = self._get_dfg0_correction_compartment(
            metabolites, parameters
        )
        dfg0_prime_mean = dfg0_prime_mean + dfg0_prime_correction

        return dfg0_prime_mean, dfg0_prime_cov_sqrt

    def _get_dfg0(
        self,
        met_keys: List[str],
        met_pH: Q,
        met_pMg: Q,
        met_I: Q,
        met_T: Q,
    ) -> Tuple[Q, Q, Q]:
        """Compute estimates for the formation energies of a list of metabolites.

        The method uses eQuilibrator to return mean as well as covariance of the
        estimates.

        Parameters
        ----------
        met_keys : List[str]
            List of n keys identifying the metabolites. These can be in any format
            or namespace supported by eQuilibrator.
        met_pH : Q
            Vector containing the pH of the compartment of each metabolite.
        met_pMg : Q
            Vector containing the pMg of the compartment of each metabolite.
        met_I : Q
            Vector containing the ionic strength of the compartment of each
            metabolite.
        met_T : Q
            Vector containing the temperature of the compartment of each
            metabolite.

        Returns
        -------
        Tuple[Q, Q, Q]
            Tuple with a n-dimensional vector containing the estimates of the n
            metabolites, a square root of the covariance matrix of the
            estimation uncertainty and a matrix containing the columns of the
            sqrt-covariance for which equilibrator has no estimate (the uncertainty is
            virtually infinite).
        """

        # Use half-reactions as a workaround for eQuilibrator not exposing
        # formation energies explicitely.
        half_rxn_strings = ["= " + m for m in met_keys]
        rxns = [self._try_parse_reaction(r) for r in half_rxn_strings]

        # Only work with metabolites for which eQuilibrator can provide an estimate.
        # The remaining metabolites will be handled further down.
        missing_rxn_ids, covered_rxn_ids, covered_rxns = [], [], []
        for i, rxn in enumerate(rxns):
            if rxn is not None:
                covered_rxn_ids.append(i)
                covered_rxns.append(rxn)
            else:
                missing_rxn_ids.append(i)

        met_pH = [met_pH[i] for i in covered_rxn_ids]
        met_I = [met_I[i] for i in covered_rxn_ids]
        met_pMg = [met_pMg[i] for i in covered_rxn_ids]

        if len(missing_rxn_ids) > 0:
            logger.warning(
                "\n    ".join(
                    ["The following metabolites could not be found in eQuilibrator:"]
                    + [met_keys[idx] for idx in missing_rxn_ids]
                )
            )

        met_count = len(met_keys)
        dfg0_mean = Q(np.zeros((met_count, 1)), "kJ/mol")
        dfg0_cov_sqrt = Q(np.zeros((len(rxns), len(rxns))), "kJ/mol")
        default_dfg0_std = self.rmse_inf
        basis_size = 0
        unreliable_basis_ids = []

        if covered_rxn_ids != []:
            dfg0_mean[covered_rxn_ids, 0] = qrvector(
                [
                    self._try_get_drg0_prime_single(*rxn_args, met_T)
                    for rxn_args in zip(covered_rxns, met_pH, met_pMg, met_I)
                ]
            )

            _, cov_sqrt = self.eq_api.standard_dg_prime_multi(covered_rxns, "fullrank")
            basis_size = cov_sqrt.shape[1]
            dfg0_cov_sqrt[covered_rxn_ids, 0:basis_size] = Q(cov_sqrt, "kJ/mol")

            # When equilibrator recognizes an metabolite or group but has
            # insufficient information to make an estimate, it will return an
            # unreliable estimate and an uncertainty equal to rmse_inf. We flag
            # and fit these values later.
            unreliable_basis_ids = [
                i
                for i in range(basis_size)
                if np.any(np.abs(dfg0_cov_sqrt[:, i]) >= self.rmse_inf)
            ]

            # Fill estimates for non-covered metabolites with conservative values.
            default_dfg0_mean = np.mean(dfg0_mean[covered_rxn_ids, 0])
            dfg0_mean[missing_rxn_ids, 0] = default_dfg0_mean

        # Enforce correlation between multiple occurrences of the same metabolite in
        # different compartments when eQuilibrator doesn't recognize the metabolite.
        metabolite_basis_id: Dict[str, int] = {}
        eq_basis_size = basis_size
        for rxn_id in missing_rxn_ids:
            metabolite_id = met_keys[rxn_id]
            if metabolite_id in metabolite_basis_id:
                dfg0_cov_sqrt[
                    rxn_id, metabolite_basis_id[metabolite_id]
                ] = default_dfg0_std
            else:
                metabolite_basis_id[metabolite_id] = basis_size
                dfg0_cov_sqrt[rxn_id, basis_size] = default_dfg0_std
                basis_size += 1

        # Identify dimensions for which eQuilibrator has no estimate.
        unreliable_basis_ids += range(eq_basis_size, basis_size)
        unknowns_basis = dfg0_cov_sqrt[:, unreliable_basis_ids].m_as("kJ/mol")

        return dfg0_mean, dfg0_cov_sqrt, unknowns_basis

    def _get_dfg0_correction_compartment(
        self, metabolites: List[Metabolite], parameters: CompartmentParameters
    ):

        nH = np.array([[m.nH] for m in metabolites])
        z = np.array([[m.z] for m in metabolites])
        pH = qvector([parameters.pH(m.compartment) for m in metabolites])
        phi = qvector([parameters.phi(m.compartment) for m in metabolites])

        pH_correction = -R * parameters.T() * LOG10 * pH * nH
        phi_correction = F * phi * z

        return pH_correction + phi_correction

    def _make_metabolite_keys(
        self,
        metabolites: List[Metabolite],
    ) -> List[str]:
        return [
            m.key
            if m.key not in self.incorrect_metabolites
            else "__incorrect__:" + m.key
            for m in metabolites
        ]

    def _try_parse_reaction(
        self,
        rxn_string: str,
    ) -> Union[Reaction, None]:
        """Parse a string into a Reaction object.

        Returns none if eQuilibrator cannot provide an estimate for the free energy
        of the reaction.
        """
        logging.getLogger().setLevel(logging.ERROR)
        try:
            reaction = self._eq_api.parse_reaction_formula(rxn_string)
        except Exception:
            return None

        for cpd, _ in reaction.items():
            if len(cpd.microspecies) == 0:
                return None
        logging.getLogger().setLevel(logging.WARNING)
        return reaction

    def _try_get_drg0_prime_single(
        self,
        rxn: Reaction,
        pH: Q,
        pMg: Q,
        I: Q,
        T: Q,
    ) -> Q:
        """Estimate the transformed standard free energy of a reaction."""
        self._eq_api.p_h = pH
        self._eq_api.ionic_strength = I
        self._eq_api.temperature = T
        self._eq_api.p_mg = pMg
        return self._eq_api.standard_dg_prime(rxn).value

    def _fit_unknown_dfg0(
        self, S: np.array, dfg0_prime_mean: Q, unknowns_basis: np.array
    ) -> Q:
        # Perform Ordinary Least Squares on the unknown metabolites.
        X = S.T @ unknowns_basis
        y = -S.T @ dfg0_prime_mean.m_as("kJ/mol")
        beta = la.lstsq(X, y, rcond=None)[0]
        return dfg0_prime_mean + Q(unknowns_basis @ beta, "kJ/mol")
