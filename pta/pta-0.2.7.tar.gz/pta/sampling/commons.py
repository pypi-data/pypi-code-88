import datetime
import math
import os
from typing import Any, Callable

import numpy as np
import pandas as pd

from _pta_python_binaries import SamplerSettings

from ..constants import default_max_psrf, default_min_chains


class SamplingException(Exception):
    """Raised when an exception occurs during sampling."""

    pass


class SamplingResult:
    """Encapsulates the result of a sampler.

    Parameters
    ----------
    samples : pd.DataFrame
        Data frame containing the samples as rows.
    psrf : pd.Series
        Series containing the PSRF of each variable.
    """

    def __init__(self, samples: pd.DataFrame, psrf: pd.Series):
        self._samples = samples
        self._psrf = psrf

    @property
    def samples(self) -> pd.DataFrame:
        """Gets a data frame containing the samples."""
        return self._samples

    @property
    def psrf(self) -> pd.Series:
        """Gets the Potential Scale Reduction Factor (PSRF) of each variable."""
        return self._psrf

    def check_convergence(self, max_psrf: float = default_max_psrf) -> bool:
        """Checks whether the chains converged according to the given criteria.

        Parameters
        ----------
        max_psrf : float, optional
            Maximum PSRF value for convergence.

        Returns
        -------
        bool
            True if the test succeeded, false otherwise.
        """
        return np.all(self.psrf <= max_psrf)


def sample_from_chains(chains: np.array, num_samples: int) -> np.array:
    """Draws samples from a given set of chains.

    Parameters
    ----------
    chains : np.array
        Numpy 3D array containing the chains.
    num_samples : int
        Number of samples to draw.

    Returns
    -------
    np.array
        Array of samples.
    """
    samples = np.hstack(chains)
    indices = np.random.choice(samples.shape[1], num_samples, False)
    return samples[:, indices].T


def split_chains(chains: np.array) -> np.array:
    """Split the chains in two, threating each half as a new chain. This is often used
    to detect systematic trends in a random walk.

    Parameters
    ----------
    chains : np.array
        Numpy 3D array containing the input chains.

    Returns
    -------
    np.array
        Numpy 3D array containing the resulting chains.
    """
    half_chain_idx = math.floor(chains.shape[0] / 2)
    return np.dstack(
        [
            chains[:half_chain_idx, :, :],
            chains[half_chain_idx : 2 * half_chain_idx, :, :],
        ]
    )


def apply_to_chains(chains: np.array, f: Callable[[np.array], np.array]) -> np.array:
    """Apply a function to each sample of a group of chains.

    Parameters
    ----------
    chains : np.array
        Numpy 3D array containing the input chains.
    f : Callable[[np.array], np.array]
        Function to apply to each sample.

    Returns
    -------
    np.array
        Numpy 3D array containing the transformed samples.
    """
    n_chains = chains.shape[2]
    transformed_chains = []
    for i in range(n_chains):
        transformed_chains.append(f(chains[:, :, i].T).T)
    return np.dstack(transformed_chains)


def split_R(chains: np.array) -> np.array:
    """Compute the split-R  (or Potential Scale Reduction Factor) of each variable in
    the given chains.

    Parameters
    ----------
    chains : np.array
        Numpy 3D array containing the input chains.

    Returns
    -------
    np.array
        Vector containing the split-R value for each variable.
    """
    chains = split_chains(chains)
    n_steps, n_params, n_chains = chains.shape
    R = np.empty(n_params)

    # Iterate over parameters.
    for i in range(n_params):
        chain_means = np.mean(chains[:, i, :], axis=0, keepdims=True)
        sample_mean = np.mean(chain_means)
        sample_variance = (
            1 / (n_steps) * np.sum((chains[:, i, :] - chain_means) ** 2, axis=0)
        )

        # Compute between-chains variance.
        B = n_steps / (n_chains - 1) * np.sum((chain_means - sample_mean) ** 2)

        # Compute within-chain variance.
        W = 1 / n_chains * np.sum(sample_variance)

        if (
            np.all(np.abs(sample_variance / chain_means) < 1e-8)
            and np.abs(B / sample_mean) < 1e-8
        ):
            # If the variance-to-mean ratios within each chain and between all chains
            # are very low, we can assume that the variable is practically constant. Set
            # R to one in order to avoid numerical artifacts.
            R[i] = 1
        else:
            # Compute pooled variance.
            V = (n_steps - 1) / n_steps * W + 1 / n_steps * B

            # Compute potential scale reduction factor estimate.
            R[i] = np.sqrt(V / W)

    return R


def fill_common_sampling_settings(
    settings: SamplerSettings,
    log_directory: str,
    num_samples: int,
    num_steps: int,
    num_chains: int = -1,
    num_warmup_steps: int = -1,
    log_interval: datetime.timedelta = None,
):
    """Fills default values for common sampling settings.

    Parameters
    ----------
    settings : SamplerSettings
        The settings object to be filled.
    log_directory : str
        Directory in which the sampling logs should be stored.
    num_samples : int
        Number of samples to draw.
    num_steps : int
        Number of steps to take with each chain.
    num_chains : int, optional
        Number of chains to use. Will be set to the number of CPUs by default.
    num_warmup_steps : int, optional
        Number of burn-in steps to discard. Will be set to half the number of steps by
        default.
    log_interval : datetime.timedelta, optional
        Interval between each logging event.

    Raises
    ------
    ValueError
        If the inputs are inconsistent.
    """
    if num_samples < 0:
        raise ValueError("The number of samples must be positive")
    if num_chains == 0:
        raise ValueError("Sampling requires at least one chain")

    # If the number of chains is not specified, use at least as many as the number of
    # CPUs.
    if num_chains < 0:
        num_avail_cpus = os.cpu_count() or 1
        num_chains = max(num_avail_cpus, default_min_chains)

    # If the number of warmup steps is not specified, set it to half the number of
    # steps.
    min_steps_per_chain = math.ceil(num_samples / num_chains)
    if num_warmup_steps < 0:
        num_warmup_steps = math.ceil(num_steps / 2)
    if num_warmup_steps + min_steps_per_chain > num_steps:
        raise ValueError(
            "The chosen number of steps is insufficient for the chosen number of "
            "samples"
        )

    # Compute the steps thinning and adjust the total steps count if needed.
    samples_per_chain = math.ceil(num_samples / num_chains)
    steps_thinning = math.ceil((num_steps - num_warmup_steps) / samples_per_chain)
    num_steps = num_warmup_steps + samples_per_chain * steps_thinning

    log_interval = log_interval or datetime.timedelta(seconds=1)

    settings.num_steps = num_steps
    settings.num_chains = num_chains
    settings.steps_thinning = steps_thinning
    settings.num_skipped_steps = num_warmup_steps
    settings.log_interval = log_interval
    settings.log_directory = log_directory
