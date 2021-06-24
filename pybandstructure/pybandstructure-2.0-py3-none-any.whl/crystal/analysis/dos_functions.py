from pybandstructure.common import *
import numpy as np

def dos(epsilon, energies, k_weights ,integration_constant, eta, shape):
    """calculates the DOS using trapz_bz and E_matrix containing samples of
    the band energy"""
    delta = delta_function(np.expand_dims(epsilon, axis=(0,1)) - np.expand_dims(energies, axis =(2)), eta, shape=shape)
    return integration_constant * np.einsum('nke,k->e', delta, k_weights)

def jdos(epsilon, nu, mu, energies, k_weights ,integration_constant, eta, shape):
    """calculates the jDOS using trapz_bz and E_matrix containing samples of
    the band energy"""
    delta = delta_function(np.expand_dims(epsilon, axis=(0)) - np.expand_dims(energies[nu,:] - energies[mu,:], axis =(1)) , eta, shape=shape)
    return integration_constant * np.einsum('ke,k->e', delta, k_weights)