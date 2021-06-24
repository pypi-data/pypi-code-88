#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Two-dimensional Dirac fermions"""
__all__ = ["dirac"]
############################ Import modules ############################
import numpy as numpy

from pybandstructure.common import *
from pybandstructure.operators.operators import *

########################################################################
def dirac(hv, delta):
    sigma_x = pauli_matrix("x")
    sigma_y = pauli_matrix("y")
    sigma_z = pauli_matrix("z")
    hamiltonian = Momentum_Conserving_Operator(
        matrices=[[sigma_x, sigma_y], sigma_z],
        coefficients=[_f_dirac(hv=hv, der=(0, 0)), delta],
    )
    overlap = None
    p_x = Momentum_Conserving_Operator(
        matrices=[[sigma_x, sigma_y]], coefficients=[_f_dirac(hv=hv, der=(1, 0))]
    )
    p_y = Momentum_Conserving_Operator(
        matrices=[[sigma_x, sigma_y]], coefficients=[_f_dirac(hv=hv, der=(0, 1))]
    )
    momentum_operator = [p_x, p_y]
    return {
        "hamiltonian": hamiltonian,
        "overlap": overlap,
        "momentum_operator": momentum_operator,
    }


class _f_dirac:
    def __init__(self, hv, der=(0, 0)):
        self.hv = hv
        self.der = der

    def __call__(self, k):
        if self.der == (0, 0):
            return [self.hv * k[0], self.hv * k[1]]
        if self.der == (1, 0):
            return self.hv * np.array([1, 0])
        if self.der == (0, 1):
            return self.hv * np.array([0, 1])
        else:
            return np.array([0, 0])
