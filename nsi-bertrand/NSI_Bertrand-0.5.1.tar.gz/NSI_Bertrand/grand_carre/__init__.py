"""
"""

from random import random
import matplotlib.pyplot as plt
import numpy as np


def generate_grid(proportion, n, m=0):
    """Generate a grid nxm with random 1 (with proportion) or 0"""
    if m == 0:
        m = n
    return [[int(random() < proportion) for _ in range(m)] for _ in range(n)]


def trim_axs(axs, N):
    """
    Reduce *axs* to *N* Axes. All further Axes are removed from the figure.
    """
    axs = axs.flat
    for ax in axs[N:]:
        ax.remove()
    return axs[:N]


def draw_image(grid, ax):
    """Draw a grid onto an matplotlib axe"""
    hight = len(grid)
    lenght = len(grid[0])
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.imshow(grid, cmap="binary")
    ax.hlines(
        y=np.arange(0, hight) + 0.5,
        xmin=np.full(lenght, 0) - 0.5,
        xmax=np.full(lenght, hight) - 0.5,
        color="gray",
    )
    ax.vlines(
        x=np.arange(0, lenght) + 0.5,
        ymin=np.full(lenght, 0) - 0.5,
        ymax=np.full(lenght, hight) - 0.5,
        color="gray",
    )
    return ax


def grid_to_image(grid, filename):
    """Draw a grid and save it to filename"""
    plt.clf()
    fig, ax = plt.subplots()
    draw_image(grid, ax)
    plt.savefig(filename)


def grids_to_image(grids, filename, n_cols=3):
    """Draw multiple grids and save it to filename"""
    plt.clf()
    n_rows = len(grids) // n_cols
    axs = plt.figure(constrained_layout=True).subplots(n_rows, n_cols)
    axs = trim_axs(axs, len(grids))
    for ax, grid in zip(axs, grids):
        draw_image(grid, ax)

    plt.savefig(filename)


def build_largest_square_grid(grid):
    largest = [[1 for i in r] for r in grid]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell:
                largest[i][j] = 0
            elif i > 0 and j > 0:
                largest[i][j] = (
                    min(largest[i - 1][j], largest[i][j - 1], largest[i - 1][j - 1]) + 1
                )
    return largest


def trouve_plus_grand_carre(grid):
    """Find largest square in a grid with dynamic programming

    :param grid: the grid (list of list of 0 and 1)
    :returns: size of the largest square

    """
    largest = build_largest_square_grid(grid)
    return max([max(i) for i in largest])


if __name__ == "__main__":
    specs = [
        {"proportion": 0.2, "n": 5},
        {"proportion": 0.3, "n": 5},
        {"proportion": 0.2, "n": 8},
        {"proportion": 0.3, "n": 8},
        {"proportion": 0.2, "n": 10},
        {"proportion": 0.3, "n": 10},
    ]
    grids = [generate_grid(**spec) for spec in specs]
    # grid_to_image(grids[0], "grid.pdf")
    grids_to_image(grids, "grids.pdf")
    for grid in grids:
        print(trouve_plus_grand_carre(grid))
