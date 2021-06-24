#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""class for calculating and storing band structures"""
############################ Import modules ############################

import os
from warnings import warn
import numpy as np
from scipy.linalg import eigh
from numpy.linalg import multi_dot
from scipy.optimize import root_scalar
from scipy.optimize import root
from scipy.optimize import minimize
from tqdm import tqdm
import h5py
import matplotlib.pyplot as plt

from pybandstructure.common import *
from pybandstructure.sample.sample import Unit_Cell_Sample, Space_Sample
from pybandstructure.operators.operators import *

################ Band_Structure class ##################################


class Band_Structure:
    """class for calculating and storing band structures and operators
    matrix elements between Bloch eigenstates"""

    ######## Initialization and constructors ###########################

    def __init__(
        self,
        k_sample,
        q_sample=None,
        G_sample=None,
        energies=None,
        wavefunctions=None,
        hamiltonian=None,
        overlap=None,
        momentum_operator=None,
        momentum_matrix=None,
        density_operator=None,
        density_matrix=None,
        degeneracy=2,
        zero_filling=0.0,
        density=0.0,
        temperature=0.0,
        statistics = 'F',
        k_plus_q_ind = None,
    ):
        """Initialize a class instance.
        The user is not supposed to instanciate the classs directly but
        to use one of the constructors below.

        Parameters
        ----------
        k_sample : Space_Sample
            sampling of points of reciprocal space where the band structure
            is calculated
        energies : [n_bands, len(k_sample)] array of floats, optional
            band energies $ E_nu(k^(i)) $ is stored in energies[nu,i],
            by default None
        wavefunctions : [size,n_bands, len(k_sample)] array of complex,
        optional
            expansion coefficients of the Bloch wavefunctions
            $|k^(i),\nu> = c^(j)_nu(k^(i)) |v_j(k^(i))>$
            c^(j)_nu(k^(i)) is stored in wavefunctions[j,nu,i],
            by default None
        hamiltonian : Operator, optional
            hamiltonian operator, by default None
        overlap : Operator, optional
            overlap matrix for non orthogonal basis, by default None
        momentum_operator : list of Operator, optional
            cartesian components of the momentum operator,
            by default None
        momentum_matrix :
        [space_dimension,n_bands,n_bands, len(k_sample)] array of complex,
        optional
            momentum matrix elements between bands,
            $<k^(j),nu|\hbar p_i/m|k^(j), mu>$ is stored in
            momentum_matrix[i,nu,mu,j]
            by default None
        q_sample : Space_Sample, optional
            sampling of points of reciprocal space of the momentum exchanged between
            wavefunctions in evaluating the matrix elements of a non-conserving operator.
        G_sample : Space, lattice_sample, optional
            sampling of points of reciprocal lattice
        density_operator : list of Operator, optional
            list of density operators ordered with  G_sample index:
                density_operator = [len(G_sample)] #list, type(density_operator[0]) = Operator
            by default None
        density_matrix :
        [n_bands,n_bands, len(k_sample), len(q_sample), len(G_sample)] array of complex,
        optional
            density matrix elements between bands,
            $<k,nu|n(q+G)|k+q, mu>$
            by default None
        degeneracy : int, optional
            band degeneracy, by default 2
        zero_filling : float, optional
            number of bands filled at zero density, density = 0
            corresponds to degeneracy * zero_filling / unit_cell_volume
            by default 0.
        density : float, optional
            electronic density, by default 0.
        temperature : float, optional
            temperature in energy units, by default 0.
        statistics : str, optional
            'F' for Fermi-Dirac, 'B' for Bose-Einstein, 'M' for Maxwell-Boltzmann,
            by default 'F'.
        k_plus_q_ind : [n_q_points,n_k_points], array of int, optional by default None
            table of indices in k_sample indicating the corresponding k+q vector ubication
        """
        ### check and load
        ### k_sample
        assert isinstance(k_sample, (Space_Sample, Unit_Cell_Sample))
        self._k_sample = k_sample
        ### energies and wavefunctions
        # add checks on dimensions
        self._energies = energies
        self._wavefunctions = wavefunctions
        ### hamiltonian and overlap
        assert hamiltonian is None or (isinstance(hamiltonian, Operator ) and  hamiltonian.momentum_conserving)
        self._hamiltonian = hamiltonian
        assert overlap is None or (isinstance(overlap, Operator) and overlap.momentum_conserving)
        self._overlap = overlap
        ### momentum operator
        assert (
            type(momentum_operator) == list
            and all(
                [
                    (isinstance(pi, Operator) and pi.momentum_conserving)
                    for pi in momentum_operator
                ]
            )
        ) or momentum_operator is None
        self._momentum_operator = momentum_operator
        ### momentum matrix
        # add checks on dimensions
        self._momentum_matrix = momentum_matrix
        #check q_sample
        if not q_sample is None:
            try:
                assert isinstance(q_sample, Sample)
            except TypeError:
                print('q_sample must be of the type Sample.')
            try:
                assert np.allclose(q_sample.basis_vectors, self._k_sample.basis_vectors)
            except ValueError:
                print('The attribute basis_vectors of q_sample must be the same between q_sample and k_sample.')
            try:
                assert np.allclose(q_sample.denominator, self._k_sample.denominator)
            except ValueError:
                print('The attribute denominator of q_sample must be the same between q_sample and k_sample.')

        self._q_sample = q_sample
        #check G_sample
        if not G_sample is None:
            G_denominator = np.ones(len(G_sample.denominator), dtype=int)
            try:
                assert isinstance(G_sample, Sample)
            except TypeError:
                print('G_sample must be of the type Sample.')
            try:
                assert np.allclose(G_sample.basis_vectors, self._k_sample.basis_vectors)
            except ValueError:
                print('The attribute basis_vectors of G_sample must be the same between G_sample and k_sample.')
            try:
                assert np.allclose(G_sample.denominator, G_denominator)
            except:
                warn('G must have unitary denominator.')
        self._G_sample = G_sample
        ### density operator
        if not (q_sample is None or G_sample is None or density_operator is None):
            try:
                assert (
                               type(density_operator) == list
                                and len(density_operator) == len(G_sample)
                               and all(
                           [
                               isinstance(ni, Operator)
                               for ni in density_operator
                           ]
                       )
                       ) or density_operator is None
            except TypeError:
                print('density_operator must be a list; ni in density_operator must be of the type Operator')
        else:
            pass
        self._density_operator = density_operator
        ### density matrix
        #Check on dimensions
        #shape expected [n_bands, n_bands, len(k_sample), len(q_sample), len(G_sample)]
        if not (q_sample is None or G_sample is None or density_matrix is None):
            n_bands = len(self._energies)
            try:
                assert (
                        len(density_matrix[0, 0, 0, 0, :]) == len(G_sample) and len(density_matrix[0, 0, 0, :, 0])==len(q_sample) and
                        len(density_matrix[0, 0, :, 0, 0]) == len(k_sample)
                        and len(density_matrix[0, :, 0, 0, 0]) == len(density_matrix[:, 0, 0, 0, 0]) == n_bands
                        )
            except ValueError:
                print('Check of density_matrix dimensions failed, must be [n_bands, n_bands, len(k_sample), len(q_sample), len(G_sample)]')
        else:
            pass
        self._density_matrix = density_matrix
        ### other attributes
        self._degeneracy = degeneracy
        self._zero_filling = zero_filling
        self._density = density
        self._temperature = temperature
        ### distribution function
        if statistics == 'F':
            self._distribution_function = fermi_function
        elif statistics == 'B':
            self._distribution_function = bose_function
        elif statistics == 'M':
            self._distribution_function = maxwell_function
        else:
            raise ValueError('stastistics must be F,B or M')
        self._statistics = statistics
        ### table k_plus_q_ind
        self._k_plus_q_ind = k_plus_q_ind
        ### calculate chemical potential if possible
        if self._energies is None:
            self._chemical_potential = None
        else:
            self._chemical_potential = self.compute_chemical_potential()
        ### compute occupations if possible
        if self._energies is None:
            self._occupations = None
        else:
            self._occupations = self.compute_occupations()


    @classmethod
    def from_hamiltonian(
        cls,
        k_sample,
        hamiltonian,
        q_sample=None,
        G_sample=None,
        overlap=None,
        momentum_operator=None,
        density_operator=None,
        degeneracy=2,
        zero_filling=0,
        density=0,
        temperature=0,
        statistics = 'F',
        k_plus_q_ind = None,
    ):
        """Create a Band_Structure object given operators.
        This is the recommended constructor for problems that need to be
        diagonalized.

        Parameters
        ----------
        k_sample : Space_Sample
            sampling of points of reciprocal space where the band structure
            is calculated
        hamiltonian : Operator, optional
            hamiltonian operator, by default None
        overlap : Operator, optional
            overlap matrix for non orthogonal basis, by default None
        momentum_operator : list of Operator, optional
            cartesian components of the momentum operator,
            by default None
        q_sample : Space_Sample, optional
            sampling of points of reciprocal space of the momentum exchanged between
            wavefunctions in evaluating the matrix elements of a non-conserving operator.
        G_sample : Space_sample, lattice_sample, optional
            sampling of points of reciprocal lattice
        density_operator : list of Operator, optional
            list of density operators ordered with  G_sample index i:
                density_operator = [Operator, j] #list
            by default None
        degeneracy : int, optional
            band degeneracy, by default 2
        zero_filling : float, optional
            number of bands filled at zero density, density = 0
            corresponds to degeneracy * zero_filling / unit_cell_volume
            by default 0.
        density : float, optional
            electronic density, by default 0.
        temperature : float, optional
            temperature in energy units, by default 0.
        statistics : str, optional
            'F' for Fermi-Dirac, 'B' for Bose-Einstein, 'M' for Maxwell-Boltzmann,
            by default 'F'.
        Returns
        -------
        Band_Structure
            object created from operators
        """
        return cls(
            k_sample=k_sample,
            q_sample=q_sample,
            G_sample=G_sample,
            hamiltonian=hamiltonian,
            overlap=overlap,
            momentum_operator=momentum_operator,
            density_operator=density_operator,
            degeneracy=degeneracy,
            zero_filling=zero_filling,
            density=density,
            temperature=temperature,
            statistics = statistics,
            k_plus_q_ind = k_plus_q_ind,
        )

    @classmethod
    def from_file(cls, file_name, band_structure_name, file_format="hdf5"):
        """Initialize an instance using data from a file.
        This is the recommended constructor to reload data from a previous
        simulation.

        Parameters
        ----------
        file_name : str
            name of the file from which data are read
        band_structure_name : str
            name of the group inside the file where data are stored
        file_format : str, optional
            format of the input file, only "hdf5" available in this version,
            by default "hdf5"

        Returns
        -------
        Band_Structure
            object recreated from stored data
        """
        if file_format == "hdf5":
            with h5py.File(file_name, "r") as file_to_read:
                ### load energies, wavefunctions, k_sample
                energies = file_to_read[band_structure_name + "/energies"][...]
                wavefunctions = file_to_read[band_structure_name + "/wavefunctions"][
                    ...
                ]
                k_sample = Sample.from_file(
                    file_format = 'hdf5',
                    file_name=file_name, 
                    sample_name=band_structure_name + "/k_sample")
                ### Load q and G sample if present                
                if "q_sample" in file_to_read[band_structure_name]:
                    q_sample = Sample.from_file(
                    file_format = 'hdf5',
                    file_name=file_name, 
                    sample_name=band_structure_name + "/q_sample")
                else:
                    q_sample = None

                if "G_sample" in file_to_read[band_structure_name]:
                    G_sample = Sample.from_file(
                    file_format = 'hdf5',
                    file_name=file_name, 
                    sample_name=band_structure_name + "/G_sample")
                else:
                    G_sample = None
                ### Load momentum and density matrix
                if "momentum_matrix" in file_to_read[band_structure_name]:
                    momentum_matrix = file_to_read[
                        band_structure_name + "/momentum_matrix"
                    ][...]
                else:
                    momentum_matrix = None

                if "density_matrix" in file_to_read[band_structure_name]:
                    density_matrix = file_to_read[
                        band_structure_name + "/density_matrix"
                    ][...]
                else:
                    density_matrix = None
                ### Load k+q lookup table if present
                if "k_plus_q_ind" in file_to_read[band_structure_name]:
                    k_plus_q_ind = file_to_read[
                        band_structure_name + "/k_plus_q_ind"
                    ][...]
                else:
                    k_plus_q_ind = None
                ### Load attributes
                degeneracy = file_to_read[band_structure_name].attrs["degeneracy"]
                zero_filling = file_to_read[band_structure_name].attrs["zero_filling"]
                density = file_to_read[band_structure_name].attrs["density"]
                temperature = file_to_read[band_structure_name].attrs["temperature"]

        else:
            warn("unrecognized file type")

        return cls(
            k_sample=k_sample,
            q_sample=q_sample,
            G_sample=G_sample,
            energies=energies,
            wavefunctions=wavefunctions,
            momentum_matrix=momentum_matrix,
            density_matrix=density_matrix,
            degeneracy=degeneracy,
            zero_filling=zero_filling,
            density=density,
            temperature=temperature,
            k_plus_q_ind = k_plus_q_ind,
        )

    @classmethod
    def from_data(
        cls,
        k_sample,
        energies,
        q_sample,
        G_sample,
        wavefunctions,
        degeneracy=2,
        zero_filling=0,
        density=0,
        temperature=0,
        momentum_matrix=None,
        density_matrix=None,
        statistics = 'F',
        k_plus_q_ind = None,
    ):
        """Initialize an instance of the class given the arrays of energies
        and wavefunctions (and optionally momentum matrix elements).
        Intended to be used to load data from other softwares.

        Parameters
        ----------
         k_sample : Space_Sample
            sampling of points of reciprocal space where the band structure
            is calculated
        energies : [n_bands, len(k_sample)] array of floats, optional
            band energies $ E_nu(k^(i)) $ is stored in energies[nu,i],
            by default None
        wavefunctions : [size,n_bands, len(k_sample)] array of complex,
        optional
            expansion coefficients of the Bloch wavefunctions
            $|k^(i),\nu> = c^(j)_nu(k^(i)) |v_j(k^(i))>$
            c^(j)_nu(k^(i)) is stored in wavefunctions[j,nu,i],
            by default None
        q_sample : Space_Sample, optional
            sampling of points of reciprocal space of the momentum exchanged between
            wavefunctions in evaluating the matrix elements of a non-conserving operator.
        G_sample : Space_sample, lattice_sample, optional
            sampling of points of reciprocal lattice
        momentum_matrix :
        [space_dimension,n_bands,n_bands, len(k_sample)] array of complex,
        optional
            momentum matrix elements between bands,
            $<k^(j),nu|\hbar p_i/m|k^(j), mu>$ is stored in
            momentum_matrix[i,nu,mu,j]
            by default None
        density_matrix :
        [n_bands,n_bands, len(k_sample), len(q_sample), len(G_sample)] array of complex,
        optional
            density matrix elements between bands,
            $<k,nu|n(q+G)|k+q, mu>$
            by default None
        degeneracy : int, optional
            band degeneracy, by default 2
        zero_filling : float, optional
            number of bands filled at zero density, density = 0
            corresponds to degeneracy * zero_filling / unit_cell_volume
            by default 0.
        density : float, optional
            electronic density, by default 0.
        temperature : float, optional
            temperature in energy units, by default 0.
        statistics : str, optional
            'F' for Fermi-Dirac, 'B' for Bose-Einstein, 'M' for Maxwell-Boltzmann,
            by default 'F'.

        Returns
        -------
        Band_Structure
            object created from arrays of data
        """
        return cls(
            k_sample=k_sample,
            energies=energies,
            q_sample=q_sample,
            G_sample=G_sample,
            wavefunctions=wavefunctions,
            momentum_matrix=momentum_matrix,
            density_matrix=density_matrix,
            degeneracy=degeneracy,
            zero_filling=zero_filling,
            density=density,
            temperature=temperature,
            statistics = statistics,
            k_plus_q_ind = k_plus_q_ind,
        )

    ########### Properties #############################################

    @property
    def k_sample(self):
        return self._k_sample

    @k_sample.setter
    def k_sample(self, value):
        warn("k_sample cannot be changed.")

    @property
    def q_sample(self):
        return self._q_sample

    @q_sample.setter
    def q_sample(self, value):
        warn("q_sample cannot be changed.")

    @property
    def G_sample(self):
        return self._G_sample

    @G_sample.setter
    def G_sample(self, value):
        warn("G_sample cannot be changed.")

    @property
    def energies(self):
        return self._energies

    @energies.setter
    def energies(self, value):
        warn("energies cannot be changed.")

    @property
    def wavefunctions(self):
        return self._wavefunctions

    @wavefunctions.setter
    def wavefunctions(self, value):
        warn("wavefunctions cannot be changed.")

    @property
    def momentum_matrix(self):
        return self._momentum_matrix

    @momentum_matrix.setter
    def momentum_matrix(self, value):
        warn("momentum_matrix cannot be changed")

    @property
    def density_matrix(self):
        return self._density_matrix

    @density_matrix.setter
    def density_matrix(self, value):
        warn("density_matrix cannot be changed")

    @property
    def degeneracy(self):
        return self._degeneracy

    @degeneracy.setter
    def degeneracy(self, value):
        warn("degeneracy cannot be changed")

    @property
    def zero_filling(self):
        return self._zero_filling

    @zero_filling.setter
    def zero_filling(self, value):
        warn("zero_filling cannot be changed")

    @property
    def statistics(self):
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        warn("statistics cannot be changed")

    @property
    def density(self):
        return self._density

    @density.setter
    def density(self, value):
        warn("changing density without changing band structure")
        self._density = value
        self._chemical_potential = self.compute_chemical_potential(
            self._density, self._temperature
        )
        self._occupations = self.compute_occupations()

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        warn("changing temperature without changing band structure")
        self._temperature = value
        self._chemical_potential = self.compute_chemical_potential(
            self._density, self._temperature
        )
        self._occupations = self.compute_occupations()

    @property
    def chemical_potential(self):
        return self._chemical_potential

    @chemical_potential.setter
    def chemical_potential(self, value):
        warn(
            """changing chemical potential 
                         without changing band structure"""
        )
        self._chemical_potential = value
        self._density = self.compute_density(
            self._chemical_potential, self._temperature
        )
        self._occupations = self.compute_occupations()

    @property
    def occupations(self):
        return self._occupations

    @occupations.setter
    def occupations(self, value):
        warn(
            """occupations cannot be changed directly, change 
            chemical_potential, density or temperature instead"""
        )

    @property
    def distribution_function(self):
        return lambda x : self._distribution_function(
            x - self._chemical_potential, self._temperature)
    @distribution_function.setter
    def distribution_function(self, value):
        warn(
            """distribution_function cannot be changed directly, change 
            chemical_potential, density or temperature instead"""
        )

    @property
    def k_plus_q_ind(self):
        return self._k_plus_q_ind

    @k_plus_q_ind.setter
    def k_plus_q_ind(self, value):
        warn(
            """table of k_plus_q_ind cannot be changed directly"""
        )

    ########### Methods ################################################

    def compute_bands(self, eigvals=None):
        """Comute the band structure by diagonalizing the Hamiltonian

        Parameters
        ----------
        eigvals : tuple of int or None, optional
            bands to be calculated. See scipy.linalg.eigh documentation
            for the definition, by default None, i.e. all eigenvalues
            are calculated.
        """
        ### Check if energies already present.
        #if (not self._energies is None) or (not self._wavefunctions is None):
        #    warn("bandstructure already present, ignoring command")
        #    return
        ### Number of bands to be calculated
        energies, wavefunctions = self._spectrum(
            hamiltonian= self._hamiltonian,
            overlap= self._overlap,
            k_sample = self._k_sample,
            eigvals = eigvals
        )
        ### store results
        self._energies = energies[...]
        self._wavefunctions = wavefunctions[...]
        self._chemical_potential = self.compute_chemical_potential(
            self.density, self.temperature
        )
        self._occupations = self.compute_occupations()
    
    @staticmethod 
    def _spectrum(hamiltonian, overlap, k_sample, eigvals):
        '''Internal function that does the actual diagonalization'''
        if eigvals is None:
            n_bands = hamiltonian.size
        else:
            n_bands = eigvals[1] - eigvals[0] + 1
        ### arrays to store the results
        energies = np.zeros([n_bands, len(k_sample)], dtype=float)
        wavefunctions = np.zeros(
            [hamiltonian.size, n_bands, len(k_sample)], dtype=complex
        )
        ### loop over k points
        for i, k in enumerate(tqdm(k_sample.coords)):
            energies_k, wavefunctions_k = hamiltonian.diagonalize(
                k, overlap=overlap, eigvals=eigvals
            )
            energies[:, i] = energies_k
            wavefunctions[:, :, i] = wavefunctions_k
        return energies, wavefunctions

    def average_operator(self, operator, use_bands=slice(None)):
        """Average a Momentum conserving operator

        Parameters
        ----------
        operator : Operator
            operator to average
        use_bands : slice, optional
            bands to be used in dos computation, by default slice(None)
        Returns
        -------
        average value : complex
            g/L^D\sum_{\bm k,\nu} f_{\bm k, \nu}\langle \bm k \nu|A|\bm k \nu\rangle
        """        
        assert operator.momentum_conserving
        avg = np.zeros([len(self._k_sample)], dtype = float)
        for i, k in enumerate(tqdm(self.k_sample.coords)):
            ###check
            avg[i] = np.real(np.einsum(
                'n,an,ab,bn->', 
                self._occupations[use_bands,i], 
                np.conj(self._wavefunctions[:,use_bands,i]),
                operator(k), 
                self._wavefunctions[:,use_bands,i]
                ))
        return self.integrate_bz(avg, axis = 0)

    def compute_sc_bands(
        self, 
        operators, 
        initial_values,
        transfer_function,
        #variational_functional = None,
        eigvals = None, 
        options = None,
        ):
        """compute self-consistent bands.
        Solve the self-consistent Hamiltonian
        H(k) = H_0(k) + sum_i V[i] A_i(k)
        where H_0 is the single-particle Hamiltonian of the model and
        V is a n-dimensional vector of couplings, and A_i are n 
        MomentumConservingOperators
        The couplings are calculated self-consistently as
        V = f(<A_0>, ..., <A_n-1>)
        where f is a transfer function and <A_i> are the average values 
        of the operators A_i taken on the non-interacting thermal equilibrium 
        state of H(k) at the electronic density and temperature specified by
        self.density and self.temperature respectively.
        Once self-consistency is reached the hamiltonian is substituted 
        with the mean-field hamiltonian H with the converged values of 
        the couplings.

        Parameters
        ----------
        operators : list
            list of n Momentum_Conserving_Operator whose average values
            are computed after each iteration
        transfer_function : callable
            function that takes as input the n average values of operators
            and returns n real couplings
        initial_values : sequence of length n
            initial values of <A_0>, ..., <A_n-1>
        eigvals : tuple of int or None, optional
            bands to be calculated. See scipy.linalg.eigh documentation
            for the definition, by default None, i.e. all eigenvalues
            are calculated.
        options : dict or None, optional
            options to be passed to scipy.optimize.root

        Returns
        -------
        sol : scipy.optimize.OptimizeResult
            output of scipy.optimize.root (final values of <A_0>, ..., <A_n-1>)

        """        
        ### Default options
        if options is None:
            options = {}
        ### initalize class for sc iteration
        sc_iteration = _SC_Iteration(
            k_sample = self._k_sample,
            hamiltonian = self._hamiltonian,
            overlap = self._overlap, 
            degeneracy  = self._degeneracy,
            zero_filling = self._zero_filling,
            density = self._density, 
            temperature = self._temperature, 
            statistics = self._statistics,
            eigvals = eigvals,
            operators = operators, 
        )
        ### solve sc equation
        #if not transfer_function is None:
        sol = root(lambda x : sc_iteration(transfer_function(x), H_0_average = False) - x, 
                   x0 = initial_values, **options)
        # elif not variational_functional is None:
        #     sol = minimize(lambda x : variational_functional(x,*sc_iteration(x, H_0_average = True)),
        #         x0=initial_values, **options)
        print(sol)
        ### mean field hamiltonian with optimized values
        couplings = transfer_function(sol.x)
        H_mf = self._hamiltonian
        for i, operator in enumerate(operators):
            H_mf += couplings[i] * operator
        H_mf.collapse_constant_coefficients()
        self._hamiltonian_mf = H_mf
        ### calculate spectrum
        energies, wavefunctions = self._spectrum(
            hamiltonian= self._hamiltonian_mf,
            overlap= self._overlap,
            k_sample = self._k_sample,
            eigvals = eigvals
        )
        ### store results
        self._energies = energies[...]
        self._wavefunctions = wavefunctions[...]
        self._chemical_potential = self.compute_chemical_potential(
            self.density, self.temperature
        )
        self._occupations = self.compute_occupations()
        ### return converged values
        return sol

    def compute_matrix_elements(self, operator):
        """compute matrix elements of an operator

        Parameters
        ----------
        operator : Operator
            
        """
        if operator.momentum_conserving:
            """Compute matrix elements
            $\langle W_{\bm k}^{(i)}|O|W_{\bm k}^{(j)}^\prime\rangle$
            between wavefunction arrays indexed by a wavevevctor

            Parameters
            ----------
            k_sample : Sample
                sampling of k (initial wavevector)
            wavefunctions : array with shape [size,n_bands,n_k_points]
                left wavefunctions
            wavefunctions2 : array with shape [size,n_bands,n_k_points],
            optional
                right wavefunctions, by default None i.e. use
                left wavefunctions

            Returns
            -------
            array with shape [n_bands, n_bands, n_k_points]
                values of the matrix element
            """
           
            ### initialize array
            n_k_points = len(self.k_sample)
            n_bands = self.wavefunctions.shape[1]
            op_array = np.zeros([n_bands, n_bands, n_k_points], dtype=complex)
            ### iterate over k and q
            for ki in tqdm(range(n_k_points)):
                op_array[:, :, ki] = multi_dot(
                    [
                        np.conj(self.wavefunctions[:, :, ki].T),
                        operator(self.k_sample.coords[ki]),
                        self.wavefunctions[:, :, ki],
                    ]
                )
            return op_array
        else:
            """Compute matrix elements

            $\langle W_{\bm k}^{(i)}|O|W_{\bm k + \bm q}^{(j)}^\prime\rangle$

            between wavefunction arrays indexed by a wavevector

            Parameters
            ----------
            k_sample : Sample
                sampling of k (initial wavevector)
            q_sample : Sample
                sampling of q (transferred wavevector)
            wavefunctions : array with shape [size,n_bands,n_k_points]
                left wavefunctions
            wavefunctions2 : array with shape [size,n_bands,n_k_points],
            optional
                right wavefunctions, by default None i.e. use
                left wavefunctions

            Returns
            -------
            array with shape [n_bands, n_bands, n_k_points, n_q_points]
                values of the matrix element

            array of int with shape [n_q_points, n_k_points]
                table of the index of k + q with respect to k_sample
            """
            ### initialize arrays
            n_k_points = len(self.k_sample)
            n_q_points = len(self.q_sample)
            n_bands = self.wavefunctions.shape[1]
            k_plus_q_tab = np.zeros([n_q_points,n_k_points], dtype = int)
            op_array = np.zeros([n_bands, n_bands, n_k_points, n_q_points], dtype=complex)
            count = 0
            ### iterate over k and q
            for ki in tqdm(range(n_k_points)):
                for qj in range(n_q_points):
                    #integer coords of k+q
                    k_plus_q_int = tsum(self._k_sample.integer_coords[ki], self._q_sample.integer_coords[qj])
                    # checks if k+q has an equivlent in k_sample
                    if k_plus_q_int in self._k_sample:
                        #k+q decomposition
                        data = self._k_sample(k_plus_q_int).copy()
                        #index of the equivalent vector
                        k_plus_q_index = data.pop('index')
                        k_plus_q_tab[qj,ki] = k_plus_q_index
                        # calculate the matrix element
                        op_array[:, :, ki, qj] = multi_dot(
                            [
                                np.conj(self.wavefunctions[:, :, ki].T),
                                operator(self.k_sample.coords[ki], self.q_sample.coords[qj], **data),
                                self.wavefunctions[:, :, k_plus_q_index],
                            ]
                        )
                    else:
                        op_array[:, :, ki, qj] = np.nan
                        count += 1
            if count:
                warn("{} k+q vectors out of {} do not have an equivalent in k_sample ".format(count, n_k_points * n_q_points))
            return op_array, k_plus_q_tab

    def compute_momentum_matrix(self):
        """Compute matrix elements of the momentum operator"""
        ### Check if band structure has been calculated
        if (self._energies is None) or (self._wavefunctions is None):
            warn("bandstructure not available, ignoring command")
            return
        momentum_list = []
        for pi in self._momentum_operator:
            momentum_list.append(
                self.compute_matrix_elements(pi)
            )
        self._momentum_matrix = np.stack(momentum_list)

    def compute_density_matrix(self):
        """Compute matrix elements of the density operator"""
        ### Check if band structure has been calculated
        if (self._energies is None) or (self._wavefunctions is None):
            warn("bandstructure not available, ignoring command")
            return

        ### Check if q_sample and G_sample exist
        if (self._q_sample is None) or (self._G_sample is None):
            warn("q_sample or G_sample not available for calculating density matrix elements, ignoring command")
            return
        # Initialize the density matrix list
        density_list = []
        # Filling the density list running over the density_operator index
        for ni in self._density_operator:
            matrix, table = self.compute_matrix_elements(ni)
            density_list.append(matrix)
            self._k_plus_q_ind = table
        self._density_matrix = np.stack(density_list, axis=-1)

    def save(self, file_name, band_structure_name, file_format="hdf5"):
        """Save band structure data to file.

        Parameters
        ----------
        ----------
        file_name : str
            name of the file from which data are read
        band_structure_name : str
            name of the group inside the file where data are stored
        file_format : str, optional
            format of the input file, only "hdf5" available in this version,
            by default "hdf5"

        """
        if file_format == "hdf5":
            with h5py.File(file_name, "a") as file_to_write:
                file_to_write.create_group(band_structure_name)
                file_to_write[band_structure_name + "/energies"] = self._energies
                file_to_write[
                    band_structure_name + "/wavefunctions"
                ] = self._wavefunctions
                file_to_write[band_structure_name + "/k_points"] = self._k_sample.coords
                ##Saving of k_plus_q_ind
                if not self._k_plus_q_ind is None :
                    file_to_write[band_structure_name + "/k_plus_q_ind"] = self._k_plus_q_ind
                file_to_write[band_structure_name].attrs[
                    "degeneracy"
                ] = self._degeneracy
                file_to_write[band_structure_name].attrs[
                    "zero_filling"
                ] = self._zero_filling
                file_to_write[band_structure_name].attrs["density"] = self._density
                file_to_write[band_structure_name].attrs[
                    "temperature"
                ] = self._temperature

                if not self._momentum_matrix is None:
                    file_to_write[
                        band_structure_name + "/momentum_matrix"
                    ] = self._momentum_matrix

                if not self._density_matrix is None:
                    file_to_write[
                        band_structure_name + "/density_matrix"
                    ] = self._density_matrix
            self._k_sample.save(
                file_name=file_name,
                sample_name=band_structure_name + "/k_sample",
                file_format=file_format,
            )
            if not self._q_sample is None:
                self._q_sample.save(
                    file_name=file_name,
                    sample_name=band_structure_name + "/q_sample",
                    file_format=file_format,
                )
            if not self._G_sample is None:
                self._G_sample.save(
                    file_name=file_name,
                    sample_name=band_structure_name + "/G_sample",
                    file_format=file_format,
                )
        else:
            warn("invalid file_format")

    def plot(self, contour, energy_scale=1.0, emin=None, emax=None, **kwargs):
        """Plot energies along a given path in k space

        Parameters
        ----------
        contour : list
            vertices of the contour. Each element can be an integer index,
            a tuple of rational coordinates or a string labelling a special
            point
        energy_scale : float, optional
            rescaling factor for the energies, by default 1
        emin : float or None, optional
            minimum energy in the plot, by default None
        emax : float or None, optional
            maximum energy in the plot, by default None
        kwargs : keyword arguments to be passed to plt.plot() for band
        plotting

        Returns
        -------
        bands, frame, cp
            plots of bands, frame and chemical potential
        """
        plotting_contour = self._k_sample.contour(contour)
        index = plotting_contour["indices"]
        distances = plotting_contour["x"]
        points = plotting_contour["vertices"]
        if emin is None:
            emin = 1.1 * np.amin(self._energies) - 0.1 * np.amax(self._energies)
        if emax is None:
            emax = 1.1 * np.amax(self._energies) - 0.1 * np.amin(self._energies)
        bands = []
        frame = []
        for i in range(self._energies.shape[0]):
            bands.append(
                plt.plot(distances, energy_scale * self.energies[i, index], **kwargs)
            )
        for point in points:
            frame.append(
                plt.plot(
                    [distances[point], distances[point]],
                    [energy_scale * emin, energy_scale * emax],
                    lw=0.5,
                    c="k",
                )
            )
        cp = plt.plot(
            [distances[0], distances[-1]],
            [self.chemical_potential, self.chemical_potential],
            "--",
            c="k",
            lw=0.5,
        )
        plt.xticks(distances[points], contour)
        plt.ylim(energy_scale * emin, energy_scale * emax)
        return bands, frame, cp

    def integrate_bz(self, array, axis):
        """Integrate an array over the Brillouin zone according to the
        measure $g int_{BZ} \frac{d^D \bm k}{(2\pi)**D}$ where g is the
        degeneracy and D the lattice dimension.

        Parameters
        ----------
        array : array to be integrated. The selected axis must have
        length equal to len(k_sample)
            array to be integrated
        axis : int
            axis to be integrated over

        Returns
        -------
        ndarray
            integrated array with the corresponding axis removed
        """
        return (
            self._k_sample.integrate(array, axis)
            * self.degeneracy
            / ((2.0 * np.pi) ** self.k_sample.lattice_dimension)
        )

    def compute_occupations(
        self, chemical_potential=None, temperature=None, energies=None
    ):
        """compute occupation numbers

        Parameters
        ----------
        chemical_potential : float or None, optional
            chemical potential, by default None i.e. use self._chemical_potential
        temperature : float or None, optional
            temperature in energy units, by default None, i.e use self._temperature
        energies : 2D array of float or None, optional
            energies of the electronic bands, by default None, i.e use self._energies
            Use of differnt energies is intended for use inside self-consistency loops

        Returns
        -------
        array of floats
            array of occupation numbers. same shape as energies
        """
        if chemical_potential is None:
            chemical_potential = self._chemical_potential
        if temperature is None:
            temperature = self._temperature
        if energies is None:
            energies = self._energies
        return self._distribution_function(energies - chemical_potential, temperature)

    def compute_density(self, chemical_potential=None, temperature=None, energies=None):
        """compute electronic density given chemical potential and
        temperature.

        Parameters
        ----------
        chemical_potential : float or None, optional
            chemical potential, by default None i.e. use 
            self._chemical_potential
        temperature : float or None, optional
            temperature in energy units, by default None, i.e 
            use self._temperature
        energies : 2D array of float or None, optional
            energies of the electronic bands, by default None, 
            i.e use self._energies
            Use of differnt energies is intended for use inside 
            self-consistency loops
        Returns
        -------
        float
            electronic density
        """

        occupations = self.compute_occupations(
            chemical_potential=chemical_potential,
            temperature=temperature,
            energies=energies,
        )
        arr = np.sum(occupations, axis=0) - self._zero_filling
        return self.integrate_bz(array=arr, axis=-1)

    def compute_chemical_potential(self, density=None, temperature=None, energies=None):
        """compute the chemical potential at given density and temperature

        Parameters
        ----------
        density : float or None, optional
            electronic density, by default None, i.e. use self.density
        temperature : float or None, optional
            temperature in energy units, by default None, i.e use 
            self._temperature
        energies : 2D array of float or None, optional
            energies of the electronic bands, by default None, i.e use 
            self._energies
            Use of differnt energies is intended for use inside 
            self-consistency loops
        Returns
        -------
        float
            chemical potential
        """
        if density is None:
            density = self._density
        if temperature is None:
            temperature = self._temperature
        if energies is None:
            energies = self._energies

        n_bands = energies.shape[0]
        density_min = (
            -self.zero_filling
            * self.degeneracy
            * self._k_sample.volume
            / ((2.0 * np.pi) ** (self._k_sample.lattice_dimension))
        )
        density_max = (
            density_min
            + n_bands
            * self.degeneracy
            * self._k_sample.volume
            / ((2.0 * np.pi) ** (self._k_sample.lattice_dimension))
        )
        energy_min = np.amin(energies)
        energy_max = np.amax(energies)

        if density > density_min and density < density_max:
            try:
                root = root_scalar(
                    lambda mu: (
                        self.compute_density(
                            chemical_potential=mu,
                            temperature=temperature,
                            energies=energies,
                        )
                        - density
                    ),
                    bracket=[
                        energy_min - 5.0 * temperature,
                        energy_max + 5.0 * temperature,
                    ],
                )
                return root.root
            except:
                try:
                    warn("bracketing failed, fallback to secant method")
                    root = root_scalar(
                        lambda mu: (
                            self.compute_density(
                                chemical_potential=mu,
                                temperature=temperature,
                                energies=energies,
                            )
                            - density
                        ),
                        x0=energy_min,
                        x1=energy_max,
                    )
                    return root.root
                except:
                    warn("failed to calculate chemical potential")
                    return np.nan
        elif density == density_min and temperature == 0.0:
            return energy_min
        elif density == density_min:
            return -np.inf
        elif density == density_max and temperature == 0.0:
            return energy_max
        elif density == density_max:
            return np.inf
        else:
            warn("density value out of range")
            return np.nan

############ Class that performs self-consistent iteration #############

class _SC_Iteration():
    def __init__(
        self,
        k_sample, 
        hamiltonian, 
        overlap , 
        degeneracy,
        zero_filling,
        density, 
        temperature, 
        statistics,
        eigvals,
        operators, 
        ):
        self.k_sample = k_sample
        self.hamiltonian = hamiltonian
        self.overlap = overlap
        self.degeneracy = degeneracy
        self.zero_filling =zero_filling
        self.density = density
        self.temperature = temperature
        self.statistics = statistics
        self.eigvals = eigvals
        self.operators = operators

    def __call__(self, couplings, H_0_average = False):
        '''returns the average values of the operators A_i over the non
        interacting ground-state of H = H_0 + sum_i V[i] A_i with V[i] 
        being the vector of couplings. If H_0_average is true the mean 
        value of H_0 is returned as a separate output'''
        H = self.hamiltonian 
        for i,operator in enumerate(self.operators):
            H += couplings[i] * operator
        H.collapse_constant_coefficients()
        temp_bs = Band_Structure.from_hamiltonian(
            k_sample = self.k_sample,
            hamiltonian = H,
            overlap = self.overlap,
            degeneracy = self.degeneracy,
            zero_filling= self.zero_filling,
            density=self.density,
            temperature = self.temperature,
            statistics=self.statistics
            )
        temp_bs.compute_bands(eigvals = self.eigvals)
        values = [temp_bs.average_operator(operator) for operator in self.operators]
        if H_0_average:
            E_0 = temp_bs.average_operator(self.hamiltonian)
        del(temp_bs)
        if H_0_average:
            return values, E_0
        else:
            return values

########################################################################