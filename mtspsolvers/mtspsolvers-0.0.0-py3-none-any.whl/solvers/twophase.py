from time import perf_counter

import numpy as np
import pandas as pd
import scipy.spatial.distance as sp_dist
from sklearn.cluster import KMeans


def get_next_city_idx(dist_series: pd.Series,
                      tsp_heuristics: str):
    if tsp_heuristics == 'NI':
        n_city = dist_series.argmin()  # index in position
    elif tsp_heuristics == 'FI':
        n_city = dist_series.argmax()
    elif tsp_heuristics == 'RI':
        n_city = np.random.choice(dist_series.shape[0])
    else:
        raise RuntimeError
    return n_city


def solve_twophase(m: int,  # Number of salesmen
                   n: int = None,  # Number of cities including the depot
                   coords: np.ndarray = None,  # Depot and cities positions [ n x 2]
                   tsp_heuristics: str = 'NI',
                   seed: int = None):  # random seed for generating city positions

    if seed is not None:
        np.random.seed(seed)

    assert n is None or coords is None
    if n is not None:  # generate positions on fly.
        # the first city serves as the depot following the convention
        coords = np.random.uniform(size=(n, 2))
        depot_coord = coords[0:1, :]
        city_coord = coords[1:, :]
    if coords is not None:
        n = coords.shape[0]
        depot_coord = coords[0:1, :]
        city_coord = coords[1:, :]

    start_time = perf_counter()
    kmeans = KMeans(n_clusters=m, random_state=0).fit(city_coord)

    assigned_cities = {_m: np.arange(1, n)[kmeans.labels_ == _m] for _m in range(m)}
    tours = dict()
    tour_length = dict()
    for _m in range(m):
        if len(assigned_cities[_m]) == 0:  # Not assigned to any city
            tours[_m] = []
            tour_length[_m] = 0.0
        elif len(assigned_cities[_m]) == 1:  # Assigned to a single city
            city_i = int(assigned_cities[_m][0])
            tours[_m] = [city_i]
            # the depot returning cost
            tour_length[_m] = 2 * sp_dist.cdist(depot_coord, city_coord[city_i - 1:city_i, :], metric='euclidean')
        else:
            sub_coords = np.vstack([depot_coord, city_coord[assigned_cities[_m] - 1, :]])
            sub_dists = sp_dist.cdist(sub_coords, sub_coords, metric='euclidean')

            # initialize the tour
            cur_city_idx = 0  # depot start
            tour = []
            tour_len = 0.0

            unvisit_cities = assigned_cities[_m].tolist()  # except the depot
            cities = [0] + unvisit_cities  # including depot as the initial city.
            dist_df = pd.DataFrame(sub_dists, index=cities, columns=cities)

            while len(unvisit_cities) >= 1:
                cur_df = dist_df.loc[cur_city_idx][dist_df.loc[cur_city_idx] > 0.0]
                n_city_idx = cur_df.index[get_next_city_idx(cur_df, tsp_heuristics)]

                tour_len += float(cur_df.loc[n_city_idx])
                tour.append(int(n_city_idx))
                dist_df = dist_df.drop(columns=cur_city_idx)
                unvisit_cities.remove(n_city_idx)
                cur_city_idx = n_city_idx

            tours[_m] = tour
            tour_length[_m] = float(tour_len + dist_df.loc[0])  # add depot returning cost
    end_time = perf_counter()

    info = dict()

    # meta info
    info['solution_method'] = '2phase-{}'.format(tsp_heuristics)
    info['n'] = int(n)
    info['m'] = int(m)
    info['coords'] = coords

    # solution and solver conditions
    info['solve'] = True
    info['obj_val'] = max(tour_length.values())
    info['run_time'] = end_time - start_time
    return_tour = {k: [0] + v + [0] for k, v in tours.items()}  # appending the depot to the end and first
    info['tours'] = return_tour

    # additional performance metrics
    info['amplitude'] = max(tour_length.values()) - min(tour_length.values())
    info['total_length'] = float(sum(tour_length.values()))
    info['tour_length'] = tour_length

    n_inactive = 0
    for tl in info['tour_length'].values():
        if tl <= 0.0:
            n_inactive += 1
    info['n_inactive'] = n_inactive
    info['utilization'] = (m - n_inactive) / m

    return info
