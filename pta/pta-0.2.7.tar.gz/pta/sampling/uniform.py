import datetime
import logging
from typing import List, Tuple, Union

import numpy as np
import pandas as pd

import _pta_python_binaries as pb
import cobra
from PolyRound.api import PolyRoundApi, Polytope, StoichiometryParser

from ..constants import (
    default_flux_bound,
    default_max_psrf,
    default_num_samples,
    us_steps_multiplier,
)
from ..utils import apply_transform
from .commons import (
    SamplingException,
    SamplingResult,
    apply_to_chains,
    fill_common_sampling_settings,
    sample_from_chains,
    split_R,
)

logger = logging.getLogger(__name__)


class UniformSamplingModel:
    """Object holding the information necessary to run uniform sampling.

    Parameters
    ----------
    polytope : Polytope
        Polytope object describing the flux space.
    reaction_ids : List[str]
        Identifiers of the reactions in the flux space.
    """

    def __init__(self, polytope: Polytope, reaction_ids: List[str]):
        rounded_polytope = PolyRoundApi.simplify_transform_and_round(polytope)
        self._G = rounded_polytope.A.to_numpy()
        self._h = rounded_polytope.b.to_numpy()[:, np.newaxis]
        self._to_fluxes_transform = (
            rounded_polytope.transformation.to_numpy(),
            rounded_polytope.shift.to_numpy()[:, np.newaxis],
        )
        self._reaction_ids = reaction_ids
        logger.info(
            f"Created sampling polytope with {self.dimensionality} dimensions and "
            f"{self.h.size} constraints."
        )

    @property
    def G(self) -> np.array:
        """Gets the left-hand side of the constraints of the flux space."""
        return self._G

    @property
    def h(self) -> np.array:
        """Gets the right-hand side of the constraints of the flux space."""
        return self._h

    @property
    def to_fluxes_transform(self) -> Tuple[np.array, np.array]:
        """Gets the transform from a point in the model to a point in the flux space."""
        return self._to_fluxes_transform

    @property
    def reaction_ids(self):
        """Gets the IDs of the reactions in the model."""
        return self._reaction_ids

    def to_fluxes(self, value: np.array) -> np.array:
        """Transform a point or matrix from the model to the flux space.

        Parameters
        ----------
        value : np.array
            Input values.

        Returns
        -------
        np.array
            The corresponding fluxes.
        """
        return apply_transform(value, self.to_fluxes_transform)

    @property
    def dimensionality(self) -> int:
        """Gets the dimensionality of the flux space."""
        return self.G.shape[1]

    @classmethod
    def from_cobrapy_model(
        cls, model: cobra.Model, infinity_flux_bound: float = default_flux_bound
    ) -> "UniformSamplingModel":
        """Builds a uniform sampling model from a cobrapy model.

        Parameters
        ----------
        model : cobra.Model
            The input cobra model.
        infinity_flux_bound : float, optional
            Default bound to use for unbounded fluxes.

        Returns
        -------
        UniformSamplingModel
            The constructed model.
        """
        polytope = StoichiometryParser.extract_polytope(model, infinity_flux_bound)
        return cls(polytope, [r.id for r in model.reactions])


def get_initial_points(model: "UniformSamplingModel", num_points: int) -> np.array:
    """Gets initial points for sampling fluxes.

    Parameters
    ----------
    model : UniformSamplingModel
        The model to sample.
    num_points : int
        Number of initial points to generate.

    Returns
    -------
    np.array
        Array containing the initial points.
    """
    # Find the radius of the hypersphere inscribed in the polytope.
    distances = model.h / np.linalg.norm(model.G, axis=1)
    radius = np.min(distances)

    # Sample random directions and scale them to a random length inside the hypersphere.
    samples = np.random.rand(model.dimensionality, num_points)
    length = np.random.rand(1, num_points) ** (
        1 / model.dimensionality
    ) / np.linalg.norm(samples, axis=0)
    samples = samples * np.diag(length) * radius

    logger.info(f"Generated {num_points} initial points.")
    return samples


def sample_flux_space_uniform(
    model: Union[cobra.Model, "UniformSamplingModel"],
    num_samples: int = default_num_samples,
    initial_points: np.array = None,
    num_steps: int = -1,
    num_warmup_steps: int = -1,
    num_chains: int = -1,
    log_interval: datetime.timedelta = None,
    max_psrf: float = default_max_psrf,
    check_convergence: bool = True,
) -> SamplingResult:
    """Sample steady state fluxes in the given model.

    Parameters
    ----------
    model : Union[cobra.Model, UniformSamplingModel]
        The model to sample.
    num_samples : int, optional
        Number of samples to draw.
    initial_points : np.array, optional
        The initial points for the chains.
    num_steps : int, optional
        The number of steps to use for each chain.
    num_warmup_steps : int, optional
        The number of burn-in steps to discard.
    num_chains : int, optional
        The number of chains to simulate.
    log_interval : datetime.timedelta, optional
        How often should the sampler log the progress.
    max_psrf : float, optional
        Maximum value of the PSRFs for convergence.
    check_convergence : bool, optional
        Whether to check for convergence or not.

    Returns
    -------
    SamplingResult
        The sampling result.

    Raises
    ------
    SamplingException
        If sampling fails.
    """
    if isinstance(model, cobra.Model):
        model = UniformSamplingModel.from_cobrapy_model(model)

    if num_steps < 0:
        num_steps = model.dimensionality ** 2 * us_steps_multiplier
    if initial_points is not None and num_chains < 0:
        num_chains = initial_points.shape[1]

    # Fill the settings.
    settings = pb.UniformSamplerSettings()
    fill_common_sampling_settings(
        settings,
        "",
        num_samples,
        num_steps,
        num_chains,
        num_warmup_steps,
        log_interval,
    )

    # Generate the initial points if needed.
    initial_points = initial_points or get_initial_points(model, settings.num_chains)
    assert (
        initial_points.shape[1] == settings.num_chains
    ), "Sampling requires the same number of initial points and chains."

    logger.info(
        f"Starting uniform sampler with {settings.num_chains} chains and "
        f"{settings.num_steps} steps."
    )

    try:
        chains = pb.sample_flux_space_uniform(
            model.G,
            model.h,
            np.identity(model.dimensionality),
            initial_points,
            settings,
        )
    except Exception as e:
        logger.error(f"Uniform sampling failed. {e}")
        raise SamplingException("Uniform sampling failed.") from e
    else:
        logger.info("Sampling completed.")
        samples = model.to_fluxes(sample_from_chains(chains, num_samples).T).T

        logger.info("Computing PSRFs.")
        psrf_var_names = [
            "var" + str(i) for i in range(model.dimensionality)
        ] + model.reaction_ids
        psrf = np.hstack(
            [split_R(chains), split_R(apply_to_chains(chains, model.to_fluxes))]
        )

        result = SamplingResult(
            pd.DataFrame(samples, columns=model.reaction_ids),
            pd.Series(psrf, index=psrf_var_names),
        )
        if check_convergence:
            if result.check_convergence(max_psrf):
                logger.info("Convergence criteria satisfied.")
            else:
                logger.warning(
                    "Uniform sampling did not converge. Please try increasing the number "
                    "of steps."
                )

        return result
