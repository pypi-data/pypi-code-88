
from oap.lib import floodfill
from oap.utils import barycenter
from oap.__conf__ import MARKER, SLICE_SIZE


def area_ratio(array):
    pass


def korolev_correction(array):
    pass


def poisson_spot(array, check_y=False, slice_size=SLICE_SIZE):
    """
    If the particle has a Poisson spot, the function fills the spot
    with a marker. In this case it returns the size of the spot.

    If the Poisson spot is not closed in x-direction, it is not possible
    to measure the spot size. In this case false is returned.
    If check_y is true, the Poisson spot must also be closed in y-direction.

    :param array:       optical array (particle image)
    :type array:        numpy array (1 dimensional) or list or string

    :param check_y      the poisson spot must close in y-direction as well
    :type check_y       boolean

    :param slice_size:  width of the optical array (number of diodes)
    :type slice_size:   integer

    :return:            if spot is closed, returns spot size, else returns false
    """
    bary = barycenter(array, slice_size=slice_size)
    floodfill(array, *bary, MARKER['poisson'], slice_size=slice_size)

    # Check if the Poisson spot is closed. If the sides of a particle image are
    # colored with the Poisson spot marker, the spot cannot be closed.
    spot_is_closed = True

    for y in range(int(len(array) / slice_size)):
        if array[y * slice_size] == MARKER['poisson'] or array[y * slice_size + (slice_size - 1)] == MARKER['poisson']:
            spot_is_closed = False

    if spot_is_closed and check_y:
        for x in range(slice_size):
            if array[x] == MARKER['poisson']\
                    or array[int(((len(array) / slice_size) - 1) * slice_size + x)] == MARKER['poisson']:
                spot_is_closed = False

    # If the spot is not closed, the Poisson Spot marker gets deleted.
    if not spot_is_closed:
        for y in range(int(len(array) / slice_size)):
            for x in range(slice_size):
                if array[y * slice_size + x] == MARKER['poisson']:
                    array[y * slice_size + x] = 0

    # If sizing is True, the function returns the Poisson Spot diameter.
    if spot_is_closed:
        min_poisson_index = slice_size - 1
        max_poisson_index = 0
        for y in range(int(len(array) / slice_size)):
            for x in range(slice_size):
                if array[y * slice_size + x] == MARKER['poisson'] and x > max_poisson_index:
                    max_poisson_index = x
                if array[y * slice_size + x] == MARKER['poisson'] and x < min_poisson_index:
                    min_poisson_index = x
        poisson_diameter = max_poisson_index - min_poisson_index + 1
        poisson_diameter = poisson_diameter if poisson_diameter > 0 else 0
        return poisson_diameter
    else:
        return False
