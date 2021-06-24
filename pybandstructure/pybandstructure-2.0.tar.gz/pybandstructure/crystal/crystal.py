import numpy as np
from tqdm import tqdm
from pybandstructure.common import *
from pybandstructure.geometry.crystal_geometry import Crystal_Geometry
from pybandstructure.band_structure.band_structure import Band_Structure
from warnings import warn
from pybandstructure.crystal.analysis import dos_functions
from pybandstructure.crystal.analysis import conductivity_functions
from pybandstructure.crystal.analysis import polarization_functions


import matplotlib.pyplot as plt
########## Crystal class ###############################################

class Crystal:
    """Class that contains a geometry and a band structure.
    It has methods to calculate 
    - density of states and related functions
    - optical conductivity and related functions
    - polarization and related functions
    """

    ##### Initialization ###############################################

    def __init__(self, geometry, band_structure, eta=1e-6):
        assert isinstance(geometry, Crystal_Geometry)
        self._geometry = geometry
        assert isinstance(band_structure, Band_Structure)
        self._band_structure = band_structure
        self.eta = eta

        ###### New attributes I am adding ##############################
        self._k_int_const = (self.band_structure.k_sample.volume 
        * self.band_structure.degeneracy 
        /((2.*np.pi)**self.band_structure.k_sample.lattice_dimension))



        self._symmetry_repr = self.geometry.point_group.integer_representation(self.geometry._reciprocal_lattice_basis)

        if not (band_structure.q_sample is None):
            try:
                self._q_int_const = (self.band_structure.q_sample.volume 
                    * self.band_structure.degeneracy 
                    /((2.*np.pi)**self.band_structure.k_sample.lattice_dimension))
            except:
                self._q_int_const = np.nan
            
            q_symmetry_repr = np.zeros([self.geometry._point_group.cardinality, len(self.band_structure.q_sample)], dtype = int)
            for g in range(self.geometry._point_group.cardinality):
                for q_ind in range(len(self.band_structure.q_sample)):
                    tr_vec = tuple(self._symmetry_repr[g, :, :].T @ self.band_structure.q_sample.integer_coords[q_ind])
                    if tr_vec in self.band_structure.q_sample:
                        q_symmetry_repr[g, q_ind]= self.band_structure.q_sample[tr_vec]
                    else:
                        q_symmetry_repr[g, q_ind]= np.nan
            self._q_symmetry_repr = q_symmetry_repr

        if not (band_structure.G_sample is None):
            G_symmetry_repr = np.zeros([self.geometry._point_group.cardinality, len(self.band_structure.G_sample)], dtype = int)
            for g in range(self.geometry._point_group.cardinality):
                for G_ind in range(len(self.band_structure.G_sample)):
                    G_symmetry_repr[g, G_ind] = self.band_structure.G_sample[tuple(self._symmetry_repr[g, :, :].T @ self.band_structure.G_sample.integer_coords[G_ind])]
            self._G_symmetry_repr = G_symmetry_repr
    ###### Properties ##################################################

    @property
    def geometry(self):
        return self._geometry

    @geometry.setter
    def geometry(self, _):
        warn("geometry cannot be changed")

    @property
    def band_structure(self):
        return self._band_structure

    @band_structure.setter
    def band_structure(self, _):
        warn("band_structure cannot be changed")

    ###### Utility functions ###########################################

    def get_transformation_matrix(self, tensor_order):
        if tensor_order > 8 or tensor_order < 1:
            raise ValueError(
                """tensors with at least 1 and at most 8 indices are supported"""
            )
        input_string = ", ".join(
            [chr(ord("a") + i) + chr(ord("i") + i) for i in range(tensor_order)]
        )
        output_string = "".join(
            [chr(ord("a") + i) for i in range(tensor_order)]
        ) + "".join([chr(ord("i") + i) for i in range(tensor_order)])
        path_string = input_string + "->" + output_string
        result_list = [
            np.einsum(path_string, *[rho for i in range(tensor_order)])
            for rho in self.geometry.point_group.group_matrices
        ]
        result = np.sum(result_list, axis=0) / self.geometry.point_group.cardinality
        result = np.round(result, decimals=7)
        result[np.isclose(result, 0.0)] = 0.0
        nz = np.stack(np.nonzero(result)[tensor_order:], axis=1)
        if nz.size != 0:
            non_zero = [tuple(key) for key in np.unique(nz, axis=0)]
        else:
            non_zero = []
        return result, non_zero

    ##### Dos related functions ########################################

    def dos(self, epsilon, use_bands=slice(None), shape = 'lorentz'):
        """density of states

        Parameters
        ----------
        epsilon : 1D array of energies
            energies
        use_bands : slice, optional
            bands to be used in dos computation, by default slice(None)

        Returns
        -------
        1D array with same length of epsilon
            values of the density of states
        """        
        return dos_functions.dos(
            epsilon=epsilon,
            energies=self.band_structure.energies[use_bands,:],
            k_weights = self.band_structure.k_sample.weights,
            integration_constant = self._k_int_const,
            eta=self.eta,
            shape = shape
        )

    def jdos(self, epsilon, nu, mu, shape = 'lorentz'):
        """joint density of states

        Parameters
        ----------
        epsilon : 1D array of energies
            energies
        nu : int
            index of the first band
        mu : int
            index of the second band

        Returns
        -------
        1D array with same length of epsilon
            values of the joint density of states
        """        
        return dos_functions.jdos(
            epsilon=epsilon,
            nu=nu,
            mu=mu,
            energies=self.band_structure.energies,
            k_weights = self.band_structure.k_sample.weights,
            integration_constant = self._k_int_const,
            eta=self.eta,
            shape =shape
        )

    ###### Conductivity related functions ##############################

    def local_interband_conductivity(self, omega, use_bands=slice(None)):
        """local conductivity due to interband processes

        Parameters
        ----------
        omega : 1D array of float or complex 
            values of the angular frequency
        use_bands : slice, optional
            bands to be used in dos computation, by default slice(None)

        Returns
        -------
        array [omega,i,j]
            values of the interband conductivity
        """        
        omega = np.atleast_1d(np.array(omega, dtype = complex))

        energy_diff = np.expand_dims(
            self.band_structure.energies[use_bands, :], 1
        ) - np.expand_dims(self.band_structure.energies[use_bands, :], 0)

        occupation_diff = np.expand_dims(
            self.band_structure.occupations[use_bands, :], 1
        ) - np.expand_dims(self.band_structure.occupations[use_bands, :], 0)

        transformation_matrix, nonzero_components = self.get_transformation_matrix(
            tensor_order=2
        )

        sigma_IBZ = np.zeros(
            [self.geometry.space_dimension, self.geometry.space_dimension, len(omega)],
            dtype=complex,
        )
        for alpha, beta in nonzero_components:
            sigma_IBZ[alpha, beta,:] = conductivity_functions.local_conductivity_interband(
                omega=omega +1.j* self.eta,
                energy_diff=energy_diff,
                occupation_diff=occupation_diff,
                momentum_matrix_alpha = self.band_structure.momentum_matrix[alpha, use_bands, use_bands,:],
                momentum_matrix_beta = self.band_structure.momentum_matrix[beta, use_bands, use_bands,:],
                k_weights = self.band_structure.k_sample.weights,
                integration_constant = self._k_int_const)
        return np.einsum('ijab,abw->wij',transformation_matrix, sigma_IBZ)

    def generalized_drude_weight(
        self,
        chemical_potential=None,
        temperature=None,
        exponent=0,
        use_bands=slice(None),
    ):
        """generalized_drude_weight

        Parameters
        ----------
        chemical_potential : 1D array of float, optional
            chemical potential, by default None, i.e. value from band_structure
        temperature : 1D array of float, optional
            temperature, by default None, i.e. value from band_structure
        exponent : int, optional
            exponent of the generalized Drude weight, by default 0
        use_bands : slice, optional
            bands to be used in dos computation, by default slice(None)

        Returns
        -------
        array [chemical_potential, temperature,i,j]
            values of generalized Drude weight
        """    
        if chemical_potential is None:
            chemical_potential = self.band_structure.chemical_potential
        if temperature is None:
            temperature = self.band_structure.temperature
        momentum_matrix_intra = np.real(
            np.einsum(
                "annk->ank",
                self.band_structure.momentum_matrix[:, use_bands, use_bands, :],
            )
        )
        transformation_matrix, nonzero_components = self.get_transformation_matrix(
            tensor_order=2
        )
        result = []
        b = np.broadcast(chemical_potential, temperature)
        for mu_val, T_val in b:
            drude_IBZ = np.zeros(
                [self.geometry.space_dimension, self.geometry.space_dimension],
                dtype=float,
            )
            for alpha, beta in nonzero_components:
                drude_IBZ[alpha, beta] = conductivity_functions.generalized_drude_weight(
                    exponent=exponent,
                    energies=self.band_structure.energies[use_bands, :],
                    chemical_potential=mu_val,
                    temperature=T_val,
                    momentum_matrix_intra_alpha =momentum_matrix_intra[alpha,:,:],
                    momentum_matrix_intra_beta =momentum_matrix_intra[beta,:,:],
                    k_weights = self.band_structure.k_sample.weights,
                    integration_constant = self._k_int_const)
            result.append(np.tensordot(transformation_matrix, drude_IBZ, axes=2))
        return np.array(result).reshape(
            b.shape + (self.geometry.space_dimension, self.geometry.space_dimension)
        )

    def local_intraband_conductivity(self, omega, use_bands=slice(None)):
        """local conductivity due to intraband processes


        Parameters
        ----------
        omega : 1D array of float or complex
            values of the angular frequency
        use_bands : [type], optional
            [description], by default slice(None)

        Returns
        -------
        array [omega,i,j]
            values of the intraband conductivity
        """        
        D = self.generalized_drude_weight(use_bands=use_bands)
        return 1j * np.einsum('ij,w->wij',D, 1./(omega + 1j * self.eta))

    def local_conductivity(self, omega, use_bands=slice(None)):
        """local conductivity

        Parameters
        ----------
        omega : 1D array of float or complex
            values of the angular frequency
        use_bands : [type], optional
            [description], by default slice(None)

        Returns
        -------
        array [omega,i,j]
            values of the intraband conductivity
        """        
        return self.local_intraband_conductivity(
            omega, use_bands=use_bands
        ) + self.local_interband_conductivity(omega, use_bands=use_bands)

    ###### Polarization functions ######################################

    def static_polarization(self, q_index, G_index, G1_index, use_bands=slice(None), eta = None):
        """Returns the static polarization value

                Parameters
                ----------
                q_index : int
                    index of the transferred momentum q = self.band_structure.q_sample.coords[q_index]
                G_index : int
                    index of the reciprocal wavevector G = self.band_structure.G_sample.coords[G_index]
                G1_index : int
                    index of the reciprocal wavevector G1 = self.band_structure.G_sample.coords[G1_index]
                use_bands : slice, optional
                    bands to be used in the calculation, by default slice(None)

                Returns
                -------
                complex scalar
                    value of the polarization function in omega=0
        """
        if eta is None:
            eta = self.eta
        if self.geometry._point_group.cardinality != 1:
            warn('Computing polarization with non-trivial point group is an experimental feature')

        static_polarization = complex(0, 0)
        
        for g in range(self.geometry._point_group.cardinality):
            static_polarization += polarization_functions.static_polarization(
                energies=self.band_structure.energies[use_bands, :],
                occupations = self.band_structure.occupations[use_bands, :],
                densityG = np.nan_to_num(self.band_structure.density_matrix[
                                    use_bands,
                                    use_bands,
                                    :,
                                    self._q_symmetry_repr[g, q_index],
                                    self._G_symmetry_repr[g, G_index]
                                    ]),
                densityG1 = np.nan_to_num(self.band_structure.density_matrix[
                                    use_bands,
                                    use_bands,
                                    :,
                                    self._q_symmetry_repr[g, q_index],
                                    self._G_symmetry_repr[g, G1_index]
                                    ]),
                k_p_q_ind = self.band_structure._k_plus_q_ind[self._q_symmetry_repr[g, q_index], :],
                k_weights = self.band_structure.k_sample.weights,
                integration_constant = self._k_int_const,
                eta = eta
            )
        return static_polarization / self.geometry._point_group.cardinality


    def polarization(self, omega, q_index, G_index, G1_index, use_bands=slice(None)):
        """Returns the polarization function 

        Parameters
        ----------
        omega : 1D array of complex (for example of the form omega + 1j*eta)
            values of the angular frequency
        q_index : int
            index of the transferred momentum q = self.band_structure.q_sample.coords[q_index]
        G_index : int
            index of the reciprocal wavevector G = self.band_structure.G_sample.coords[G_index]
        G1_index : int
            index of the reciprocal wavevector G1 = self.band_structure.G_sample.coords[G1_index]
        use_bands : slice, optional
            bands to be used in the calculation, by default slice(None)

        Returns
        -------
        ndarray of complex with the same shape as omega
            value of the polarixation function
        """        
        if self.geometry._point_group.cardinality != 1:
            warn('Computing polarization with non-trivial point group is an experimental feature')

        polarization = np.zeros_like(omega, dtype = complex)

        for g in range(self.geometry._point_group.cardinality):
            polarization += polarization_functions.polarization(
                omega = omega,
                energies=self.band_structure.energies[use_bands,:],
                occupations=self.band_structure.occupations[use_bands,:],
                densityG = np.nan_to_num(self.band_structure.density_matrix[
                    use_bands,
                    use_bands,
                    :,
                    self._q_symmetry_repr[g,q_index],
                    self._G_symmetry_repr[g,G_index]
                    ]),
                densityG1=np.nan_to_num(self.band_structure.density_matrix[
                    use_bands,
                    use_bands,
                    :,
                    self._q_symmetry_repr[g,q_index],
                    self._G_symmetry_repr[g,G1_index]
                    ]),
                k_p_q_ind = self.band_structure._k_plus_q_ind[self._q_symmetry_repr[g,q_index],:],
                k_weights = self.band_structure.k_sample.weights,
                integration_constant = self._k_int_const)
        return polarization / self.geometry._point_group.cardinality