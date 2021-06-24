import numpy as np

def static_polarization(energies, occupations, densityG, densityG1, k_p_q_ind, k_weights, integration_constant, eta):
    energy_diff = np.expand_dims(energies, 1) - np.expand_dims(energies[:, k_p_q_ind], 0)
    occupation_diff = np.expand_dims(occupations, 1) - np.expand_dims(occupations[:, k_p_q_ind], 0)
    with np.errstate(divide="ignore"):
        prefactor = occupation_diff * energy_diff/ (energy_diff**2 +eta**2)
    prefactor[np.logical_not(np.isfinite(prefactor))] = 0
    S = (densityG * np.conj(densityG1))
    return integration_constant * np.einsum('nmk,nmk,k->', prefactor,S, k_weights)

def polarization(omega, energies, occupations, densityG, densityG1, k_p_q_ind, k_weights, integration_constant):
    energy_diff = np.expand_dims(energies, 1) - np.expand_dims(energies[:, k_p_q_ind], 0)
    occupation_diff = np.expand_dims(occupations, 1) - np.expand_dims(occupations[:, k_p_q_ind], 0)
    energy_denominator = 1. / (np.expand_dims(energy_diff,3) + np.expand_dims(omega, axis=(0,1,2))) 
    S = (occupation_diff * densityG * np.conj(densityG1))
    return integration_constant * np.einsum('nmk,nmkw,k->w', S,energy_denominator, k_weights)
