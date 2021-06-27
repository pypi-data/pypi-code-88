# author: Drew Botwinick, Botwinick Innovations
# license: 3-clause BSD

from math import ceil, copysign

import numpy as np

from .cartesian import Line2D, distance
from ..maths.precision import snap_to_increment


def grid_walk_2d(x1, y1, x2, y2, grid_size=1):
    """
    Naive grid walking algorithm for a regular 2D grid with a given grid size with no obstructions. Finds a reasonable stable
    path through the grid based on trying to stay close to a given line. No guarantees on whether
    it is actually the most "cost-effective" solution either in terms of the selected path or
    computational efficiency, but it gets the job done and it's an entertaining exercise...

    The outcome of this algorithm is a path walk list hat contains (i, j) index-style outputs to indicate
    the walking path in terms of grid steps.

    Note that for best results, (x1, y1) and (x2, y2) should be on-grid to ensure that multiple walks/paths
    meet without gaps.

    :param x1: x1 (float); point 1 x; if grid size == 1, then it can also be i of (i, j) indexed coordinate pair
    :param y1: y1 (float); point 1 y; if grid size == 1, then it can also be j of (i, j) indexed coordinate pair
    :param x2: x2 (float); point 2 x; if grid size == 1, then it can also be i of (i, j) indexed coordinate pair
    :param y2: y2 (float); point 2 y; if grid size == 1, then it can also be j of (i, j) indexed coordinate pair
    :param grid_size: grid size (float); default of 1 means that the grid_walk can be performed directly on indices
    :return: list of (i, j) tuples that indicate the walking path in terms of grid indices
    :rtype: list[tuple[int, int]]
    """
    # target line characteristics
    target_line = Line2D([x1, y1], [x2, y2])
    start = target_line.start
    end = target_line.end
    dx, dy = dxy = target_line.dxy
    m = target_line.slope

    # use slope to determine on-axis and off-axis directions
    axes = [0, 1] if abs(m) < 1 else [1, 0]  # whether we perform calculations as x-dominant or y-dominant depends on the slope of the line
    a0, a1 = axes
    a0d = end[a0] - start[a0]  # target distance to travel in on-axis direction

    # start from aspect ratio based step size in the x and y to derive initial position guess
    initial_steps = np.asarray([copysign(ceil(abs(dx / (dy or 1))), dx), copysign(ceil(abs(dy / (dx or 1))), dy)], dtype=np.int64)

    path = []
    iteration = 0
    steps = np.empty_like(initial_steps)
    new_position = start

    # grid_diagonal = grid_size * sqrt(2.0)
    # loop while we have distance to travel greater than 1 grid diagonal or if the position isn't changing
    while distance(new_position, end) >= 0.5 * grid_size and \
            ((new_position[a0] - start[a0] < a0d) if dxy[a0] >= 0 else (new_position[a0] - start[a0] > a0d)):
        position = new_position  # we do this at the beginning of the loop to enable more loop control options

        # determine current/other axis (i.e. we alternate between x- and y- direction movement)
        ca = axes[iteration % 2]
        oa = axes[(iteration % 2) - 1]

        # reset steps
        steps[:] = initial_steps  # start from initial slope/aspect-ratio based guess; alter array but preserve reference
        steps[oa] = 0  # we don't move in the other axis

        # do corrections as needed
        if ca == a1:  # for movement on the off-axis (i.e. adjust "grid traversal aspect ratio" compared to line slope)
            oat = target_line.fn(a1, position[a0])  # off-axis target position given current on-axis position [changed last iteration]
            error = oat - (position[a1] + steps[ca] * grid_size)  # calculate tentative new position as part of determining error
        elif ca == a0 and abs(steps[a0]) > 1:  # for on-axis, we check if we're going to overshoot and try to correct it if possible
            projected_end = snap_to_increment(end[ca] - position[ca], steps[ca] * grid_size, position[ca])
            error = projected_end - end[ca]
        else:
            error = 0

        # adjust walk steps based on accumulated error (or predicted future error)
        steps[ca] += int(round(snap_to_increment(error, grid_size) / grid_size, 0))

        # store integer path movements if movement was registered
        if np.abs(steps).max() > 0:
            path.append((int(steps[0]), int(steps[1])))

        # prepare for next loop iteration
        new_position = position + steps * grid_size  # calculate new position
        iteration += 1

    return path
