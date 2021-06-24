#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Common functions used in the project"""

################# Import modules #######################################

import numpy as np
import numpy.linalg as lin

#################### Distribution functions ############################


def fermi_function(E, T):
    """
    Returns Fermi-Dirac function $f(E, T)=\frac{1}{1+\exp[E/T]}$
    correctly handling T=0
    """
    if T != 0.0:
        return 0.5 - 0.5 * np.tanh(0.5 * E / T)
    else:
        return 0.5 - 0.5 * np.sign(E)


def bose_function(E, T):
    if T != 0.0:
        return -0.5 + 1.0 / np.tanh(0.5 * E / T)
    else:
        return -0.5 + 0.5 * np.sign(E)


def maxwell_function(E, T):
    if T != 0.0:
        return np.exp(-E / T)
    else:
        return np.nan


def delta_function(x, eta, shape="fermi"):
    """returns different types of function converging to a Dirac delta
    function as the parameter eta goes to 0"""
    if shape == "fermi":
        return 1.0 / eta * 0.25 * (1.0 - (np.tanh(x / (2.0 * eta))) ** 2)
    if shape == "lorentz":
        return eta / (np.pi * (x ** 2 + eta ** 2))
    if shape == "gauss":
        return np.exp(-(x ** 2) / (2.0 * eta ** 2)) / (eta * np.sqrt(2.0 * np.pi))


##################### Arithmetic operations for tuples #################


def tsum(a, b):
    "sum two tuples a and b"
    return tuple([x + y for x, y in zip(a, b)])


def tdif(a, b):
    "difference of two tuples a and b"
    return tuple([x - y for x, y in zip(a, b)])


def tneg(a):
    "negative of a tuple"
    return tuple([-x for x in a])


def tmul(a, b):
    "element-wise multiplication for tuples"
    return tuple([x * y for x, y in zip(a, b)])


def tdiv(a, b):
    "element-wise division for tuples"
    return tuple([x / y for x, y in zip(a, b)])


def tint_div(a, b):
    "element-wise integer division for tuples"
    return tuple([x // y for x, y in zip(a, b)])


def tmod(a, b):
    "element-wise modulus for tuples"
    return tuple([x % y for x, y in zip(a, b)])


def tsmul(s, a):
    "multiplies a tuple a by a scalar s"
    return tuple([s * x for x in a])


#################### Functions manipulation ############################


def translate_function(f, v):
    "given a function f and v returns a function g such as g(x) = f(x+v)"
    return lambda x: f(x + v)


def sum_functions(f, g):
    return lambda *args, **kwargs: f(*args, **kwargs) + g(*args, **kwargs)


def multiply_functions(f, g):
    return lambda *args, **kwargs: f(*args, **kwargs) * g(*args, **kwargs)


def multiply_function_scalar(f, a):
    return lambda *args, **kwargs: f(*args, **kwargs) * a


def conjugate_function(f):
    return lambda *args, **kwargs: np.conj(f(*args, **kwargs))


def split_function(f, n):
    return [lambda *args, **kwargs: f(*args, **kwargs)[i] for i in range(n)]


################ Geometrical transformations ###########################


def rotation_matrix(theta, rad=False):
    # Rotation matrix, default input in degrees
    if not rad:
        theta = np.radians(theta)
    s, c = np.sin(theta), np.cos(theta)
    return np.array([[c, -s], [s, c]])


def reflection_matrix(theta, rad=False):
    # Rotation matrix, default input in degrees
    if not rad:
        theta = np.radians(theta)
    s, c = np.sin(2 * theta), np.cos(2 * theta)
    return np.array([[c, s], [s, -c]])


########### Pauli matrices #############################################


def pauli_matrix(index):
    """Returns Pauli matrices given index """
    if index == 0 or index == "I":
        return np.eye(2, dtype=complex)
    elif index == 1 or index == "x":
        return np.array([[0, 1], [1, 0]], dtype=complex)
    elif index == 2 or index == "y":
        return np.array([[0, -1.0j], [1.0j, 0]], dtype=complex)
    elif index == 3 or index == "z":
        return np.array([[1, 0], [0, -1]], dtype=complex)
    elif index == "+":
        return np.array([[0, 1], [0, 0]], dtype=complex)
    elif index == "-":
        return np.array([[0, 0], [1, 0]], dtype=complex)
    elif index == "u":
        return np.array([[1, 0], [0, 0]], dtype=complex)
    elif index == "l":
        return np.array([[0, 0], [0, 1]], dtype=complex)
    else:
        raise ValueError("index can be 0,1,2,3,I,x,y,z,+,-,u,l")


########################################################################
