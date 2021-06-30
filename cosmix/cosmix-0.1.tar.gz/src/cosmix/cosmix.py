"""CosmiX model to generate charge by ionization."""
# import logging
import math
import numpy as np
from tqdm import tqdm
from cosmix.simulation import Simulation
from cosmix.util import read_data
from cosmix.plotting import Plotting


def run_cosmix(detector,
               simulation_mode: str,
               # simulation_mode: str = 'irradiation_beam',
               # simulation_mode: str = 'cosmic_ray',
               particle_type: str = 'proton',
               particle_number: int = 10,              # -
               # initial_energy: float = 0.,              # MeV
               initial_energy: float = 9990.,           # MeV
               # initial_energy: float = 100.,          # MeV
               # initial_energy: float = 1000.,         # MeV
               spectrum_file: str = 'data/proton_L2_solarMax_11mm_Shielding.txt',  # MeV
               starting_position: list = np.array([500., 500., 1.]),   # None,      # um
               beam_direction: list = np.array([0, 0, -1]),      # None,      # -
               random_seed: int = 11111):
    """Simulate charge deposition by cosmic rays.

    :param detector: Pyxel detector object
    :param simulation_mode: simulation mode: ``cosmic_rays``    # ``radioactive_decay``
    :param particle_type: type of particle: ``proton``          # ``alpha``, ``ion``
    :param particle_number: Number of particles
    :param initial_energy: Kinetic energy of particle in MeV
    :param spectrum_file: path to input spectrum in MeV
    :param starting_position: starting position: ``[x, y, z]`` in um
    :param beam_direction: ``[u, v, w]`` unit vector
    :param random_seed: seed
    """
    # logger = logging.getLogger('pyxel')
    # logger.info('')
    if random_seed:
        np.random.seed(random_seed)

    if isinstance(detector, dict):
        det = detector
    else:
        geo = detector.geometry
        det = {
            'det_vert_dimension':   geo.vert_dimension,     # um
            'det_horz_dimension':   geo.horz_dimension,     # um
            'det_total_thickness':  geo.total_thickness     # um
        }

    spectrum = None
    if initial_energy == 0.:
        spectrum = read_data(spectrum_file)                         # x: MeV , y: nuc/m2*s*sr*MeV

        # TODO: this is not needed now, but needed for other spectra,
        #  depending on the spectrum file content (weigths)

        detector_area = det['det_vert_dimension'] * det['det_horz_dimension'] * 1.0e-8    # cm^2
        spectrum[:, 1] *= 4 * math.pi * 1.0e-4 * detector_area      # x: MeV , y: nuc/s*MeV
        # TODO detector area or detector surface??

        cum_sum = np.cumsum(spectrum[:, 1])
        cum_sum /= np.max(cum_sum)
        spectrum, _ = np.stack((spectrum[:, 0], cum_sum), axis=1), spectrum[:, 1]

    cosmix = Simulation(detector=det,
                        simulation_mode=simulation_mode,
                        particle_type=particle_type,
                        initial_energy=initial_energy,
                        spectrum=spectrum,
                        starting_position=starting_position,
                        beam_direction=beam_direction)

    for k in tqdm(range(0, particle_number)):

        e_cluster_size_lst, e_pos0_lst, e_pos1_lst, e_pos2_lst = cosmix.event_generation()

        if isinstance(detector, dict):
            pass
        # within Pyxel:
        else:
            size = len(e_cluster_size_lst)
            detector.charge.add_charge('e',
                                       e_cluster_size_lst,
                                       [0.] * size,
                                       e_pos0_lst, e_pos1_lst, e_pos2_lst,
                                       [0.] * size, [0.] * size, [0.] * size)

        if k % 100 == 0 or k == particle_number - 1:
            np.save('outputs/cosmix_electron_per_event', cosmix.electron_per_event)
            np.save('outputs/cosmix_p_init_energy_lst_per_event', cosmix.p_init_energy_lst_per_event)
            np.save('outputs/cosmix_p_final_energy_lst_per_event', cosmix.p_final_energy_lst_per_event)
            np.save('outputs/cosmix_track_length_lst_per_event', cosmix.track_length_lst_per_event)
            np.save('outputs/cosmix_edep_per_event', cosmix.edep_per_event)
            np.save('outputs/cosmix_step_size_lst_per_step', cosmix.step_size_lst_per_step)

            np.save('outputs/cosmix_angle_alpha_lst_per_event', cosmix.angle_alpha_lst_per_event)
            np.save('outputs/cosmix_angle_beta_lst_per_event', cosmix.angle_beta_lst_per_event)
            np.save('outputs/cosmix_starting_pos_lst_per_event', cosmix.starting_pos_lst_per_event)
            np.save('outputs/cosmix_first_pos_lst_per_event', cosmix.first_pos_lst_per_event)
            np.save('outputs/cosmix_last_pos_lst_per_event', cosmix.last_pos_lst_per_event)
            np.save('outputs/cosmix_direction_lst_per_event', cosmix.direction_lst_per_event)

            np.save('outputs/cosmix_charge_num', cosmix.e_cluster_size_lst)
            np.save('outputs/cosmix_charge_v_pos', cosmix.e_pos0_lst_per_event)
            np.save('outputs/cosmix_charge_h_pos', cosmix.e_pos1_lst_per_event)
            np.save('outputs/cosmix_charge_z_pos', cosmix.e_pos2_lst_per_event)

    # winsound.Beep(440, 2000)
    # print('Done.')


if __name__ == '__main__':

    plato_ccd = {
        'det_vert_dimension': 1000.,  # um
        'det_horz_dimension': 1000.,  # um
        'det_total_thickness': 15.  # um
    }
    gaia_bam_ccd = {
        'det_vert_dimension': 1000.,  # um
        'det_horz_dimension': 1000.,  # um
        'det_total_thickness': 40.  # um
    }
    det, mode = plato_ccd, 'irradiation_beam'
    # det, mode = gaia_bam_ccd, 'cosmic_ray'

    run_cosmix(detector=det, simulation_mode=mode)

    plots = Plotting(show_plots=True, output_dir='outputs', geometry=det)

    # current_dir = 'outputs/run-10k-55MeV-2um/'
    current_dir = 'outputs/'

    plots.cluster_positions(chg_v_pos=current_dir + 'cosmix_charge_v_pos.npy',
                            chg_h_pos=current_dir + 'cosmix_charge_h_pos.npy',
                            chg_z_pos=current_dir + 'cosmix_charge_z_pos.npy')
    #
    plots.cluster_charges_3d(chg_v_pos=current_dir + 'cosmix_charge_v_pos.npy',
                             chg_h_pos=current_dir + 'cosmix_charge_h_pos.npy',
                             chg_z_pos=current_dir + 'cosmix_charge_z_pos.npy',
                             chg_num=current_dir + 'cosmix_charge_num.npy')

    plots.event_polar_angle_dist(alpha=current_dir + 'cosmix_angle_alpha_lst_per_event.npy',
                                 beta=current_dir + 'cosmix_angle_beta_lst_per_event.npy')

    plots.event_direction_hist(direction=current_dir + 'cosmix_direction_lst_per_event.npy')

    plots.event_tracks_3d(first_pos=current_dir + 'cosmix_first_pos_lst_per_event.npy',
                          last_pos=current_dir + 'cosmix_last_pos_lst_per_event.npy')

    plots.event_electrons_deposited(elec=current_dir + 'cosmix_electron_per_event.npy')

    plots.event_proton_spectra(init=current_dir + 'cosmix_p_init_energy_lst_per_event.npy',
                               final=current_dir + 'cosmix_p_final_energy_lst_per_event.npy')

    plots.event_starting_position(start_pos=current_dir + 'cosmix_starting_pos_lst_per_event.npy')

    plots.cluster_charge_number(chg_num=current_dir + 'cosmix_charge_num.npy')
    plots.cluster_step_size(step_size=current_dir + 'cosmix_step_size_lst_per_step.npy')

    plots.plot_plato_hists(edep=current_dir + 'cosmix_edep_per_event.npy',
                           elec=current_dir + 'cosmix_electron_per_event.npy')

    # plots.event_energy_deposited(edep=current_dir + 'cosmix_edep_per_event.npy')

    plots.show()
