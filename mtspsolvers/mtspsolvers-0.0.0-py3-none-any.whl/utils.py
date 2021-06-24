import math
from enum import Enum

import matplotlib.pyplot as plt
import numpy as np


class SolutionStatus(Enum):
    solve = 1
    feasible = 2
    infeasible = 3
    opt = 4


def get_circular_coords(n: int,
                        r: float = 1.0):  # radius of the circle

    divisor = math.floor(360 / n)
    theta = np.arange(1, 360, divisor)  # degree
    theta_rad = theta * (np.pi / 180)
    x = r * np.cos(theta_rad)
    y = r * np.sin(theta_rad)
    coords = np.stack([x, y], axis=-1)
    return coords


def get_uniform_coords(n: int):
    coords = np.random.uniform(0.0, 1.0, size=(n, 2))
    return coords


def visualize_solution(info):
    x, y = info['coords'][:, 0], info['coords'][:, 1]

    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.scatter(x[1:], y[1:], c='C0', label='city')
    ax.scatter(x[0], y[0], c='C2', marker='^', label='depot')
    for m, tour in info['tours'].items():
        tour_x = x[tour]
        tour_y = y[tour]
        ax.plot(tour_x, tour_y, label='Tour {}'.format(m))
    plt.legend(loc='best')
    ax.legend()


def summary_solution(info):
    print("== Minmax mTSP {} x {} ==".format(info['n'], info['m']))
    print("Solution method : {}".format(info['solution_method']))
    print("Makespan : {:.5f}".format(info['obj_val']))
    print("Amplitude : {:.5f}".format(info['amplitude']))
    print("Total tour length: {:.5f}".format(info['total_length']))
    print("Num inactive salesmen: {}".format(info['n_inactive']))
    print("Utilization ratio : {:.2f}".format(info['utilization']))
    print("Run time : {:.2f}".format(info['run_time']))
    visualize_solution(info)


def process_tour_info(tours, coords):
    tour_length_dict = dict()
    total_tour_length = 0.0
    n_inactive = 0

    x, y = coords[:, 0], coords[:, 1]

    for m, tour in tours.items():
        tour_len = 0.0
        prev_x, prev_y = x[0], y[0]
        for dst_i in tour:
            cur_x, cur_y = x[dst_i], y[dst_i]
            tour_len += np.sqrt((prev_x - cur_x) ** 2 + (prev_y - cur_y) ** 2)
        tour_length_dict[m] = tour_len

        total_tour_length += tour_len
        if tour_len <= 0.0:
            n_inactive += 1

    max_tour_len = max(tour_length_dict.values())
    min_tour_len = min(tour_length_dict.values())
    amplitude = max_tour_len - min_tour_len
    return tour_length_dict, amplitude, total_tour_length, n_inactive
