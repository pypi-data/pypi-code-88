import numpy as np
from pybandstructure.common import *


def local_conductivity_interband(
    omega, energy_diff, occupation_diff, momentum_matrix_alpha, momentum_matrix_beta, k_weights, integration_constant):
    with np.errstate(divide="ignore"):
        prefactor = -occupation_diff / energy_diff
    prefactor[np.logical_not(np.isfinite(prefactor))] = 0
    energy_denominator = 1. / (np.expand_dims(energy_diff,3) + np.expand_dims(omega, axis=(0,1,2)))
    return 1.j * np.pi * integration_constant * np.einsum(
        'nmk,nmkw,nmk,nmk,k->w',
        prefactor, 
        energy_denominator, 
        momentum_matrix_alpha, 
        np.conj(momentum_matrix_beta),
        k_weights)

def generalized_drude_weight(
    exponent,
    energies,
    chemical_potential,
    temperature,
    momentum_matrix_intra_alpha,
    momentum_matrix_intra_beta,
    k_weights, 
    integration_constant):

    f = delta_function(
        energies - chemical_potential, temperature, shape="fermi"
    ) * np.power(energies - chemical_potential, exponent)
    return np.pi * integration_constant * np.einsum(
        'nk,nk,nk,k->',
        f ,
        momentum_matrix_intra_alpha,
        momentum_matrix_intra_beta,
        k_weights)
