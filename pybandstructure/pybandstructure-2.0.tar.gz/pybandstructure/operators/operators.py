#!/usr/bin/env python3
# -*- coding: utf-8 -*-
########## Import modules ##############################################

from warnings import warn

import numpy as np
from scipy.linalg import eigh
from scipy.linalg import eig
from numpy.linalg import multi_dot
from tqdm import tqdm
import copy
import h5py

from pybandstructure.common import *
from pybandstructure.sample.sample import Sample

####### Operator class #################################################


class Operator:
    """Class for generic operators represented in a basis
    $|v_{\bm k}^{(i)}\rangle$ by its matrix elements

    $\langle v_{\bm k}^{(i)}|O|v_{\bm k + \bm q}^{(j)}\rangle
    = O_{ij}(\bm k,\bm q)$.

    The matrix elements are specified as linear combinations of matrices
    with k and q dependent coefficients in the form

    $O_{ij}(\bm k, \bm q) = \sum_\ell M_{ij}^{(\ell)}
    f_\ell(\bm k, \bm q)$

    Attributes
    ----------
    matrices
    coefficients
    size
    hermitian
    n_terms
    momentum_conserving

    """

    ######## Initialization ############################################

    def __init__(self, matrices, coefficients, momentum_conserving, hermitian, collapse=True):
        """Initializes an instance of the class given matrices and
        coefficients

        Parameters
        ----------
        matrices : list
            list of the matrices $ M_{ij}^{(\ell)} $. Each element can
            be a 2D array or a list of 2D arrays. All the matrices must
            be square and with the same size
        coefficients : list
            list of coefficients $ f_\ell(\bm k, \bm q) $. Each element
            can be a callable (accepting two arguments) or a c number.
        collapse : bool, optional
            whether to collapse constant coefficients into a unique
            matrix, by default True
        hermitian : bool, optional
            whether the operator is hermitian, by default True

        Raises
        ------
        TypeError
            if input is not of the correct type
        """
        ### copy and store attrs
        self.matrices = copy.deepcopy(matrices)
        self.coefficients = copy.deepcopy(coefficients)
        self.momentum_conserving = momentum_conserving
        self.hermitian = hermitian
        self.n_terms = len(matrices)
        if self.n_terms == 0:
            self.size = 0
        else:
            if type(matrices[0]) == np.ndarray:
                self.size = matrices[0].shape[0]
            elif type(matrices[0]) == list:
                self.size = matrices[0][0].shape[0]
        ### checks
        assert type(self.matrices) == list
        assert type(self.coefficients) == list
        assert len(self.coefficients) == self.n_terms
        for i, M in enumerate(self.matrices):
            if type(M) == np.ndarray:
                assert M.shape == (self.size, self.size)
                assert callable(self.coefficients[i]) or isinstance(
                    self.coefficients[i], (int, float, complex)
                )
            elif type(M) == list:
                assert callable(self.coefficients[i]) or len(
                    self.coefficients[i]
                ) == len(M)
                for Mj in M:
                    assert Mj.shape == (self.size, self.size)
            else:
                raise TypeError("matrices must be 2D arrays or lists of ndarrays")
        ### collapse constant coeffs
        if collapse:
            self.collapse_constant_coefficients()

    ########## Methods #################################################

    def __call__(self, *args, **kwargs):
        """Evaluate the matrix element of the operator

        Parameters
        ----------
        args
            arguments to be passed to the coefficient functions

        Returns
        -------
        array of complex of shape [size, size]
        """
        matrix = np.zeros([self.size, self.size], dtype=complex)
        for i in range(self.n_terms):
            if type(self.matrices[i]) == np.ndarray:
                if callable(self.coefficients[i]):
                    coeff = self.coefficients[i](*args, **kwargs)
                else:
                    coeff = self.coefficients[i]
                if coeff != 0.:
                    matrix += coeff * self.matrices[i]
            elif type(self.matrices[i]) == list:
                if callable(self.coefficients[i]):
                    coeff = self.coefficients[i](*args, **kwargs)
                else:
                    coeff = self.coefficients[i]
                for j, mat in enumerate(self.matrices[i]):
                    if coeff[j] != 0.:
                         matrix += coeff[j] * mat
                #matrix += np.sum(
                #    [coeff[j] * mat for j, mat in enumerate(self.matrices[i])], axis=0
                #)
            else:
                raise TypeError("matrices must be 2D arrays or lists of ndarrays")
        return matrix


    def collapse_constant_coefficients(self):
        """
        Collapse all the constant coefficients in one matrix with unity
        coefficient
        """
        ### Find constant matrices and indices
        constant_matrix = np.zeros([self.size, self.size], dtype=complex)
        constant_coefficients = []
        for i, f in enumerate(self.coefficients):
            if not callable(f):
                constant_coefficients.append(i)
                if type(self.matrices[i]) == np.ndarray:
                    constant_matrix += f * self.matrices[i]
                elif type(self.matrices[i]) == list:
                    constant_matrix += np.sum(
                        [f[j] * mat for j, mat in enumerate(self.matrices[i])], axis=0
                    )
                else:
                    raise TypeError("matrices must be 2D arrays or lists of ndarrays")
        ### remove constant matrices and coefficients (note that lists
        # are traversed backwards)
        for index in constant_coefficients[::-1]:
            del self.coefficients[index]
            del self.matrices[index]
        ### append one single matrix with unity cofficient
        if not np.allclose(constant_matrix, 0.0):
            self.coefficients.append(1.0)
            self.matrices.append(constant_matrix)
        ### update n_terms
        self.n_terms = len(self.matrices)

    def flatten(self):
        """Transform list of matrices multiplied by vector coefficients
        in matrices multiplied by c numbers
        """
        for i, m in enumerate(self.matrices):
            if type(m) == list:
                if callable(self.coefficients[i]):
                    coefficient_list = split_function(self.coefficients[i], len(m))
                else:
                    coefficient_list = self.coefficients[i]
                del self.matrices[i]
                del self.coefficients[i]
                self.matrices[i:i] = m
                self.coefficients[i:i] = coefficient_list

    def diagonalize(self, *args, **kwargs):
        """Diagonalize the operator at a given value of k and q
        Parameters
        ----------
        args :
            arguments to be passed to the function coefficients
        kwargs :
            overlap : Operator or None, optional
                overlap matrix for generalized eigenvalue problems

                $O u = \lambda S u$

                It must accept the same arguments as O
                by default None, i.e. S = 1.

            eigvals : tuple, optional
                eigenvalues to be computed (see numpy.linalg.eigh),
                by default None, i.e. compute all the eigenvalues.
            other keyword arguments to be passed to the operator and overlap

        Returns
        -------
        eigenvalues, eigenvectors
            see description of the output of numpy.linalg.eigh
        """
        overlap = kwargs.pop("overlap", None)
        eigvals = kwargs.pop("eigvals", None)

        if self.hermitian:
            
            if overlap is None:
                ### Hermitian
                return eigh(self.__call__(*args,**kwargs), eigvals = eigvals)
            else:
                ### Hermitian generalized
                return eigh(self.__call__(*args,**kwargs), overlap(*args,**kwargs), eigvals = eigvals)
        else:
            print('diagonalizing non hermitian operator')
            if overlap is None:
                ### Generic
                return eig(self.__call__(*args,**kwargs), eigvals = eigvals)
            else:
                ### Generic generalized
                return eig(self.__call__(*args,**kwargs), overlap(*args,**kwargs), eigvals = eigvals)

    ######### Operations ###############################################

    def __add__(self, other):
        """sum two operators or an operator and a number"""
        if isinstance(other, Operator):
            return Operator(
                matrices=self.matrices + other.matrices,
                coefficients=self.coefficients + other.coefficients,
                momentum_conserving = self.momentum_conserving and other.momentum_conserving,
                hermitian = self.hermitian and other.hermitian,
                collapse = True
            )
        elif isinstance(other, (int, float, complex)):
            return Operator(
                matrices=self.matrices + [np.identity(self.size, dtype=complex)],
                coefficients=self.coefficients + [other],
                momentum_conserving = self.momentum_conserving,
                hermitian = self.hermitian and np.imag(other)==0.,
                collapse = True,
            )
        else:
            raise TypeError(
                "invalid operation + for Operator and {}".format(type(other))
            )

    def __radd__(self, other):
        """right addition"""
        return self.__add__(other)

    def __mul__(self, other):
        """multiplication by a scalar"""
        if isinstance(other, (int, float, complex)):
            matrices_result = []
            for m in self.matrices:
                if type(m) == np.ndarray:
                    matrices_result.append(other * m)
                elif type(m) == list:
                    matrices_result.append([other * mat for mat in m])
                else:
                    raise TypeError("matrices must be 2D arrays or lists of ndarrays")
                
            return Operator(matrices=matrices_result, 
            coefficients=self.coefficients,
            momentum_conserving=self.momentum_conserving,
            hermitian = self.hermitian and np.imag(other)==0.,
            collapse = True)
        else:
            raise TypeError(
                "invalid operation * for Operator and {}".format(type(other))
            )

    def __rmul__(self, other):
        """right multiplication"""
        return self.__mul__(other)

    def __sub__(self, other):
        """subtraction"""
        return self.__add__(-1 * other)

    def __neg__(self):
        """multiply by -1"""
        return self.__mul__(-1)

    def __pos__(self):
        """do nothinig """
        return self

    #### illegal and not implemented operations

    def __gt__(self, other):
        self._illegal(">")

    def __ge__(self, other):
        self._illegal(">=")

    def __lt__(self, other):
        self._illegal("<")

    def __le__(self, other):
        self._illegal("<=")

    def __pow__(self, other):
        self._not_implemented("**")

    def _illegal(self, operation):
        print('illegal operation "{:s}" for operators'.format(operation))

    def _not_implemented(self, operation):
        print('operation "{:s}" is not implemented for operators'.format(operation))


########################################################################

####### Momentum_Conserving_Operator class #############################


class Momentum_Conserving_Operator(Operator):
    """Class for operators that conserve momentum represented in a basis
    $|v_{\bm k}^{(i)}\rangle$ by its matrix elements

    $\langle v_{\bm k}^{(i)}|O|v_{\bm k}^{(j)}\rangle
    = O_{ij}(\bm k)$.

    The matrix elements are spcified as linear combinations of matrices
    with k and q dependent coefficients in the form

    $O_{ij}(\bm k, \bm q) = \sum_\ell M_{ij}^{(\ell)}
    f_\ell(\bm k)$

    Attributes
    ----------
    matrices
    coefficients
    size
    hermitian
    n_terms

    """

    ############### Initialization #####################################

    def __init__(self, matrices, coefficients, collapse=True, hermitian=True):
        """Initalize an instance from matrices and coefficient.
        Note that the default option is hermitian = True

        Parameters
        ----------
        matrices : list
            list of the matrices $ M_{ij}^{(\ell)} $. Each element can
            be a 2D array or a list of 2D arrays. All the matrices must
            be square and with the same size
        coefficients : list
            list of coefficients $ f_\ell(\bm k, \bm q) $. Each element
            can be a callable (accepting two arguments) or a c number.
        collapse : bool, optional
            whether to collapse constant coefficients into a unique
            matrix, by default True
        hermitian : bool, optional
            whether the operator is hermitian, by default False

        Raises
        ------
        TypeError
            if input is not of the correct type
        """
        Operator.__init__(
            self,
            matrices=matrices,
            coefficients=coefficients,
            momentum_conserving = True,
            collapse=collapse,
            hermitian=hermitian,
        )

########################################################################