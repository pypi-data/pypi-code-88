import warnings
from time import perf_counter

import docplex.mp.model as cpx
import numpy as np

from mTSPsolvers.utils import process_tour_info


def solve_cplex(m: int,  # Number of salesmen
                n: int = None,  # Number of cities - excluding the depot
                coords: np.ndarray = None,  # Depot and cities positions [ 1 + #.cities x 2]
                time_limit: float = -1,  # seconds
                n_workers: int = -1,  # number of parallel workers for solving mTSP problem.
                seed: int = None,  # random seed for generating city positions
                verbose: bool = False):  # report CPLEX results

    if seed is not None:
        np.random.seed(seed)

    model = cpx.Model('mTSP')

    assert n is None or coords is None
    if n is not None:  # generate positions on fly.
        # the first city serves as the depot following the convention
        loc_x, loc_y = np.random.uniform(size=n + 1), np.random.uniform(size=n + 1)
        coords = np.concatenate([loc_x, loc_y], axis=-1)
    if coords is not None:
        loc_x, loc_y = coords[:, 0], coords[:, 1]
        n = coords.shape[0] - 1  # except the depot

    if n >= 13 and m >= 6:
        warnings.warn("n > 12 and m>=3 may takes indefinitely long to solve mTSP with CPLEX.")

    T = list(range(m))  # for constructing upper bounds of tours
    S = [0]
    N = list(range(1, n + 1))
    V = [0] + N

    e = model.continuous_var_dict(T, name='e')
    X = [(i, j, k) for i in V for j in V for k in T if i != j]
    A = [(i, j) for i in V for j in V if i != j]
    F = [(i, k) for i in V for k in T]
    c = {(i, j): np.hypot(loc_x[i] - loc_x[j], loc_y[i] - loc_y[j]) for i, j in A}
    y = model.continuous_var()
    model.minimize(y)

    x = model.binary_var_dict(X, name='x')
    f = model.continuous_var_dict(F, name='f')
    model.add_constraints(model.sum(c[i, j] * x[i, j, k] for i in V for j in V if j != i) <= y for k in T)
    model.add_constraints(f[0, k] == 0 for k in T)
    model.add_constraints(model.sum(x[i, j, k] for j in V if i != j) == 1 for i in S for k in T)
    model.add_constraints(model.sum(c[i, j] * x[i, j, k] for i in V for j in V if j != i) == e[k] for k in T)
    model.add_constraints(model.sum(x[i, j, k] for i in V for k in T if i != j) == 1 for j in N)
    model.add_constraints(
        model.sum(x[i, j, k] for i in V if i != j) == model.sum(x[j, h, k] for h in V if h != j) for j in N for k in T)
    model.add_indicator_constraints(
        model.indicator_constraint(x[i, j, k], f[i, k] - f[j, k] == -1) for i in V for j in N for k in T if i != j)

    if time_limit != -1:
        model.parameters.timelimit = time_limit

    if n_workers != -1:
        model.parameters.threads = n_workers

    start_time = perf_counter()
    solution = model.solve(log_output=verbose)
    end_time = perf_counter()

    info = dict()

    # meta info
    info['solution_method'] = 'CPLEX'
    info['n'] = n + 1  # cities + depot
    info['m'] = m
    info['coords'] = coords

    # method related
    # info['model'] = model
    # info['status'] = solution.solve_status

    # solution and solver conditions
    info['solve'] = True if solution.solve_status._name_ == 'OPTIMAL_SOLUTION' else False
    info['obj_val'] = solution._objective  # minmax objective val.
    info['tours'] = convert_cplex_sol_to_tours(x, m, n + 1)  # 'n+1' is the right one!
    info['run_time'] = end_time - start_time

    # additional performance metrics
    tour_length_dict, amplitude, total_tour_length, n_inactive = process_tour_info(info['tours'], coords)
    info['amplitude'] = amplitude
    info['total_length'] = total_tour_length  # minsum objective val.
    info['tour_length'] = tour_length_dict
    info['n_inactive'] = n_inactive
    info['utilization'] = (m - n_inactive) / m

    return info


def convert_cplex_sol_to_tours(cplex_x, m, n):
    """
    :param cplex_x: cplex solution matrix
    :param m: number of salesmen
    :param n: number of cities "INCLUDING the depot"
    :return:
    """

    # construct 'tour' matrix
    # sales man x src x dst
    tours = np.zeros(shape=(m, n, n))
    for i, j, k in cplex_x:
        if i != j:
            visit = 1.0 if cplex_x[i, j, k].solution_value > 0.9 else 0.0
            tours[k, i, j] = visit

    k, i, j = np.nonzero(tours)
    tour_dict = dict()
    for _m in range(m):
        # destination cities of salesman "m"
        dst_index = i[k == _m]
        tour = list(map(int, dst_index)) + [0]  # append the depot to the last; visualization purpose
        tour_dict[_m] = tour
    return tour_dict
