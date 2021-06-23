"""Methods for the thermodynamic assessment of a metabolic network.
"""

import logging
from typing import List, Optional, Union

import numpy as np
import pandas as pd

import cobra
from cobra.flux_analysis.variability import (
    find_blocked_reactions,
    flux_variability_analysis,
)

from .constants import (
    Q,
    default_flux_bound,
    default_max_non_intracellular_conc_mM,
    default_theta_s,
    default_theta_z,
    non_intracellular_compartment_ids,
)
from .pmo import PmoProblem
from .utils import get_internal_cycles, tighten_model_bounds

logger = logging.getLogger(__name__)


class StructuralAssessment:
    """This class is used to find thermodynamic inconsistencies in the definition of the
    network that make the model infeasible. Inconsistencies arise when flux constraints
    (steady state and irreversibilities) prevent any thermodynamically feasible non-zero
    solution. These inconsistencies occur with any assignment of Gibbs free energies.

    Parameters
    ----------
    model : cobra.Model
        The target model.
    biomass_id : Optional[str], optional
        ID of the biomass reactions. If None, the method will try to find it
        automatically.
    atpm_id : str, optional
        ID of the ATP maintenance reaction.
    """

    def __init__(
        self,
        model: cobra.Model,
        biomass_id: Optional[str] = None,
        atpm_id: str = "ATPM",
    ):
        # Enumerate all the internal cycles of the network and select the ones that must
        # be active in any non-zero solution.
        cycles = get_internal_cycles(model, biomass_id, atpm_id)
        forced_cycles = self._get_forced_internal_cycles(model, cycles)

        # Convert the EFMs matrix to a list of cycles, represented by reaction IDs.
        self._forced_internal_cycles = []
        for cycle in forced_cycles.T:
            cycle_reaction_ids = [
                model.reactions[i].id for i, v in enumerate(cycle) if v != 0
            ]
            self._forced_internal_cycles.append(cycle_reaction_ids)

    @property
    def forced_internal_cycles(self) -> List[List[str]]:
        """Gets a list of all the forced internal cycles of the network, i.e. the
        internal cycles that must be active in any non-zero flux solution and
        thus make the model thermodynamically inconsistent.
        """
        return self._forced_internal_cycles

    def summary(self):
        """Print a summary of the structural assessment."""
        print("Strutural thermodynamic assessment summary:")
        print("---------------------------------------------")
        print("")

        pd_context = pd.option_context(
            "display.max_rows",
            None,
            "display.max_columns",
            None,
            "display.precision",
            3,
        )

        if len(self.forced_internal_cycles) > 0:
            print(
                "> The following internal cycles are thermodynamically "
                "unfeasible, but must be active in any non-zero flux "
                "solution, meaning that the model is thermodynamically "
                "inconsistent. For the cycles below, please:\n (1) Verify and "
                "correct the direction of the irreversible reactions.\n (2) "
                "Remove reactions in cycles that are connected to the rest "
                "of the network through a single reaction (e.g. A -> B, "
                "B -> A, where only A participates in other reactions).\n "
                "Alternatively, you can use the StructuralAssessment."
                "autoresolve() function to automatically curate the model."
            )
            for i, cycle in enumerate(self.forced_internal_cycles):
                print(f'{i}. {", ".join(cycle)}')
        else:
            print(f"> No thermodynamic inconsistencies detected in the model.")
        print("")

    def autoresolve(
        self, model: cobra.Model, default_bound: float = default_flux_bound
    ):
        """Attempt to automatically resolve thermodynamic inconsistencies. This method
        removes all reactions involved in dead-end cycles (internal cycles that
        exchange flux with the rest of the network through a single metabolite) and
        makes all the reactions in the remaining cycles reversible. While this method
        should always resolve all inconsistencies, it is still recommended to inspect
        the inconsistencies and the curated model manually to verify that the model
        behave as expected. The output of the curation can be seen by enabling logging
        level INFO.

        Parameters
        ----------
        model : cobra.Model
            The model in which the curation actions must be applied. This can be the
            model on which the assessment was run or a similar model. This is useful for
            cases where assessment is run on a condition specific model but actions
            should be applied to a base model.
        default_bound : float, optional
            Default bound to use for unconstrained reactions.
        """
        for cycle in self.forced_internal_cycles:
            if self._is_semi_disconnected_cycle(model, cycle):
                logger.info(
                    "Removing all reactions of the dead-end cycle:"
                    f' {", ".join(cycle)}.'
                )
                model.remove_reactions(cycle, remove_orphans=True)
            else:
                logger.info(
                    "Removing bounds for all reactions in the cycle: "
                    f'{", ".join(cycle)}.'
                )
                for rxn_id in cycle:
                    try:
                        reaction = model.reactions.get_by_id(rxn_id)
                    except:
                        continue
                    reaction.lower_bound = -default_bound
                    reaction.upper_bound = default_bound

    def _is_semi_disconnected_cycle(self, model: cobra.Model, cycle: np.array) -> bool:
        """Check whether a cycle is dead-end, i.e. it exchanges flux with the
        rest of the network through a single metabolite only.
        """
        with model as model:
            # Pick a reaction and fix it to a flux value that is not at the
            # boundaries.
            try:
                fixed_reaction = model.reactions.get_by_id(cycle[0])
            except:
                # If the reaction does not exist, the cycle is broken and we don't need
                # to do anything else.
                return False
            model.objective = {fixed_reaction: 1}
            max_flux = model.slim_optimize()
            model.objective = {fixed_reaction: -1}
            min_flux = -model.slim_optimize()
            fixed_flux = (max_flux + min_flux) / 2
            fixed_reaction.lower_bound = fixed_flux
            fixed_reaction.upper_bound = fixed_flux

            # If all other reactions of the cycle are not fixed as well, then this is a
            # dead-end cycle.
            for i in range(len(cycle)):
                try:
                    other_reaction = model.reactions.get_by_id(cycle[i])
                except:
                    return False
                model.objective = {other_reaction: 1}
                max_flux = model.slim_optimize()
                model.objective = {other_reaction: -1}
                min_flux = -model.slim_optimize()
                if max_flux - min_flux > 1e-8:
                    return False

        return True

    def _get_forced_internal_cycles(
        self, model: cobra.Model, cycles: np.array
    ) -> np.array:
        """Select our of a list of cycles the ones that are forced."""
        forced_cycle_idxs = []
        for e in range(cycles.shape[1]):
            if self._is_forced_cycle(model, cycles[:, e]):
                forced_cycle_idxs.append(e)

        return cycles[:, forced_cycle_idxs]

    def _is_forced_cycle(
        self,
        model: cobra.Model,
        cycle: np.array,
    ) -> bool:
        """Check if a cycle is forced (must be active in any non-zero flux solution)."""
        min_flux = 1e-6
        rxn_idxs = np.where(cycle != 0)[0].tolist()

        # Check for any pair of reaction and for any sense of the cycle.
        for i in range(len(rxn_idxs)):
            for j in range(i):
                for sense in [-1, 1]:
                    with model as model:
                        rxn_i = model.reactions[rxn_idxs[i]]
                        rxn_j = model.reactions[rxn_idxs[j]]
                        direction_i = cycle[rxn_idxs[i]] * sense
                        direction_j = cycle[rxn_idxs[j]] * sense

                        # If the chosen directions are not within the flux bounds of the
                        # model we can skip the iteration.
                        if (
                            (direction_i > 0 and rxn_i.upper_bound <= 0)
                            or (direction_i < 0 and rxn_i.lower_bound >= 0)
                            or (direction_j < 0 and rxn_j.upper_bound <= 0)
                            or (direction_j > 0 and rxn_j.lower_bound >= 0)
                        ):
                            continue

                        # Set the direction of the cycle for the first reaction.
                        if direction_i > 0:
                            rxn_i.lower_bound = max(rxn_i.lower_bound, min_flux)
                        else:
                            rxn_i.upper_bound = min(rxn_i.upper_bound, -min_flux)

                        # Set the opposite direction (with respect to the direction in
                        # the EFM) for the second reaction.
                        if direction_j < 0:
                            rxn_j.lower_bound = max(rxn_j.lower_bound, min_flux)
                        else:
                            rxn_j.upper_bound = min(rxn_j.upper_bound, -min_flux)

                        # Check whether the model is feasible. If yes, there are
                        # thermodynamically feasible solutions for the set of
                        # reactions involved in the EFM because the cycle is not
                        # mandatory.
                        if not np.isnan(model.slim_optimize()):
                            return False

        # If we could not find any thermodynamically feasible combination of directions
        # the cycle is forced.
        return True


class QuantitativeAssessment:
    """Quantitative thermodynamic assessment of a metabolic network. This process
    combines thermodynamic data and flux constraints to identify parts of the network
    where the mechanism in the model is possibly incorrect.

    Parameters
    ----------
    pmo_problem : PmoProblem
        A solved PMO problem.
    z_score_threshold : float, optional
        Threshold on the z-score to consider a predicted value an anomaly.
    shadow_price_threshold : float, optional
        Threshold on the shadow price to consider a reaction a strong thermodynamic
        constrain.
    max_extracellular_conc : Q, optional
        Threshold on the concentration to consider a predicted concentration an anomaly.
    """

    def __init__(
        self,
        pmo_problem: PmoProblem,
        z_score_threshold: float = default_theta_z,
        shadow_price_threshold: float = default_theta_s,
        max_extracellular_conc: Q = None,
    ):
        self._theta_z = z_score_threshold
        self._theta_s = shadow_price_threshold
        self._max_ex_conc = max_extracellular_conc or Q(
            default_max_non_intracellular_conc_mM, "mM"
        )
        self._is_intracellular = pd.DataFrame(
            [
                m.compartment not in non_intracellular_compartment_ids
                for m in pmo_problem.T.metabolites
            ]
        )

        # Restrict the PMO problem to the predicted directions. This way, the
        # problem is not an MILP anymore and solvers should be able to return
        # shadow prices.
        orthant_pmo = pmo_problem.rebuild_for_directions(pmo_problem.d.value)
        status = orthant_pmo.solve()

        assert status == "optimal" or status == "optimal_inaccurate"
        if status == "optimal_inaccurate":
            logger.warning("Inaccurate solution found when computing shadow prices.")

        # Assemble metabolite and reaction data in two data frames.
        self._metabolites_df = pd.DataFrame(
            {
                "id": pmo_problem.T.metabolite_ids,
                "conc": np.exp(pmo_problem.log_c).ravel() * 1000
                if pmo_problem.log_c is not None
                else np.nan,
                "z_log_c": self._make_z_scores(pmo_problem, "log_c"),
            }
        )

        self._reactions_df = pd.DataFrame(
            {
                "id": pmo_problem.T.reaction_ids,
                "v": pmo_problem.v[pmo_problem._rxn_idxs_F_to_T].ravel(),
                "drg0": pmo_problem.drg0.ravel()
                if pmo_problem.drg0 is not None
                else np.nan,
                "drg": pmo_problem.drg.ravel()
                if pmo_problem.drg is not None
                else np.nan,
                "z_drg": self._make_z_scores(pmo_problem, "drg"),
                "z_drg0": self._make_z_scores(pmo_problem, "drg0"),
                "sp_drg": np.maximum(
                    orthant_pmo.sign_constraints[0].dual_value,
                    orthant_pmo.sign_constraints[1].dual_value,
                ).ravel(),
            }
        )

    @property
    def metabolites_df(self) -> pd.DataFrame:
        """Gets a data frame with the metabolite-related quantities."""
        return self._metabolites_df

    @property
    def reactions_df(self) -> pd.DataFrame:
        """Gets a data frame with the reaction-related quantities."""
        return self._reactions_df

    @property
    def theta_z(self) -> float:
        """Gets the mimimum absolute z-score used to classify a metabolite
        concentration as anomaly."""
        return self._theta_z

    @property
    def theta_s(self) -> float:
        """Gets the mimimum absolute shadow price to flag a constraint."""
        return self._theta_s

    @property
    def max_ex_concentration(self) -> float:
        """Gets the minimum concentration used to classify a non-intracellular
        metabolite concentration as anomaly."""
        return self._max_ex_conc

    def summary(self):
        """Print a summary of the quantitative assessment."""

        print("Quantitative thermodynamic assessment summary:")
        print("------------------------------------------------")
        print("conentrations: mM, free energies: kJ/mol")
        print("")

        pd_context = pd.option_context(
            "display.max_rows",
            None,
            "display.max_columns",
            None,
            "display.precision",
            3,
        )

        # Search for anomalies based on concentration z-scores.
        anomalies_m_z = self.metabolites_df[
            self.metabolites_df["z_log_c"].abs() > self.theta_z
        ]
        anomalies_m_z = anomalies_m_z.reindex(
            anomalies_m_z["z_log_c"].abs().sort_values(ascending=False).index
        )
        if not anomalies_m_z.empty:
            print(
                f"> The following metabolites have been flagged as "
                f"anomalies because their predicted concentration has an "
                f"absolute z-score greater than {self.theta_z}:"
            )
            with pd_context:
                print(anomalies_m_z)
        else:
            print(f"> No anomaly found in concentration z-scores.")
        print("")

        # Search for anomalies based on maximum concentration.
        max_ex_concentration_mM = self.max_ex_concentration.m_as("mM")
        anomalies_m_m = self.metabolites_df[
            (self.metabolites_df["conc"] >= max_ex_concentration_mM)
            & ~pd.DataFrame(self._is_intracellular)[0]
            & (self.metabolites_df["z_log_c"].abs() > 0)
        ]
        anomalies_m_m = anomalies_m_m.reindex(
            anomalies_m_m["conc"].abs().sort_values(ascending=False).index
        )
        if not anomalies_m_m.empty:
            print(
                f"> The following non-intracellular metabolites have been "
                f"flagged as anomalies because they have concentation "
                f"greater than {max_ex_concentration_mM} mM:"
            )
            with pd_context:
                print(anomalies_m_m)
        else:
            print(f"> No anomaly found in non-intracellular concentrations.")
        print("")

        # Search for anomalies based on reaction z-scores.
        anomalies_r_z = self.reactions_df[
            (self.reactions_df["z_drg"].abs() > self.theta_z)
            | (self.reactions_df["z_drg0"].abs() > self.theta_z)
        ]
        anomalies_r_z = anomalies_r_z.reindex(
            anomalies_r_z[["z_drg", "z_drg0"]]
            .abs()
            .max(axis=1)
            .sort_values(ascending=False)
            .index
        )
        if not anomalies_r_z.empty:
            print(
                f"> The following reactions have been flagged as anomalies "
                f"because their predicted free energy or standard free "
                f"energy has an absolute z-score greater than {self.theta_z}:"
            )
            with pd_context:
                print(anomalies_r_z)
        else:
            print(f"> No anomaly found in free energy z-scores.")
        print("")

        # Search for anomalies based on reaction shadow prices.
        anomalies_r_s = self.reactions_df[(self.reactions_df["sp_drg"] > self.theta_s)]
        anomalies_r_s = anomalies_r_s.reindex(
            anomalies_r_s["sp_drg"].sort_values(ascending=False).index
        )
        if not anomalies_r_s.empty:
            print(
                f"> The following reactions are predicted to impose strong "
                f"thermodynamic constraints on the network because their "
                f"shadow price is greater than {self.theta_s}:"
            )
            with pd_context:
                print(anomalies_r_s)
        else:
            print(f"> No significant thermodynamic constraints found.")
        print("")

    def _make_z_scores(
        self, pmo_problem: PmoProblem, variable: str
    ) -> Union[np.array, float]:
        """Construct the z-scores for a specific type of variables."""
        transform = None
        if variable == "log_c":
            if pmo_problem.B.to_log_conc_transform is not None:
                transform = pmo_problem.B.to_log_conc_transform[0]
        elif variable == "drg":
            if pmo_problem.B.to_drg_transform is not None:
                transform = pmo_problem.B.to_drg_transform[0]
        elif variable == "drg0":
            if pmo_problem.B.to_drg0_transform is not None:
                transform = pmo_problem.B.to_drg0_transform[0]
        else:
            raise ValueError(f"Unsuppoted variable {variable}")

        if transform is None:
            return np.nan
        else:
            std_devs = np.sqrt(np.diag(transform @ transform.T))
            scaling = np.zeros(std_devs.shape)
            scaling[std_devs > 0] = np.reciprocal(std_devs[std_devs > 0])
            scaling = np.diag(scaling)
            return (scaling @ transform @ pmo_problem.m.value).ravel()


def prepare_for_pta(
    model: cobra.Model,
    biomass_id: Optional[str] = None,
    atpm_id: str = "ATPM",
    default_bound: float = default_flux_bound,
    autoresolve_inconsistencies: bool = True,
    remove_blocked_reactions: bool = True,
    tighten_bounds: bool = True,
):
    """Attempt to automatically prepare a model for use in PTA.

    This method performs three actions:

    * Runs structural assessment on the model and attempts to autoresolve possible
      inconsistencies.
    * Removes all blocked reactions from the model.
    * Runs FVA to tighten the flux bounds of each reaction.

    Parameters
    ----------
    model : cobra.Model
        The target model.
    biomass_id : Optional[str], optional
        ID of the biomass reactions. If None, the method will try to find it
        automatically.
    atpm_id : str, optional
        ID of the ATP maintenance reaction.
    default_bound : float, optional
        Default bound to use for unconstrained reactions.
    autoresolve_inconsistencies : bool, optional
        True if the method should attempt to automatically resolve inconsistencies,
        false otherwise. By default True.
    remove_blocked_reactions : bool, optional
        True if the method should remove blocked reactions, false otherwise. By default
        True.
    tighten_bounds : bool, optional
        True if the method should restrict the flux bounds with FVA, false otherwise. By
        default True.
    """
    # Run structural assessment and auto-resolve all inconsistencies.
    if autoresolve_inconsistencies:
        assessment = StructuralAssessment(model, biomass_id, atpm_id)
        assessment.autoresolve(model, default_bound)

    # Remove blocked reactions to make sure that all reactions can have a
    # well-defined direction.
    if remove_blocked_reactions:
        model.remove_reactions(find_blocked_reactions(model), remove_orphans=True)

    # Restrict reaction bounds using FVA.
    if tighten_bounds:
        tighten_model_bounds(model)
