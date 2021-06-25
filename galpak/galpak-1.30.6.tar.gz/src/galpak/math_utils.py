# -*- coding: utf-8 -*-

import numpy as np
import math

# Mandatory TAU = 6.283185307179586...
math.tau = 2 * math.pi


def merge_where_nan(target, filler):
    """
    Procedurally mutates target by replacing its nan values by values from filler.
    This is a very simple polyfill for numpy.copyto (for numpy < 1.7).
    """
    try:
        np.copyto(target, filler, where=np.isnan(target))
    except AttributeError:
        isnan = np.isnan(target)
        target[isnan] = filler[isnan]


def safe_exp(x):
    """
    Should not throw during Underflows (and return 0) and Overflows (and return inf).
    This code is a hack, and may be cause of future bugs.
    Oddly enough, it passes a few basic tests in `math_utils_test.py`.
    """
    try:
        a = math.exp(x)
    except OverflowError:
        return float("inf")
    # There's no UnderflowError. WTF?
    # except UnderflowError:
    #     return 0
    return a


def divide(numerator, denominator, value_when_invalid=0):
    """
    Divide ndarray numerator by ndarray denominator, return the resulting ndarray.
    They MUST be of the same shape.
    This mutates numerator, too, of course.

    /!\ SLOW => UNUSED (kept as an iterator snippet)
    Benchmarking note: Devectorization of numpy one-liners is 30x slower.
    """

    it = np.nditer(numerator, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        value = denominator[it.multi_index]
        if value != 0:
            it[0] /= value
        else:
            it[0] = value_when_invalid
        it.iternext()

    return numerator


def median_clip(data, clip_sigma=3., limit_ratio=1e-3, max_iterations=5):
    """
    Computes an iteratively sigma-clipped median on a data set.

    data : ndarray
        Input data.
    clip_sigma : float
        Sigma at which to clip.
    limit_ratio : float
        If the proportion of rejected pixels is less than this fraction, the iterations stop.
    max_iterations : int
        Ceiling on the number of clipping iterations.
    """

    # Make sure data is safe
    data = data[(np.isnan(data) == False) * np.isfinite(data)]

    median = np.median(data)
    iteration = 0
    finished = False
    while not finished:
        iteration += 1
        lastct = median
        median = np.median(data)
        sigma = np.std(data)

        # Reduce data set
        index = np.nonzero(np.abs(data - median) < clip_sigma * sigma)
        if np.size(index) > 0:
            data = data[index]

        if (abs(median - lastct) / abs(lastct) < limit_ratio) or (iteration >= max_iterations):
            finished = True

    median = np.median(data)
    sigma = np.std(data)

    return median, sigma, iteration

def flux_gaussian(radius, rhwhm):
        """
        Disk Gaussian profile with Gaussian thickness
        """
        energy = np.exp(-radius ** 2 / 2. / (2. * rhwhm / 2.35) ** 2) #* np.exp(-nz ** 2 / 2. / hz ** 2)
        return energy #DizkModel.flux_sersic(radius, size, 0.5)

def flux_sersic(radius, size, index):
        """
        Sersic profile with Gaussian thickness
        See http://en.wikipedia.org/wiki/Sersic_profile
        """
        beta = 1.9992 * index - 0.3271
        energy = np.exp(-beta * (radius / size) ** (1. / index))
        #energy = np.exp(-beta * (radius / size) ** (1. / index)) * np.exp(-nz ** 2 / 2. / hz ** 2)
        #energy = np.exp(-beta * (radius / size) ** (1. / index)) * np.exp(-np.sqrt(nz ** 2) / hz )  #exponential z-profile
        #energy = np.exp(-beta * (radius / size) ** (1. / index)) * np.cosh(-nz / hz )**(-2.)        #sech^2 z-profile
        return energy

def flux_exponential(radius, size):
        """
        Disk exponential profile with Gaussian thickness
        This is merely a Sérsic profile with index = 1
        """
        return flux_sersic(radius, size, 1.)

def flux_de_vaucouleurs(radius, size):
        """
        De Vaucouleurs profile with Gaussian thickness
        See http://en.wikipedia.org/wiki/De_Vaucouleurs%27_law
        This is merely a Sérsic profile with index = 4
        """
        return flux_sersic(radius, size, 4.)







