#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""module for creating basis matrices for superlattices"""
#################################### Import modules ############################
import numpy as np
from pybandstructure.common import *
from pybandstructure.operators.operators import Operator, Momentum_Conserving_Operator
from pybandstructure.sample import Sample

#################### Lo#########################################################
def build_matrix_from_block(H, index, index1, n_blocks):
    """builds a block matrix with the square block H in the position (index, index1)

    Parameters
    ----------
    H : matrix or 2D square ndarray
        block to be inserted
    index : int
        row index of the block
    index1 : int
        column index of the block
    n_blocks : int
        number of blocks in each dimension of the matrix

    Returns
    -------
    [n_blocks * H.shape[0],n_blocks * H.shape[0]] ndarray of complex
        matrix with the block H in the specified position, zeros in the remaining entries.
    """
    assert H.ndim == 2
    assert H.shape[0] == H.shape[1]
    block_size = H.shape[0]
    size = block_size * n_blocks
    matrix = np.zeros([size, size], dtype=complex)
    matrix[
        index * block_size : (index + 1) * block_size,
        index1 * block_size : (index1 + 1) * block_size,
    ] = H
    return matrix


################################################################################
def build_basis_matrix(H, reciprocal_lattice_vectors, **kwargs):
    """builds a term of the Hamiltonian matrix given a function
    that returns the blocks corresponding to reciprocal lattice vectors G and G1

    Parameters
    ----------
    H : callable,
        matrix-valued function returning the block corresponding to given lattice vectors
        signature must be
        H(G, G1, reciprocal_lattice_vectors, **kwargs)
        with G, G1 integer coordinates
    reciprocal_lattice_vectors : Sample object
        sample of the relevant reciprocal space vectors
    **kwargs
        additional keyword arguments to be passed to H
    Returns
    -------
    [dof * #reciprocal_lattice_vectors, dof * #reciprocal_lattice_vectors]
        complex ndarray
        matrix containing the blocks given by the function
    """
    matrix = []
    for G_int in reciprocal_lattice_vectors:
        row = []
        for G1_int in reciprocal_lattice_vectors:
            row.append(H(G_int, G1_int, reciprocal_lattice_vectors, **kwargs))
        matrix.append(row)
    return np.block(matrix)


################################################################################
def build_kinetic_term(H, f, reciprocal_lattice_vectors):
    """builds one term of the kinetic hamiltonian

    Parameters
    ----------
    H : 2d ndarray or list of 2d ndarrays
        Matrix or matrices of the kinetic operator associated to the coefficient f
    f : callable or constant
        coefficient
    reciprocal_lattice_vectors : Sample object
        sample of the reciprocal lattice

    Returns
    -------
    Momentum_Conserving_Operator object
        kinetic hamiltonian term
    """
    if type(H) == np.ndarray:
        block_size = H.shape[0]
    elif type(H) == list:
        block_size = H[0].shape[0]
    n_blocks = len(reciprocal_lattice_vectors)
    matrices = []
    functions = []
    for G_int in reciprocal_lattice_vectors:
        index = reciprocal_lattice_vectors[G_int]
        G = reciprocal_lattice_vectors.get_coords(G_int)
        if type(H) == np.ndarray:
            matrices.append(build_matrix_from_block(H, index, index, n_blocks))
        elif type(H) == list:
            matrices.append(
                [build_matrix_from_block(Hi, index, index, n_blocks) for Hi in H]
            )
        if callable(f):
            functions.append(translate_function(f, G))
        else:
            functions.append(f)
    return Momentum_Conserving_Operator(matrices=matrices, coefficients=functions)

################################################################################

def build_potential_term(U, transferred_wavevector, reciprocal_lattice_vectors):
    """
    Creates a matrix with the square block U where the difference of G and G1 
    is transferred_wavevector.
    Used with the identity matrix implements exp(i Q \hat{r}) or, equivalently,
    n_{-Q} with Q being the transferred wavevector.
    Parameters
    ----------
    U : square 2d ndarray
        block to be placed at the position G-G1 = transferred_wavevector
    transferred_wavevector : tuple of int
        integer coordinates of the difference of the two vectors
    reciprocal_lattice_vectors : Sample object
        sample of the reciprocal lattice

    Returns
    -------
    [len(reciprocal_lattice_vectors)*U.shape[0], len(reciprocal_lattice_vectors)*U.shape[0]] ndarray of complex
        the potential term
    """
    assert U.ndim == 2
    assert U.shape[0] == U.shape[1]
    block_size = U.shape[0]
    n_blocks = len(reciprocal_lattice_vectors)
    size = block_size * n_blocks
    matrix = np.zeros([size, size], dtype=complex)
    for G_int in reciprocal_lattice_vectors:
        for G1_int in reciprocal_lattice_vectors:
            if tdif(G_int, G1_int) == transferred_wavevector:
                index = reciprocal_lattice_vectors[G_int]
                index1 = reciprocal_lattice_vectors[G1_int]
                matrix[
                    index * block_size : (index + 1) * block_size,
                    index1 * block_size : (index1 + 1) * block_size,
                ] = U
    return matrix


################################################################################
def build_kinetic_hamiltonian(H0, reciprocal_lattice_vectors):
    """builds a folded kinetic hamiltonian given an hamiltonian and reciprocal
    superlattice vectors

    Parameters
    ----------
    H0 : MomentumConservingOperator object
        the unfolded hamiltonian
    reciprocal_lattice_vectors : Sample object
        reciprocal lattice sample

    Returns
    -------
    MomentumConservingOperator object
        the folded hamiltonian
    """
    terms = []
    for i in range(H0.n_terms):
        terms.append(
            build_kinetic_term(
                H0.matrices[i],
                H0.coefficients[i],
                reciprocal_lattice_vectors=reciprocal_lattice_vectors,
            )
        )
    hamiltonian = terms[0]
    for i in range(H0.n_terms - 1):
        hamiltonian = hamiltonian + terms[i + 1]
    return hamiltonian


################################################################################
def build_potential_hamiltonian(U, potential_components, reciprocal_lattice_vectors):
    """Creates a potential hamiltonian given a potential matrix, the potential
    components and reciprocal lattice vectors

    Parameters
    ----------
    U : 2d square ndarray
        the potential matrix block
    potential_components : list or array of length len(reciprocal_lattice_vectors)
            coefficients associated to the corresponding wavevector transfer
    reciprocal_lattice_vectors : Sample object
        reciprocal lattice sample

    Returns
    -------
    MomentumConservingOperator object
        the potential hamiltonian
    """
    assert len(potential_components) == len(reciprocal_lattice_vectors)
    matrices = []
    constants = []
    indices = []
    for G_int in reciprocal_lattice_vectors:
        index = reciprocal_lattice_vectors[G_int]
        if potential_components[index] != 0:
            constants.append(potential_components[index])
            matrices.append(build_potential_term(U, G_int, reciprocal_lattice_vectors))
            indices.append(index)
    return Momentum_Conserving_Operator(
        matrices=matrices, coefficients=constants, collapse=False
    )

########################################################################
class Selector():
    ''''''
    def __init__(self, sample, G):
        self.sample = sample
        self.n = len(sample)
        self.G = G
    def __call__(self,*args, **kwargs):
        G = tsum(self.G, kwargs['integer_part'])
        result = np.zeros([self.n])
        result[self.sample[tneg(G)]] = 1
        return result

def build_density_operator(matrix, G, reciprocal_lattice_vectors, difference_vectors = None):
    """builds operators of the type U n_G where U commutes with n_G

    Parameters
    ----------
    matrix : 2D array
        block corresponding to U, for density use the identity of the appropriate size
    G : tuple of ints
        coordinates of G
    reciprocal_lattice_vectors : Sample object
        reciprocal lattice sample
    difference_vectors : Sample object, optional
        differences of vectors in reciprocal lattice sample, 
        if None, all the differences are calculated by default None

    Returns
    -------
    Operator
    """    
    if difference_vectors is None:
        difference_vectors = set()
        for i in range(len(reciprocal_lattice_vectors)):
            for j in range(len(reciprocal_lattice_vectors)):
                difference_vectors.add ( 
                    tdif(
                        reciprocal_lattice_vectors.integer_coords[i], 
                        reciprocal_lattice_vectors.integer_coords[j]
                    ) 
                )
    
    diff_sample = Sample(basis_vectors = reciprocal_lattice_vectors.basis_vectors,
        denominator = reciprocal_lattice_vectors.denominator,
        integer_coords = list(difference_vectors))
    matrices = [[build_potential_term(matrix, 
                                      transferred_wavevector= g ,
                                      reciprocal_lattice_vectors=reciprocal_lattice_vectors) for g in diff_sample]]
    coefficients = [Selector(diff_sample, G)]
    return Operator(matrices = matrices, coefficients = coefficients, momentum_conserving = False, hermitian = False)