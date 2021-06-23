"""Definition of the prior distribution of metabolite concentrations.
"""

import csv
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import pkg_resources
from equilibrator_cache import CompoundCache, create_compound_cache_from_zenodo

from .constants import Q, default_log_conc
from .distributions import (
    LogNormalDistribution,
    LogUniformDistribution,
    distribution_from_string,
    distribution_to_string,
)
from .metabolite import Metabolite
from .utils import get_path


class ConcentrationsPrior:
    """
    Manages prior distributions of concentrations for specific metabolites or
    compartments. This class provides a distribution for the concentration of any
    metabolite using (depending on the availability) (1) the distribution for the
    metabolite itself, (2) the default distribution of the compartment or (3) a default
    distribution.

    Internally, metabolites are stored and accessed by eQuilibrator's internal
    compound IDs or, when the compound is not recognized, by metabolite name.

    Parameters
    ----------
    compound_cache : Optional[CompoundCache], optional
        eQuilibrator's :code:`CompoundCache` object, used to identify compounds using
        identifiers from different namespaces. For performance reasons, it is
        recommended to use a single instance of `CompoundCache` for all functions in
        PTA.
    metabolite_distributions : Dict[Tuple[str, str], Any], optional
        Mapping from metabolites to their prior. Metabolites are specified as a tuple of
        metabolite ID and compartment ID.
    compartment_distributions : Dict[str, Any], optional
        Mapping from compartment IDs to the prior of the concentration for the
        compartment. This prior is used for compounds for which no explicit prior is
        given.
    default_distribution : Any, optional
        Prior distribution to use for metabolites and compartments for which no prior is
        specified.
    """

    def __init__(
        self,
        compound_cache: Optional[CompoundCache] = None,
        metabolite_distributions: Dict[Tuple[str, str], Any] = {},
        compartment_distributions: Dict[str, Any] = {},
        default_distribution: Any = default_log_conc,
    ):
        self._ccache = compound_cache or create_compound_cache_from_zenodo()

        self._metabolite_distributions = metabolite_distributions
        self._compartment_distributions = compartment_distributions
        self._default_distribution = default_distribution

        self.update_identifiers()

    @staticmethod
    def load(
        prior_file: Union[Path, str],
        compound_cache: Optional[CompoundCache] = None,
    ) -> "ConcentrationsPrior":
        """Loads the concentration priors from a .csv file.

        Parameters
        ----------
        prior_file : Union[Path, str]
            Path to the file containing the parameter values or name of a builtin
            priors set (any file present in data/concentration_priors/, e.g.
            'ecoli_M9_ac').
        compound_cache : Optional[CompoundCache], optional
            eQuilibrator's `CompoundCache` object, used to identify compounds using
            identifiers from different namespaces. For performance reasons, it is
            recommended to use a single instance of `CompoundCache` for all functions in
            PTA.

        Returns
        -------
        [type]
            [description]
        """
        # If the user passed the name of a priors set, try to load it from the data
        # folder. Otherwise, assume the user specified a file and try to load it.
        if isinstance(prior_file, str) and not "." in prior_file:
            prior_file = pkg_resources.resource_filename(
                "pta", f"data/concentration_priors/{prior_file}.csv"
            )
        prior_file = get_path(prior_file)
        if not prior_file.is_file() or not prior_file.exists():
            raise FileNotFoundError(f"Could not find priors file {prior_file}")

        metabolite_distributions = {}
        compartment_distributions = {}
        default_distribution: Any = default_log_conc

        # Read concentration priors from the file.
        with prior_file.open("r") as file:
            # Create csv reader and skip the header line.
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                distribution = distribution_from_string(row[2])
                assert isinstance(distribution, LogUniformDistribution) or isinstance(
                    distribution, LogNormalDistribution
                ), "Concentration priors must be defined in log-scale"
                if row[0] and row[1]:
                    metabolite_id = row[0]
                    metabolite_distributions[(metabolite_id, row[1])] = distribution
                elif row[1]:
                    compartment_distributions[row[1]] = distribution
                else:
                    default_distribution = distribution

        return ConcentrationsPrior(
            compound_cache,
            metabolite_distributions,
            compartment_distributions,
            default_distribution,
        )

    def save(self, prior_file: Union[Path, str]):
        """Saves the concentration priors to a .csv file.

        Parameters
        ----------
        prior_file : Union[Path, str]
            Path to the destination file.
        """
        prior_file = get_path(prior_file)

        with prior_file.open("w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Metabolite", "Compartment", "Distribution"])
            for key, d in self.metabolite_distributions.items():
                writer.writerow([key[0], key[1], distribution_to_string(d)])
            for key2, d in self.compartment_distributions.items():
                writer.writerow(["", key2, distribution_to_string(d)])
            writer.writerow(["", "", distribution_to_string(self.default_distribution)])

    def add(
        self,
        other: "ConcentrationsPrior",
        overwrite_metabolite_priors: bool = True,
        overwrite_compartment_priors: bool = True,
        overwrite_default_prior: bool = True,
    ):
        """Adds the distributions from another prior to this object.

        Parameters
        ----------
        other : ConcentrationsPrior
            The concentrations prior from which the distributions have to be copied.
        overwrite_metabolite_priors : bool, optional
            Specifies whether, in case of duplicates, metabolite distributions in this
            object should be overwritten or not.
        overwrite_compartment_priors : bool, optional
            Specifies whether, in case of duplicates, compartment distributions in this
            object should be overwritten or not.
        overwrite_default_prior : bool, optional
            Specifies whether the default distribution in this object should be
            overwritten or not.
        """

        if overwrite_metabolite_priors:
            self._metabolite_distributions = {
                **self._metabolite_distributions,
                **other.metabolite_distributions,
            }
        else:
            self._metabolite_distributions = {
                **other.metabolite_distributions,
                **self._metabolite_distributions,
            }

        if overwrite_compartment_priors:
            self._compartment_distributions = {
                **self._compartment_distributions,
                **other.compartment_distributions,
            }
        else:
            self._compartment_distributions = {
                **other.compartment_distributions,
                **self._compartment_distributions,
            }

        if overwrite_default_prior:
            self._default_distribution = other.default_distribution

        self.update_identifiers()

    def get(self, metabolite: str, compartment: str) -> Any:
        """Gets the distribution for the concentration of a given compound. This uses
        (depending on the availability) (1) the distribution for the compound itself,
        (2) the default distribution of the compartment or (3) a default distribution.

        Parameters
        ----------
        metabolite : str
            Identifier (in any namespace supported by eQuilibrator) of the compound.
        compartment : str
            Identifier of the compartment.

        Returns
        -------
        Any
            Distribution of the concentration of the specified compound.
        """
        # Try to find a prior by the equilibrator ID of the compound first.
        compound = self._ccache.get_compound(metabolite)
        if compound is not None:
            if self._ccache.is_water(compound) or self._ccache.is_proton(compound):
                return LogNormalDistribution(Q(0.0), Q(0.0))
            key = (compound.id, compartment)
            distribution = self._metabolite_distributions_eq.get(key)
            if distribution is not None:
                return distribution.copy()

        # If nothing was found, try to use the specified ID.
        key = (metabolite, compartment)
        distribution = self.metabolite_distributions.get(key)
        if distribution is not None:
            return distribution.copy()

        # If nothing was found through the identifier, fallback on compartment and
        # default priors.
        distribution = self.compartment_distributions.get(compartment)
        if distribution is not None:
            return distribution.copy()
        return self.default_distribution.copy()

    def update_identifiers(self):
        """Updates the internal representation of the compound identifiers.

        When possible, this class uses eQuiibrator's internal identifiers to represent
        compounds. This has the advantage that priors can be created and accessed using
        different namespaces. This function should be called whenever
        `metabolite_distributions` is modified.
        """
        self._metabolite_distributions_eq = {}
        for k, d in self._metabolite_distributions.items():
            compound = self._ccache.get_compound(k[0])
            if compound is not None:
                eq_id = compound.id
            else:
                eq_id = k[0]
            self._metabolite_distributions_eq[(eq_id, k[1])] = d

    @property
    def metabolite_distributions(self) -> Dict[Tuple[Any, str], Any]:
        """Gets the prior concentrations for specific metabolites. If the distributions
        are modified through this property, `update_identifiers()` should be called to
        make sure that compounds are identified correctly across different
        namespaces.
        """
        return self._metabolite_distributions

    @property
    def compartment_distributions(self) -> Dict[str, Any]:
        """Gets the prior concentrations for specific compartments."""
        return self._compartment_distributions

    @property
    def default_distribution(self):
        """Gets the default prior for concentrations."""
        return self._default_distribution
