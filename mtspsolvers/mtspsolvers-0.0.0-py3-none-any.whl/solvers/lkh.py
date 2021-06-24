import os
import uuid
from time import perf_counter

import numpy as np

from mTSPsolvers.utils import process_tour_info


def solve_lkh(m: int,
              n: int = None,
              coords: np.ndarray = None,
              seed: int = None,
              file_path: str = None,
              max_candidates: int = 6,
              max_trials: int = 10000,
              runs: int = 1,
              scale: int = 100000,
              LKH_path: str = '~/LKH-3.0.6'):
    """
    This script is a simple python interface to a compiled
    version of the LKH TSP Solver. It requires that the
    solver is compiled at the given directories.
    """

    if seed is not None:
        np.random.seed(seed)

    assert n is None or coords is None
    if n is not None:  # generate positions on fly.
        # the first city serves as the depot following the convention
        coords = np.random.uniform(size=(n, 2))
        xy_max = np.max(coords)
    if coords is not None:
        # normalize the coordinates to be in [0,1] x [0,1] range
        # for better precision for LKH3 algorithm
        xy_max = np.max(coords)
        _coords = coords  # original
        coords = coords / xy_max  # normalized
        n = coords.shape[0]

    if file_path is None:
        u_id = str(uuid.uuid4())[:4]
        file_path = os.path.join(os.getcwd(), u_id)

    atsp_file_path = file_path + '.atsp'
    par_file_path = file_path + '.par'
    tour_file_path = file_path + '.tour'

    # write *.atsp file
    with open(atsp_file_path, 'w') as f:
        f.write('NAME : {}-{}X{}\n'.format(atsp_file_path, n, m))
        f.write('TYPE: TSP \n')
        f.write('DIMENSION : {} \n'.format(n))
        f.write('SALESMEN : {} \n'.format(m))
        f.write('EDGE_WEIGHT_TYPE : EUC_2D \n')
        f.write('NODE_COORD_SECTION \n')
        for i, coord in enumerate(coords, start=1):
            f.write('{} {} {} \n'.format(i, coord[0], coord[1]))
        f.write('EOF')

    # write *.par file
    with open(par_file_path, 'w') as f:
        f.write('SPECIAL \n')
        f.write('PROBLEM_FILE = {} \n'.format(atsp_file_path))
        f.write('MAKESPAN = YES \n')
        f.write('MTSP_OBJECTIVE = MINMAX \n')
        f.write('MAX_CANDIDATES = {} \n'.format(max_candidates))
        f.write('MAX_TRIALS = {} \n'.format(max_trials))
        f.write('RUNS = {} \n'.format(runs))
        f.write('SCALE = {} \n'.format(scale))
        f.write('TOUR_FILE = {}'.format(tour_file_path))

    # invoke LKH solver
    lkh_run = os.path.join(LKH_path, 'LKH') + ' ' + par_file_path
    start_time = perf_counter()
    os.system(lkh_run)
    end_time = perf_counter()

    # parse *.tour file
    with open(tour_file_path, 'r') as f:
        result = f.read()

    # WARNING : tour results may not be correct!
    # The tour file of LKH works somewhat differently for some reason.
    # However, the objective value should be correct!
    result = result.split('\n')
    obj_val = float(result[1].replace('_', '.').split(' ')[-1]) / 100000
    tours_str = result[result.index('TOUR_SECTION') + 1: result.index('-1')]
    tours_int = np.array([int(t) for t in tours_str])

    tours = dict()
    salesman_i = 0
    tour = []
    for dim_i in tours_int:
        if dim_i >= n:
            tours[salesman_i] = [0] + list(map(int, tour)) + [0]
            salesman_i += 1
            tour = []
            continue
        tour.append(dim_i)

    # cleanup files
    os.remove(atsp_file_path)
    os.remove(par_file_path)
    os.remove(tour_file_path)

    info = dict()
    # meta info
    info['solution_method'] = 'LKH3'
    info['n'] = n
    info['m'] = m
    info['coords'] = _coords

    # solution and solver conditions
    info['obj_val'] = obj_val * xy_max
    info['tours'] = tours
    info['run_time'] = end_time - start_time

    # additional performance metrics
    tour_length_dict, amplitude, total_tour_length, n_inactive = process_tour_info(tours, coords)
    info['amplitude'] = amplitude
    info['total_length'] = total_tour_length  # minsum objective val.
    info['tour_length'] = tour_length_dict
    info['n_inactive'] = n_inactive
    info['utilization'] = (m - n_inactive) / m
    return info
