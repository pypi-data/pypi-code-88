import copy
import datetime
import logging
import math
import multiprocessing
import os
import pickle
import random
import tempfile
from typing import List, Optional, Tuple, Union

import cvxpy as cp
import numpy as np
import pandas as pd
from scipy.stats.distributions import chi2

import _pta_python_binaries as pb
import cobra

from ..constants import (
    default_max_psrf,
    default_min_eigenvalue_tds_basis,
    default_num_samples,
    tfs_default_feasibility_cache_size,
    tfs_default_min_rel_region_length,
    tfs_steps_multiplier,
)
from ..flux_space import FluxSpace
from ..pmo import PmoProblem, PmoProblemPool
from ..thermodynamic_space import ThermodynamicSpace, ThermodynamicSpaceBasis
from ..utils import apply_transform, covariance_square_root
from .commons import (
    SamplingException,
    SamplingResult,
    apply_to_chains,
    fill_common_sampling_settings,
    sample_from_chains,
    split_R,
)
from .uniform import sample_flux_space_uniform

logger = logging.getLogger(__name__)

_us_model: cobra.Model


class TFSModel:
    """Object holding the information necessary to run TFS.

    Parameters
    ----------
    network : Union[cobra.Model, FluxSpace]
        Cobra model or `FluxSpace` object describing the flux space of the metabolic
        network.
    thermodynamic_space : ThermodynamicSpace
        Description of the thermodynamic space of the metabolic network.
    thermodynamic_space_basis : ThermodynamicSpaceBasis, optional
        A basis for the thermodynamic space. If specified, `m` will be defined in this
        basis.
    objective : Callable[ [PmoProblem], cp.problems.objective.Objective], optional
        A function used to set the optimization objective. By default the probability of
        in thermodynamic space is maximized.
    confidence_level : float, optional
        Confidence level (in the range :math:`[0.0, 1.0[`) on the joint of the
        thermodynamic variables, by default 0.95.
    min_drg : float, optional
        Minimum magnitude for the reaction energy of each reaction, by default 1e-1.
    max_drg : float, optional
        Maximum magnitude for the reaction energy of each reaction, by default 1000.
    solver : Optional[str], optional
        Name of the solver to use, this can be any of the solvers supported by CVXPY, by
        default None.
    solver_options : dict, optional
        Dictionary specifying additional options for the solver.
    """

    def __init__(
        self,
        network: Union[cobra.Model, FluxSpace],
        thermodynamic_space: ThermodynamicSpace,
        thermodynamic_space_basis: ThermodynamicSpaceBasis = None,
        confidence_level: float = 0.95,
        min_drg: float = 1e-1,
        max_drg: float = 1000,
        solver: Optional[str] = None,
        solver_options: dict = {},
    ):
        if isinstance(network, FluxSpace):
            self._F = network.copy()
        else:
            self._F = FluxSpace.from_cobrapy_model(network)
        if thermodynamic_space_basis is not None:
            self._B = thermodynamic_space_basis
            assert (
                self.B.to_drg_transform is not None
                and self.B.to_drg0_transform is None
                and self.B.to_log_conc_transform is None
            ), "Currently TFS requires a basis that represents free energies only."
        else:
            self._B = ThermodynamicSpaceBasis(
                thermodynamic_space, explicit_drg0=False, explicit_log_conc=False
            )
        self._T = thermodynamic_space

        self._confidence_level = confidence_level
        self._drg_epsilon = min_drg

        self._pmo_args = [
            self.F,
            self.T,
            self.B,
            None,
            confidence_level,
            min_drg,
            max_drg,
            solver,
            solver_options,
        ]

    @property
    def B(self) -> ThermodynamicSpaceBasis:
        """Gets the basis of the thermodynamic space used for sampling."""
        return self._B

    @property
    def T(self) -> ThermodynamicSpace:
        """Gets the thermodynamic space used for sampling."""
        return self._T

    @property
    def F(self) -> FluxSpace:
        """Gets the flux space used for sampling."""
        return self._F

    @property
    def pmo_args(self):
        """Gets the arguments used to construct PMO problems."""
        return self._pmo_args

    @property
    def dimensionality(self) -> int:
        """Gets the dimensionality of the basis of the thermodynamic space."""
        return self.B.dimensionality

    @property
    def confidence_radius(self):
        """Gets the radius of the selected confidence region."""
        return math.sqrt(chi2.ppf(self._confidence_level, self.B.dimensionality))

    @property
    def drg_epsilon(self):
        """Gets the minimum magnitude of the reaction energy of irreversible
        reactions."""
        return self._drg_epsilon

    @property
    def reversible_rxn_ids(self):
        """Gets the identifiers of the reversible reactions in the thermodynamic
        space."""
        return [
            id
            for i, id in enumerate(self.F.reaction_ids)
            if self.F.lb[i] < 0 and self.F.ub[i] > 0 and id in self.T.reaction_ids
        ]

    def to_drg(self, value: np.array) -> np.array:
        """Transform a point or matrix from the the basis to reaction energies.

        Parameters
        ----------
        value : np.array
            Input values in the basis.

        Returns
        -------
        np.array
            The corresponding reaction energies.
        """
        assert self.B.to_drg_transform is not None
        return apply_transform(value, self.B.to_drg_transform)


class FreeEnergiesSamplingResult(SamplingResult):
    """Encapsulates the result of sampling reaction energies.

    Parameters
    ----------
    samples : pd.DataFrame
        Data frame containing the free energy samples.
    psrf : pd.Series
        The Potential Scale Reduction Factors of each variable.
    orthants : pd.DataFrame
        Data frame containing the signs of the reversible reactions for each orthants.
        Contains an additional column ("weight") describing the weight of the orthant.
    """

    def __init__(
        self,
        samples: pd.DataFrame,
        psrf: pd.Series,
        orthants: pd.DataFrame,
    ):
        SamplingResult.__init__(self, samples, psrf)
        self._orthants = orthants

    @property
    def orthants(self) -> pd.DataFrame:
        """Gets a data frame containing the sampled orthants. Contains an additional
        column ("weight") describing the weight of the orthant."""
        return self._orthants


def _find_point(problem: PmoProblem, flux_objective: Tuple[int, int]) -> np.array:
    # First, find an orthant with the given direction (if possible).
    problem.objective = lambda p: cp.Maximize(
        flux_objective[1] * p.d[flux_objective[0]]
    )
    result = problem.solve()

    if result != "optimal":
        logger.warning(
            f"Initial points search failed for reaction {flux_objective[0]} in "
            f"direction {flux_objective[1]} with status {result}."
        )
        return None

    # Next, restrict PMO to the orthant found and search for a point maximizing the
    # distance from all the constraints.
    orthant_problem = problem.rebuild_for_directions(problem.d.value)
    assert orthant_problem.B.to_drg_transform is not None
    (T, s) = orthant_problem.B.to_drg_transform
    CI_square = chi2.ppf(
        orthant_problem._confidence_level, orthant_problem.B.dimensionality
    )

    distance = cp.Variable(name="distance", nonneg=True)
    row_norms = np.linalg.norm(
        orthant_problem.B.to_drg_transform[0], ord=2, axis=1, keepdims=True
    )

    orthant_problem._constraints.extend(
        [
            cp.multiply(orthant_problem._big_M_r, orthant_problem.d)
            + T @ orthant_problem.m
            + row_norms * distance
            + s
            <= orthant_problem._big_M_r - orthant_problem._epsilon_r,
            cp.multiply(orthant_problem._big_M_r, orthant_problem.d)
            + T @ orthant_problem.m
            + row_norms * distance
            + s
            >= orthant_problem._epsilon_r,
            cp.atoms.quad_form(
                orthant_problem.m, np.identity(orthant_problem.B.dimensionality)
            )
            + cp.square(distance)
            <= CI_square,
        ]
    )
    orthant_problem.objective = lambda p: cp.Maximize(distance)

    orthant_problem.solve()
    if result != "optimal":
        logger.warning(
            f"Initial points search failed for reaction {flux_objective[0]} in "
            f"direction {flux_objective[1]} with status {result}."
        )
        return None
    else:
        logger.info(f"Found initial point with distance {distance.value}")
        return orthant_problem.drg


def get_initial_points(model: TFSModel, num_points: int) -> np.array:
    """Gets initial points for sampling reaction energies.

    Parameters
    ----------
    model : TFSModel
        The model to sample.
    num_points : int
        Number of initial points to generate.

    Returns
    -------
    np.array
        Array containing the initial points.
    """

    # Create the process pool for solving PMO problems.
    pool = PmoProblemPool(None, *model._pmo_args)

    # Find candidate optimization direactions.
    reaction_idxs_T = list(range(len(model.T.reaction_ids)))
    reaction_idxs_F = [model.F.reaction_ids.index(id) for id in model.T.reaction_ids]
    only_forward_ids_T = [
        i for i in reaction_idxs_T if model.F.lb[reaction_idxs_F[i]] >= 0
    ]
    only_backward_ids_T = [
        i for i in reaction_idxs_T if model.F.ub[reaction_idxs_F[i]] <= 0
    ]
    reversible_ids_T = [
        i
        for i in reaction_idxs_T
        if model.F.lb[reaction_idxs_F[i]] < 0 and model.F.ub[reaction_idxs_F[i]] > 0
    ]

    reversible_dirs = [(i, -1) for i in reversible_ids_T] + [
        (i, 1) for i in reversible_ids_T
    ]
    irreversible_dirs = [(i, -1) for i in only_backward_ids_T] + [
        (i, 1) for i in only_forward_ids_T
    ]

    # Select optimization directions, giving precedence to the reversible reactions.
    if num_points >= len(reversible_dirs):
        directions = reversible_dirs
        directions_pool = irreversible_dirs
        to_sample = min(num_points - len(reversible_dirs), len(irreversible_dirs))
    else:
        directions = []
        directions_pool = reversible_dirs
        to_sample = min(num_points, len(reversible_dirs))
    optimization_directions = random.sample(directions_pool, to_sample)

    # Run the optimizations in the pool.
    initial_points = pool.map(_find_point, optimization_directions)
    points_array = np.hstack(initial_points)
    pool.close()

    return points_array


def sample_drg(
    model: TFSModel,
    num_samples: int = default_num_samples,
    num_direction_samples: int = default_num_samples,
    initial_points: np.array = None,
    num_steps: int = -1,
    num_warmup_steps: int = -1,
    num_chains: int = -1,
    log_interval: datetime.timedelta = None,
    max_psrf: float = default_max_psrf,
    feasibility_cache_size: int = tfs_default_feasibility_cache_size,
    min_rel_region_length: float = tfs_default_min_rel_region_length,
) -> FreeEnergiesSamplingResult:
    """Sample reaction energies under steady state flux constraints in the given model.

    Parameters
    ----------
    model : TFSModel
        The model to sample.
    num_samples : int, optional
        Number of samples to draw.
    num_direction_samples : int, optional
        Number of orthant samples to collect.
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
    feasibility_cache_size : int, optional
        Maximum size of the cache storing the feasibility of the orthants encountered
        during the random walk.
    min_rel_region_length : float, optional
        Minimum length (relative to the length of the entire ray) of a segment in order
        to consider it for sampling.

    Returns
    -------
    FreeEnergiesSamplingResult
        The sampling result.

    Raises
    ------
    SamplingException
        If sampling fails.
    """
    if num_steps < 0:
        num_steps = model.dimensionality ** 2 * tfs_steps_multiplier
    if initial_points is not None and num_chains < 0:
        num_chains = initial_points.shape[1]

    # Fill the settings.
    settings = pb.FreeEnergySamplerSettings()
    fill_common_sampling_settings(
        settings,
        "",
        num_samples,
        num_steps,
        num_chains,
        num_warmup_steps,
        log_interval,
    )
    settings.truncation_multiplier = model.confidence_radius
    settings.feasibility_cache_size = feasibility_cache_size
    settings.drg_epsilon = model.drg_epsilon
    settings.flux_epsilon = 1e-4  # TODO: make this an actual setting.
    settings.min_rel_region_length = min_rel_region_length
    settings.steps_thinning_directions = math.floor(
        (settings.num_steps - settings.num_skipped_steps)
        / math.ceil(num_direction_samples / settings.num_chains)
    )
    assert settings.steps_thinning_directions > 0, (
        "Unable to generate that many direction samples with the current settings. "
        "Please select a larger number of steps or chains."
    )

    # Generate initial points if needed.
    if initial_points is None:
        initial_points = get_initial_points(model, settings.num_chains)
    assert (
        initial_points.shape[1] == settings.num_chains
    ), "Sampling requires the same number of initial points and chains."

    logger.info(
        f"Starting thermodynamic space sampler with {settings.num_chains} chains and "
        f"{settings.num_steps} steps."
    )

    try:
        # TODO: calling the sampler this way is only correct when the thermodynamic
        # space basis only represents reaction energies.
        assert model.B.to_drg_transform is not None
        tfs_result: pb.TFSResult = pb.sample_free_energies(
            model.B.to_drg_transform[0],
            model.B.to_drg_transform[1],
            model.F.S,
            model.F.lb,
            model.F.ub,
            np.array(
                [[model.F.reaction_ids.index(id) for id in model.T.reaction_ids]],
                dtype=np.uint32,
            ).T,
            initial_points,
            settings,
            np.identity(model.B.to_drg_transform[1].size),
            np.zeros_like(model.B.to_drg_transform[1]),
            np.identity(model.dimensionality),
        )
    except Exception as e:
        logger.error(f"Sampling of the thermodynamic space failed. {e}")
        raise SamplingException("Sampling of the thermodynamic space failed.") from e
    else:
        logger.info("Sampling completed.")
        samples = sample_from_chains(tfs_result.chains, num_samples)

        logger.info("Computing PSRFs.")
        psrf_var_names = model.T.reaction_ids
        psrf = split_R(tfs_result.chains)

        # Convert the orthants from binary to integer description.
        orthant_signs = np.unpackbits(tfs_result.directions, bitorder="little", axis=1)[
            :, : len(model.reversible_rxn_ids)
        ].astype(np.int8)
        orthant_signs[orthant_signs == 0] = -1

        orthants = pd.DataFrame(
            orthant_signs,
            columns=model.reversible_rxn_ids,
        )
        orthant_weights = pd.DataFrame(tfs_result.direction_counts, columns=["weight"])

        result = FreeEnergiesSamplingResult(
            pd.DataFrame(samples, columns=model.T.reaction_ids),
            pd.Series(psrf, index=psrf_var_names),
            orthant_weights.join(orthants),
        )

        if result.check_convergence(max_psrf):
            logger.info("Convergence criteria satisfied.")
        else:
            logger.warning(
                "Sampling of the thermodynamic space did not converge. Please try "
                "increasing the number of steps."
            )

        return result


def sample_log_conc_from_drg(
    thermodynamic_space: ThermodynamicSpace,
    drg_samples: pd.DataFrame,
    min_eigenvalue: float = default_min_eigenvalue_tds_basis,
) -> pd.DataFrame:
    """Sample the natural logarithm of the metabolite concentrations conditioned on
    samples of free energies. This function draws one sample for each sample of reaction
    energies.

    Parameters
    ----------
    thermodynamic_space : ThermodynamicSpace
        The thermodynamic space of the network.
    drg_samples : pd.DataFrame
        Data frame containing the samples of reaction energies.
    min_eigenvalue : float, optional
        Minimum eigenvalue to keep when performing the truncated SVD of the covariance
        of the conditional probability.

    Returns
    -------
    pd.DataFrame
        Data frame containing the log-concentration samples.
    """
    basis = ThermodynamicSpaceBasis(
        thermodynamic_space,
        explicit_drg=True,
        explicit_drg0=False,
        explicit_log_conc=True,
        min_eigenvalue=min_eigenvalue,
    )

    log_conc_samples = _sample_conditional_mvn(
        basis.to_observables_transform[1],
        basis.to_observables_transform[0],
        drg_samples.to_numpy().T,
        basis.observables_ranges["log_conc"],
        min_eigenvalue,
    )

    return pd.DataFrame(log_conc_samples.T, columns=thermodynamic_space.metabolite_ids)


def sample_drg0_from_drg(
    thermodynamic_space: ThermodynamicSpace,
    drg_samples: pd.DataFrame,
    min_eigenvalue: float = default_min_eigenvalue_tds_basis,
) -> pd.DataFrame:
    """Sample standard reaction energies conditioned on samples of reaction energies.
    This function draws one sample for each sample of reaction energies.

    Parameters
    ----------
    thermodynamic_space : ThermodynamicSpace
        The thermodynamic space of the network.
    drg_samples : pd.DataFrame
        Data frame containing the samples of reaction energies.
    min_eigenvalue : float, optional
        Minimum eigenvalue to keep when performing the truncated SVD of the covariance
        of the conditional probability.

    Returns
    -------
    pd.DataFrame
        Data frame containing the standard reaction energy samples.
    """
    basis = ThermodynamicSpaceBasis(
        thermodynamic_space,
        explicit_drg=True,
        explicit_drg0=True,
        explicit_log_conc=False,
        min_eigenvalue=min_eigenvalue,
    )

    drg0_samples = _sample_conditional_mvn(
        basis.to_observables_transform[1],
        basis.to_observables_transform[0],
        drg_samples.to_numpy().T,
        basis.observables_ranges["drg0"],
        min_eigenvalue,
    )

    return pd.DataFrame(drg0_samples.T, columns=thermodynamic_space.reaction_ids)


def _init_us_worker(args_filename):
    global _us_model
    _us_model = pickle.load(open(args_filename, "rb"))


def _sample_orthant(args: Tuple[np.array, np.array, int]) -> pd.DataFrame:
    global _us_model
    model = _us_model
    for i in range(len(model.reactions)):
        model.reactions[i].lower_bound = args[0][i]
        model.reactions[i].upper_bound = args[1][i]
    return sample_flux_space_uniform(
        model, args[2], num_chains=1, check_convergence=False
    ).samples


def _get_sample_weight(orthant_weights, orthant_signs, sample_signs):
    result = np.where(np.all(orthant_signs == sample_signs, axis=1))[0]
    if len(result) == 1:
        return orthant_weights.iloc[result[0]]
    elif len(result) == 0:
        return 1
    else:
        raise Exception("Direction samples should be unique.")


def sample_fluxes_from_drg(
    model: cobra.Model,
    drg_samples: pd.DataFrame,
    orthants: pd.DataFrame,
    num_approx_samples: int = default_num_samples,
) -> pd.DataFrame:
    """Sample the flux space using the samples of orthant of reaction energies and
    orthants as prior. For each unique orthant implied by the reaction energy samples,
    this function draws a number of uniform flux samples proportional to the probability
    of the orthant in the thermodynamic space.

    Parameters
    ----------
    model : cobra.Model
        cobrapy model describing the flux space.
    drg_samples : pd.DataFrame
        The input reaction energy samples.
    orthants : pd.DataFrame
        Data frame containing the sampled orthants and their weights.
    num_approx_samples : int, optional
        Approximate number of samples to draw.

    Returns
    -------
    pd.DataFrame
        Data frame containing the flux samples.
    """
    # Get the signs of the reversible reactions for each orthant.
    reversible_rxns_ids = list(orthants.columns)
    reversible_rxns_ids.remove("weight")
    orthant_signs = orthants[reversible_rxns_ids].to_numpy()

    # Get the signs of the reversible reactions for each sample of drg.
    drg_samples = drg_samples[reversible_rxns_ids]
    samples_signs = np.unique(np.where(drg_samples < 0, 1, -1), axis=0).astype(np.int8)

    # Find the weight of the orthant corresponding to each sample of drg.
    samples_weights = np.array(
        [
            _get_sample_weight(orthants["weight"], orthant_signs, samples_signs[i, :])
            for i in range(samples_signs.shape[0])
        ]
    )

    # Scale the weights to obtain approximately the requested number of samples.
    num_orthant_samples = samples_weights / np.sum(samples_weights) * num_approx_samples
    to_round_up = np.random.rand(num_orthant_samples.size) < (
        num_orthant_samples - np.floor(num_orthant_samples)
    )
    num_orthant_samples = num_orthant_samples.astype(np.int64) + np.where(
        to_round_up, 1, 0
    )

    worker_args = []
    original_lb = np.array([r.lower_bound for r in model.reactions])
    original_ub = np.array([r.upper_bound for r in model.reactions])
    rev_rxns_idxs_F = [model.reactions.index(id) for id in reversible_rxns_ids]
    for i in range(num_orthant_samples.size):
        if num_orthant_samples[i] > 0:
            lb = original_lb.copy()
            ub = original_ub.copy()
            rev_lb = -np.ones(len(rev_rxns_idxs_F)) * np.inf
            rev_ub = np.ones(len(rev_rxns_idxs_F)) * np.inf
            rev_lb[samples_signs[i, :] > 0] = 0
            rev_ub[samples_signs[i, :] < 0] = 0
            lb[rev_rxns_idxs_F] = np.maximum(lb[rev_rxns_idxs_F], rev_lb)
            ub[rev_rxns_idxs_F] = np.minimum(ub[rev_rxns_idxs_F], rev_ub)
            worker_args.append((lb, ub, num_orthant_samples[i]))

    # Create process pool and run uniform sampling on each orthant.
    num_processes = multiprocessing.cpu_count()
    if num_processes is None:
        logger.warning(
            "Cannot determine the number of processors available. Assuming 1."
        )
        num_processes = 1

    with tempfile.NamedTemporaryFile(delete=False) as args_file:
        pickle.dump(model, open(args_file.name, "wb"))
        args_filename = args_file.name

    pool = multiprocessing.Pool(
        num_processes,
        initializer=_init_us_worker,
        initargs=[args_filename],
    )
    pool_result = pool.map(_sample_orthant, worker_args)
    samples = pd.concat(pool_result, ignore_index=True)

    pool.close()
    pool.join()
    if os.path.isfile(args_filename):
        os.remove(args_filename)

    return samples


def _sample_conditional_mvn(
    mean: np.array,
    cov_sqrt: np.array,
    Y_samples: np.array,
    X_ids: List[int],
    min_eigenvalue: float = default_min_eigenvalue_tds_basis,
) -> np.array:
    """ Samples from the probability density of X conditioned on Y. """
    Y_ids = sorted(list(set(range(mean.size)) - set(X_ids)))

    # https://en.wikipedia.org/wiki/Schur_complement
    # [a; b] * [a; b]' = [A, B; B', C]
    a = cov_sqrt[X_ids, :]
    b = cov_sqrt[Y_ids, :]

    A = a @ a.T
    B = a @ b.T
    C = b @ b.T
    A_inv = np.linalg.pinv(A, hermitian=True)
    C_inv = np.linalg.pinv(C, hermitian=True)

    E_X = mean[X_ids]
    E_Y = mean[Y_ids]

    X_cov = A - B @ C_inv @ B.T
    std_mvn_to_X_transform = (
        covariance_square_root(X_cov, min_eigenvalue),
        np.zeros_like(E_X),
    )
    X_means = E_X + B @ C_inv @ (Y_samples - E_Y)

    n_samples = Y_samples.shape[1]
    n_dimensions = std_mvn_to_X_transform[0].shape[1]
    standard_samples = np.random.multivariate_normal(
        np.zeros(n_dimensions), np.identity(n_dimensions), n_samples
    ).T

    return apply_transform(standard_samples, std_mvn_to_X_transform) + X_means
