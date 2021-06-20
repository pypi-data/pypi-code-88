"""
Particle Diameter and other sizing methods.

Author:         Lucas Tim Grulich
Created:        March 2018
Last Update:    02. August 2019
"""

from oap.conf import KOROLEV_TABLE, SLICE_SIZE
from oap.utils.features import barycenter, particle_features, poisson_spot
from oap.utils.modifications import convert_to_monoscale
from oap.utils.transforms import scatter_array

import numpy as np

from math import sqrt, pi


# ------------------------------------------------------------------------------------------------------------------ Not perfect - Gibt die falsche y_dim an, wenn das Array nicht geclipped ist
def xy_dimension(array, monoscale=False, slicesize=SLICE_SIZE):
    """
    Measures the particle width (x dimension) and the particle length or height (y dimension)
    of a particle image as numpy array, list or string.

    If monoscale is true, the function ignores the first shadow-level.

    :param array:       optical array (particle image)
    :type array:        numpy array (1 dimensional) or list or string

    --- optional params ---
    :param monoscale:   if true method ignores first shadow level
    :type monoscale:    boolean

    :param slicesize:   width of the optical array (number of diodes)
    :type slicesize:    integer

    :return:            x- and y-dimension (2 integers)
    """
    if not len(array):
        return 0, 0

    y_dim = int(len(array) / slicesize)
    min_index = len(array)
    max_index = 0

    # With ignoring shadow-level 1, the y-dimension of the particle size
    # might change as well.
    if monoscale:
        monoscale_y_min_index = y_dim - 1
        monoscale_y_max_index = 0

    mono_pixel_no = 0

    for y in range(y_dim):
        for x in range(slicesize):

            if monoscale:
                if (array[y*slicesize+x] != 0 \
                and array[y*slicesize+x] != 1 \
                and array[y*slicesize+x] != '0' \
                and array[y*slicesize+x] != '1'):
                    mono_pixel_no += 1
                    if x > max_index:
                        max_index = x
                    if x < min_index:
                        min_index = x
                    if y < monoscale_y_min_index:
                        monoscale_y_min_index = y
                    if y > monoscale_y_max_index:
                        monoscale_y_max_index = y
            else:
                if (array[y*slicesize+x] != 0 \
                and array[y*slicesize+x] != '0'):
                    if x > max_index:
                        max_index = x
                    if x < min_index:
                        min_index = x

    if monoscale:
        if not mono_pixel_no:
            return 0, 0
        y_dim = monoscale_y_max_index - monoscale_y_min_index + 1

    x_dim = max_index - min_index + 1
    return x_dim, y_dim



def maximum_dimension(array, x=None, y=None, monoscale=False, slicesize=SLICE_SIZE): # -------------------------------------------------------------- array wird hier und bei min nicht unbedingt benötigt...
    """
    Calculates the MAXIMUM dimension diameter of particle images.

    If monoscale is true, the function ignores the first shadow-level.

    If the particle height and width is already known, the function can use these values,
    instead of computing them again.

    :param array:       optical array (particle image)
    :type array:        numpy array (1 dimensional) or list or string

    --- optional params ---
    :param x:           particle width (x-dimension)
    :type x:            integer

    :param y:           particle height/length (y-dimension)
    :type y:            integer

    :param monoscale:   if true method ignores first shadow level
    :type monoscale:    boolean

    :param slicesize:   width of the optical array (number of diodes)
    :type slicesize:    integer

    :return:            maximum dimension -> sqrt(y² + x²)
    """
    if x == None or y == None:
        x, y = xy_dimension(array, monoscale, slicesize)
    return sqrt(y*y + x*x)



def minimum_dimension(array, x=None, y=None, monoscale=False, slicesize=SLICE_SIZE):
    """
    Calculates the MINIMUM dimension diameter of particle images.

    If monoscale is true, the function ignores the first shadow-level.

    If the particle height and width is already known, the function can use these values,
    instead of computing them again.

    :param array:       optical array (particle image)
    :type array:        numpy array (1 dimensional) or list or string

    --- optional params ---
    :param x:           particle width (x-dimension)
    :type x:            integer

    :param y:           particle height/length (y-dimension)
    :type y:            integer

    :param monoscale:   if true method ignores first shadow level
    :type monoscale:    boolean

    :param slicesize:   width of the optical array (number of diodes)
    :type slicesize:    integer

    :return:            minimum dimension -> 2*sqrt((y*x) / pi)
    """
    if x == None or y == None:
        x, y = xy_dimension(array, monoscale, slicesize)
    return 2*sqrt((y*x) / pi)


# ToDo: Monoscale Area Size
def area_size(array, pixelno=None, monoscale=False, slicesize=SLICE_SIZE): # ----------------------------------------------------------- nicht perfekt array ist uninteressant - Stichwort funtkion überschreiben ?!?
    """
    Calculates the Area Size diameter of a particle image.

    If monoscale is true, the function ignores the first shadow-level.

    If the number of pixels is known, the function can use this value,
    instead of computing it again.

    :param array:       optical array (particle image)
    :type array:        numpy array (1 dimensional) or list or string

    --- optional params ---
    :param pixelno:     number of pixels
    :type pixelno:      integer

    :param monoscale:   if true method ignores first shadow level
    :type monoscale:    boolean

    :param slicesize:   width of the optical array (number of diodes)
    :type slicesize:    integer

    :return:            area size -> sqrt(4 * (pixel_no / pi))
    """
    pixel_no = pixelno
    if pixel_no ==  None:
        pixel_no = 0
        for y in range(int(len(array) / slicesize)):
            for x in range(slicesize):

                if monoscale:
                    if (array[y*slicesize+x] != 0 \
                    and array[y*slicesize+x] != 1 \
                    and array[y*slicesize+x] != '0' \
                    and array[y*slicesize+x] != '1'):
                        pixel_no += 1
                else:
                    if (array[y*slicesize+x] != 0 \
                    and array[y*slicesize+x] != '0'):
                        pixel_no += 1
    if pixel_no:
        return sqrt(4 * (pixel_no / pi))
    else:
        return 0.0







def _distance_between_two_points(a, b):
    """
    Computes the distance between two points.

    :param a:   point (x,y)
    :type a:    tuple or list (len == 2)

    :param b:   point (x,y)
    :type b:    tuple or list (len == 2)

    :return:    distance between the two points (float)
    """
    vecx = a[0]-b[0]
    vecy = a[1]-b[1]
    return sqrt(vecx*vecx+vecy*vecy)



def particle_radius(array, monoscale=False, slicesize=SLICE_SIZE):
    """
    Returns radius of particle. Biggest distance from barycenter to image pixels.

    :param array:       optical array (particle image)
    :type array:        numpy array (1 dimensional) or list or string

    --- optional params ---
    :param monoscale:   if true method ignores first shadow level
    :type monoscale:    boolean

    :param slicesize:   width of the optical array (number of diodes)
    :type slicesize:    integer

    :return:            particle radius (float)
    """
    center = barycenter(array, coordinates=False, slicesize=slicesize)
    distance = 0
    for y in range(int(len(array) / slicesize)):
        for x in range(slicesize):
            if monoscale:
                if array[y*slicesize+x] > 1 \
                and distance < _distance_between_two_points((x, y), center):
                    distance = _distance_between_two_points((x, y), center)
            else:
                if array[y*slicesize+x] != 0 \
                and distance < _distance_between_two_points((x, y), center):
                    distance = _distance_between_two_points((x, y), center)
    return distance



def maximum_distance(array, monoscale=False, slicesize=SLICE_SIZE): # ---------------------------------------------------- no monoscale
    """
    Returns maximum distance between particle image pixels.

    :param array:       optical array (particle image)
    :type array:        numpy array (1 dimensional) or list or string

    --- optional params ---
    :param monoscale:   if true method ignores first shadow level
    :type monoscale:    boolean

    :param slicesize:   width of the optical array (number of diodes)
    :type slicesize:    integer

    :return:            particle radius (float)
    """
    points = scatter_array(array, slicesize=slicesize)
    if len(points) == 1:
        return 1
    distance = 0
    for i, u in enumerate(points):
        for j, v in enumerate(points):
            if i <= j:
                continue
            if distance < _distance_between_two_points(u, v):
                distance = _distance_between_two_points(u, v)
    return distance



def korolev_correction(array, korolevtable=KOROLEV_TABLE, slicesize=SLICE_SIZE): # ---------------------------------------------------- Problem bei nicht geclippten Bildern, da particle_features das nicht abfängt
    """
    Implementation of the Korolev Correction Algorithm
    (Korolev 2007: Reconstruction of the Sizes of Spherical Particles from Their Shadow Images)

    Current table (Appendix B Korolev 2007) contains values for Poisson Spots measured with
    a monoscale probe. If you use a greyscale probe, make sure your ignore
    shadowlevel 1 (e.g. use convert_to_monoscale()) before using korolev_correction().

    If particle contains a Poisson Spot, function returns the corrected particle diameter.
    Else the measured particle diameter in x-direction (in Korolev 2007 referred as D edge)
    will be returned.

    :param array:           optical array (particle image)
    :type array:            numpy array (1 dimensional) or list or string

    --- optional params ---
    :param korolevtable:    path to the korolev table
    :type korolevtable:     string

    :param slicesize:       width of the optical array (number of diodes)
    :type slicesize:        integer

    :return:                corrected particle diameter (float)
    """

    new_array = convert_to_monoscale(array, slicesize=slicesize)

    # If there are just shadowlevel 1 pixels in the image, the array is empty after the monoscale conversion.
    if max(new_array) == 0:
        return 0
    poisson_spot(new_array, sizing=False, checkAlsoY=False, slicesize=slicesize)
    features = particle_features(new_array, slicesize)

    # If there is no Poisson Spot, return the measured particle x-diameter.
    if not features['poisson_dia']:
        return features['w']

    # First Step of the Korolev Algorithm: Calculate the measured ratio between the
    # measured Poisson Spot diameter and the measured particle diameter.
    spot_edge_ratio = float(features['poisson_dia']) / features['w']

    # Dimensionless distance Zd.
    # zd = 0.0
    edge_true_ratio = 0.0
    korolev_spot_edge_ratio = 0.0

    # Next Step: Look up the ratio between the measured diameter
    # and the true diameter in the table.
    for line in korolevtable:
        if line[2] < spot_edge_ratio:
            # zd = line[0]
            edge_true_ratio = line[1]
            korolev_spot_edge_ratio = line[2]
        # Check if the next value of the table is closer to the actual
        # measured ratio (D_spot / D_edge).
        elif abs(spot_edge_ratio - line[2]) \
           < abs(spot_edge_ratio - korolev_spot_edge_ratio):
            # zd = line[0]
            edge_true_ratio = line[1]
        else:
            break
    # Last step of the Korolev Algorithm: Calculate and return the corrected diameter.
    return features['w'] / edge_true_ratio
