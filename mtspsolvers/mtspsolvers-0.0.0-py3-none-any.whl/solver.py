from functools import partial

import numpy as np


def solve_mTSP(method: str,
               m: int,
               n: int = None,
               coords: np.ndarray = None,
               **kwargs):
    """
    :param method: (str) Solution method; one of ['cplex', 'ortools', 'lkh']
    :param n: (int) Number of cities; including the depot.
    :param m: (int) Number of salesman
    :param coords: (np.ndarray) 2D cartesian coordinates of the cities; the first city serves as the dep
    :param kwargs: optional keyword arguments for the solvers
    :return:
    """

    assert method in ['cplex', 'ortools', 'lkh', 'NI', 'FI', 'RI']

    if method == 'ortools':
        from mTSPsolvers.solvers.ortools import solve_ortools
        _solve = solve_ortools
    elif method == 'cplex':
        from mTSPsolvers.solvers.cplex import solve_cplex
        _solve = solve_cplex
        if n is not None:
            n -= 1
    elif method == 'lkh':
        from mTSPsolvers.solvers.lkh import solve_lkh
        _solve = solve_lkh
    elif method in ['NI', 'FI', 'RI']:
        from mTSPsolvers.solvers.twophase import solve_twophase
        _solve = partial(solve_twophase, tsp_heuristics=method)
    else:
        raise RuntimeError("{} is not implemented solution method".format(method))

    info = _solve(n=n, m=m, coords=coords, **kwargs)
    return info
