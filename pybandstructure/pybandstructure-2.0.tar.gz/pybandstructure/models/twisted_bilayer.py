#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Twisted bilayer graphene"""
__all__ = ["koshino"]
############################ Import modules ############################
import numpy as numpy
from numpy.linalg import norm

from pybandstructure.common import *
from pybandstructure.operators.operators import *
from pybandstructure.operators.superlattices import *
from pybandstructure.sample import Sample

################## Matrices for interlayer tunneling ###################
def interlayer_tunneling_matrices(alignment, valley):
    """Provides interlayer tunneling matrices

    Parameters
    ----------
    alignment : string
        'AA' or 'AB'
    valley : int
        +- 1

    Returns
    -------
    list of matrices

    Raises
    ------
    ValueError
        if incorret inputs
    """   
    if not (valley ==1 or valley ==-1):
         raise ValueError('valley must be +/-1')
    const = np.exp(1j * valley * 2 * np.pi / 3)
    ### AA tunneling
    if alignment == 'AA':
        return [np.eye(2, dtype = complex), 
                1.0/const * np.eye(2, dtype = complex),
                const * np.eye(2, dtype = complex)]
    ### AB tunneling
    elif alignment == 'AB':
        return [np.array([[0,1],[1,0]], dtype=complex), 
               np.array([[0,1],[const,0]], dtype=complex),
               np.array([[0,1],[1./const,0]], dtype = complex)]
    else:
        raise ValueError('alignment must be AA or AB')

def dirac_hamiltonian_block(valley):
    """return Dirac Hamiltonian block

    Parameters
    ----------
    valley : int
        +-1

    Returns
    -------
    list of matrices
        Dirac matrices

    Raises
    ------
    ValueError
        if valley not +-1
    """    
    if not (valley ==1 or valley ==-1):
        raise ValueError('valley must be +/-1')

    return [
        np.kron(pauli_matrix("u"), valley * pauli_matrix("x")),
        np.kron(pauli_matrix("u"), -pauli_matrix("y")),
        np.kron(pauli_matrix("l"), valley * pauli_matrix("x")),
        np.kron(pauli_matrix("l"), -pauli_matrix("y")),
    ]

def graphene_rec_vecs(theta, a, layer,valley):
    if layer == 1:
        return [np.array([0,0]),
                valley * 4. *np.pi/(a * np.sqrt(3.)) * np.array([np.cos((150 + theta/2)*np.pi/180), np.sin((150 + theta/2)*np.pi/180)]),
                valley * 4. *np.pi/(a * np.sqrt(3.)) * np.array([np.cos((-150 + theta/2)*np.pi/180), np.sin((-150 + theta/2)*np.pi/180)])]
    elif layer == 2:
        raise NotImplementedError
    else:
        raise ValueError('layer must be 1 or 2')

def gamma_point_tblg(theta, a, valley):
    return valley * 4. *np.pi/(a * 3.) * (np.cos(theta / 360.0 * np.pi) + np.sqrt(3) * np.sin(theta / 360.0 * np.pi)) * np.array([1,0])


########## Functions for k-dependent terms #############################

class _kinetic_function:
    def __init__(self, theta, valley, g_moire, hv, der=(0, 0)):
        self.theta = theta #angle [deg]
        self.g_moire = g_moire # lenght of the smallest reciprocal vector
        self.hv = hv # hbar *v_D 
        self.der = der # derivative order
        s = np.sin(self.theta / 360.0 * np.pi)
        c = np.cos(self.theta / 360.0 * np.pi)
        self.R1 = np.array([[c, s], [-s, c]])
        self.R2 = np.array([[c, -s], [s, c]])
        self.K1 = valley * self.g_moire / np.sqrt(3) * np.array([-np.sqrt(3) / 2, 0.5])
        self.K2 = valley * self.g_moire / np.sqrt(3) * np.array([-np.sqrt(3) / 2, -0.5])

    def __call__(self, k):
        if self.der == (0, 0):
            return self.hv * np.concatenate(
                (np.dot(self.R1, k - self.K1), np.dot(self.R2, k - self.K2))
            )
        elif self.der == (1, 0):
            return self.hv * np.concatenate(
                (
                    np.dot(self.R1, np.array([1.0, 0.0])),
                    np.dot(self.R2, np.array([1.0, 0.0])),
                )
            )
        elif self.der == (0, 1):
            return self.hv * np.concatenate(
                (
                    np.dot(self.R1, np.array([0.0, 1.0])),
                    np.dot(self.R2, np.array([0.0, 1.0])),
                )
            )
        else:
            return 0.0

class _f_non_local():
    def __init__(self, theta, a, shift, der = (0,0)):
        self.g_moire = 8. * np.pi * np.sin(theta / 360.0 * np.pi) / (np.sqrt(3) * a)
        self.KD = 4. *np.pi/(a * 3.)
        self.shift =  shift
        self.der = der
    def __call__(self, k):
        if self.der == (0,0):
            return (norm(k+self.shift) -self.KD)/self.g_moire
        elif self.der == (1,0):
            return (k[0] + self.shift[0])/(self.g_moire * norm(k+self.shift))
        elif self.der == (0,1):
            return (k[1] + self.shift[1])/(self.g_moire * norm(k+self.shift))
        else:
            raise NotImplementedError

## Functions that generate terms of the hamiltonian and momentum #######
### intralayer
def koshino_intralayer(valley, theta, hv, reciprocal_lattice_vectors):
    """Intralayer part of Koshino hamiltonian"""
    g_moire = norm(reciprocal_lattice_vectors.basis_vectors[:, 0])

    H0 = Momentum_Conserving_Operator(
        matrices=[dirac_hamiltonian_block(valley =valley)],
        coefficients=[_kinetic_function(valley = valley, theta=theta, g_moire=g_moire, hv=hv)],
        collapse=True,
    )
    H0_lattice = build_kinetic_hamiltonian(
        H0, reciprocal_lattice_vectors=reciprocal_lattice_vectors
    )
    return H0_lattice

### momentum operator for Koshino model
def koshino_momentum(valley, theta, hv, reciprocal_lattice_vectors):
    """Momentum operators corresponding to Koshino hamiltonian"""
    g_moire = norm(reciprocal_lattice_vectors.basis_vectors[:, 0])
    p_x = build_kinetic_term(
        dirac_hamiltonian_block(valley = valley),
        _kinetic_function(valley=valley,theta=theta, g_moire=g_moire, hv=hv, der=(1, 0)),
        reciprocal_lattice_vectors=reciprocal_lattice_vectors,
    )
    p_x.collapse_constant_coefficients()
    p_y = build_kinetic_term(
        dirac_hamiltonian_block(valley = valley),
        _kinetic_function(valley=valley,theta=theta, g_moire=g_moire, hv=hv, der=(0, 1)),
        reciprocal_lattice_vectors=reciprocal_lattice_vectors,
    )
    p_y.collapse_constant_coefficients()
    return [p_x, p_y]

### interlayer hamiltonian
def koshino_interlayer(alignment, valley, reciprocal_lattice_vectors):
    """Interlayer part of Koshino hamiltonian"""
    T = interlayer_tunneling_matrices(alignment = alignment, valley = valley)
    transferred_wavectors = [(0,0), (valley * 1,0), (0,valley * 1)]
    matrices = []
    for j in range(3):
        matrices.append(
            build_potential_term(
                U = np.kron(pauli_matrix("+"), T[j]),
                transferred_wavevector= transferred_wavectors[j], 
                reciprocal_lattice_vectors = reciprocal_lattice_vectors)
            + build_potential_term(
                U = np.kron(pauli_matrix("-"), np.conj(T[j].T)),
                transferred_wavevector= tneg(transferred_wavectors[j]), 
                reciprocal_lattice_vectors = reciprocal_lattice_vectors))
    return Momentum_Conserving_Operator(
        matrices = matrices, 
        coefficients = [1. for _ in range(3)], 
        collapse=True, 
        hermitian=True)

### non-local hamiltonian correction
def nonlocal_interlayer(theta, a, alignment, valley , reciprocal_lattice_vectors):
    """Non-local correction to interlayer hamiltonian """
    T = interlayer_tunneling_matrices(alignment = alignment, valley = valley)
    transferred_wavectors = [(0,0), (valley * 1,0), (0,valley * 1)]
    graphene_reciprocal_vectors = graphene_rec_vecs(theta = theta, a=a, layer = 1, valley = valley)
    gamma_point = gamma_point_tblg(theta = theta, a  =a, valley = valley)
    matrices = []
    coefficients = []
    for j in range(3):
        for G in reciprocal_lattice_vectors:
            G1 = tdif(G, transferred_wavectors[j])
            if G1 in reciprocal_lattice_vectors:
                matrices.append(
                    build_matrix_from_block(
                        H=np.kron(pauli_matrix("+"),T[j]), 
                        index = reciprocal_lattice_vectors[G], 
                        index1 = reciprocal_lattice_vectors[G1], 
                        n_blocks = len(reciprocal_lattice_vectors))
                    + build_matrix_from_block(
                        H=np.kron(pauli_matrix("-"),np.conj(T[j].T)), 
                        index = reciprocal_lattice_vectors[G1], 
                        index1 = reciprocal_lattice_vectors[G], 
                        n_blocks = len(reciprocal_lattice_vectors))
                )
                coefficients.append(
                _f_non_local(theta = theta, a = a, shift = gamma_point + graphene_reciprocal_vectors[j] + reciprocal_lattice_vectors.get_coords(G))
                )

    return Momentum_Conserving_Operator(
        matrices = matrices, 
        coefficients = coefficients, 
        collapse=True, 
        hermitian=True)

def nonlocal_momentum(theta, a, alignment,valley, reciprocal_lattice_vectors):
    """Non-local correction to momentum operator"""
    T = interlayer_tunneling_matrices(alignment = alignment, valley = valley)
    transferred_wavectors = [(0,0), (valley * 1,0), (0,valley * 1)]
    graphene_reciprocal_vectors = graphene_rec_vecs(theta = theta, a=a, layer = 1, valley = valley)
    gamma_point = gamma_point_tblg(theta = theta, a  =a, valley = valley)
    momentum_components = []
    for direction in ((1,0),(0,1)):
        matrices = []
        coefficients = []
        for j in range(3):
            for G in reciprocal_lattice_vectors:
                G1 = tdif(G, transferred_wavectors[j])
                if G1 in reciprocal_lattice_vectors:
                    matrices.append(
                        build_matrix_from_block(
                            H=np.kron(pauli_matrix("+"),T[j]), 
                            index = reciprocal_lattice_vectors[G], 
                            index1 = reciprocal_lattice_vectors[G1], 
                            n_blocks = len(reciprocal_lattice_vectors))
                        + build_matrix_from_block(
                            H=np.kron(pauli_matrix("-"),np.conj(T[j].T)), 
                            index = reciprocal_lattice_vectors[G1], 
                            index1 = reciprocal_lattice_vectors[G], 
                            n_blocks = len(reciprocal_lattice_vectors))
                    )
                    coefficients.append(
                    _f_non_local(
                        theta = theta, 
                        a = a, 
                        shift = gamma_point + graphene_reciprocal_vectors[j] + reciprocal_lattice_vectors.get_coords(G), 
                        der = direction)
                    )

        momentum_components.append(Momentum_Conserving_Operator(
            matrices = matrices, 
            coefficients = coefficients, 
            collapse=True, 
            hermitian=True)
        )
    return momentum_components
################## Assemble models #####################################
### Koshino with non_local tunneling
def koshino(valley, theta, uAA, uAB, uAA_nl, uAB_nl, hv, a, G_max):
    """Total hamiltonian of the Koshino model

    Parameters
    ----------
    theta : float
        twist angle in degrees
    uAA : float
        interlayer tunneling (AA)
    uAB : float
        interlayer tunneling (AB)
    uAA_nl : float
        interlayer non-local tunneling (AA)
    uAB_nl : float
        interlayer non-local tunneling (AB)
    hv : float
        hbar  * Dirac_velocity
    a : float
        lattice constant of the original layer (0.246 nm in graphene)
    G_max : float
        cutoff in reciprocal lattice space in units of the reciprocal lattice constant

    Returns
    -------
    dict
        model
    """
    ### lenght of the smallest (non-zero) moiré reciprocal vector
    g_moire = 8.0 * np.pi * np.sin(theta / 360.0 * np.pi) / (np.sqrt(3) * a)
    ### basis of moiré reciprocal lattice
    reciprocal_lattice_basis = g_moire * np.array(
        [[0.5, -0.5], 
        [np.sqrt(3) / 2.0, np.sqrt(3) / 2.0]], 
        dtype=float
    )
    ### sample of the moiré reciprocal lattice
    reciprocal_lattice_vectors = Sample.lattice_sample(
        basis_vectors=reciprocal_lattice_basis, 
        cut_off= g_moire * G_max
    )
    ### build hamiltonian
    H = (
        koshino_intralayer(
            valley = valley,
            theta = theta, 
            hv = hv, 
            reciprocal_lattice_vectors= reciprocal_lattice_vectors
            )
        + uAA * koshino_interlayer(
            valley = valley,
            alignment = 'AA', 
            reciprocal_lattice_vectors=reciprocal_lattice_vectors
            )
        + uAB * koshino_interlayer(
            valley = valley,
            alignment = 'AB',
            reciprocal_lattice_vectors = reciprocal_lattice_vectors
            ) 
        + uAA_nl * nonlocal_interlayer(
            valley = valley,
            theta = theta, 
            a = a, 
            alignment = 'AA', 
            reciprocal_lattice_vectors= reciprocal_lattice_vectors
            )
        + uAB_nl * nonlocal_interlayer(
            valley = valley,
            theta = theta, 
            a = a, 
            alignment = 'AB', 
            reciprocal_lattice_vectors= reciprocal_lattice_vectors
            )
    )
    H.collapse_constant_coefficients()
    ### build momentum operator
    momentum_local = koshino_momentum(
            valley = valley,
            theta = theta, 
            hv = hv, 
            reciprocal_lattice_vectors = reciprocal_lattice_vectors
            )
    momentum_non_local_AA = nonlocal_momentum(
        valley = valley,
        theta = theta, 
        a = a, 
        alignment = 'AA', 
        reciprocal_lattice_vectors = reciprocal_lattice_vectors)
    
    momentum_non_local_AB = nonlocal_momentum(
        valley = valley,
        theta = theta, 
        a = a, 
        alignment = 'AB', 
        reciprocal_lattice_vectors = reciprocal_lattice_vectors)
    momentum_operator = [momentum_local[i] 
    + uAA_nl * momentum_non_local_AA[i]
    + uAB_nl * momentum_non_local_AB[i] for i in range(2)]
    return {
        "hamiltonian": H,
        "overlap": None,
        "momentum_operator": momentum_operator,
        "reciprocal_lattice_vectors": reciprocal_lattice_vectors,
    }
