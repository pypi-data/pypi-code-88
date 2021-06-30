"""CosmiX model to generate charge by ionization."""
import typing as t  # noqa: F401
import numpy as np
from cosmix.particle import Particle
from cosmix.util import sampling_distribution
from cosmix.util import find_smaller_neighbor, load_cdf, read_data_library_new
from cosmix.util import create_data_library_new


class Simulation:
    """Main class of the program, Simulation contain all the methods to set and run a simulation."""

    def __init__(self, detector,
                 simulation_mode,
                 particle_type,
                 initial_energy,
                 starting_position: t.Optional[t.List[float]] = None,
                 beam_direction: t.Optional[t.List[float]] = None,
                 spectrum=None) -> None:
        """Initialize the simulation.

        :param detector:
        :param simulation_mode:
        :param particle_type:
        :param initial_energy:
        :param starting_position:
        :param beam_direction:
        :param spectrum:
        """
        self.detector = detector
        self.simulation_mode = simulation_mode
        self.particle_type = particle_type

        # ###############################
        # self.library_thickness_str = '300nm'     # type: str  # with 'um' or 'nm'
        self.library_thickness_str = '2um'      # type: str     # with 'um' or 'nm'
        # self.library_thickness_str = '15um'      # type: str     # with 'um' or 'nm'

        # self.thickness_gauge = 0.3               # type: float  # in um
        self.thickness_gauge = 2.               # type: float   # in um
        # self.thickness_gauge = 15.               # type: float   # in um

        # ONLY NEEDED TO RUN THIS ONCE TO GENERATE DATA LIBRARY FROM DATAFILES:
        create_data_library_new(thickness=self.library_thickness_str)

        self.mean_ionization_energy = 3.6e-3    # type: float  # in keV
        self.energy_cut = 0.1                   # type: float  # in MeV
        self.e_limit = 30000                    # type: int    # in electrons
        # ###############################

        self.step_data_library = None
        self.elec_data_library = None
        self.edep_data_library = None
        self.energy_groups = None

        self.step_data_library, self.elec_data_library, self.edep_data_library = read_data_library_new()
        self.energy_groups = sorted(self.step_data_library['energy'].unique())

        self.beam_position = starting_position
        self.beam_direction = beam_direction

        self.spectrum_cdf = None
        self.initial_energy = None
        if initial_energy == 0.:
            self.spectrum_cdf = spectrum
        else:
            self.initial_energy = initial_energy

        self.p_init_energy_lst_per_event = []      # type: t.List[float]
        self.p_final_energy_lst_per_event = []     # type: t.List[float]
        self.track_length_lst_per_event = []       # type: t.List[float]

        self.angle_alpha_lst_per_event = []       # type: t.List[float]
        self.angle_beta_lst_per_event = []        # type: t.List[float]
        self.direction_lst_per_event = []         # type: t.List[np.array]
        self.starting_pos_lst_per_event = []        # type: t.List
        self.first_pos_lst_per_event = []           # type: t.List
        self.last_pos_lst_per_event = []            # type: t.List

        self.e_cluster_size_lst = []              # type: t.List
        self.e_pos0_lst_per_event = []            # type: t.List
        self.e_pos1_lst_per_event = []            # type: t.List
        self.e_pos2_lst_per_event = []            # type: t.List

        self.step_size_lst_per_step = []            # type: t.List[float]
        self.electron_lst_per_step = []             # type: t.List[float]

        self.edep_per_event = []                    # type: t.List[float]
        self.electron_per_event = []                # type: t.List[float]

    def event_generation(self):
        """Generate an event.

        :return:
        """
        e_cluster_size_lst = []
        e_pos0_lst, e_pos1_lst, e_pos2_lst = [], [], []

        edep_total = 0.
        electron_total = 0

        particle = Particle(detector=self.detector,
                            simulation_mode=self.simulation_mode,
                            particle_type=self.particle_type,
                            input_energy=self.initial_energy,
                            spectrum_cdf=self.spectrum_cdf,
                            starting_pos=self.beam_position,
                            starting_dir=self.beam_direction)

        current_energy_grp = find_smaller_neighbor(sorted_array=self.energy_groups, value=particle.energy)
        # print('current energy grp: %.3f MeV' % current_energy_grp)
        # because protons lose energy, smaller energy is probably a better estimation than closest energy...
        stepsize_cdf = load_cdf(df=self.step_data_library, p_energy=current_energy_grp)
        # step_size_limit = np.power(10, stepsize_cdf[-2, 0]) * 1000
        edep_cdf = load_cdf(df=self.edep_data_library, p_energy=current_energy_grp)

        # import matplotlib.pyplot as plt
        # plt.plot(edep_cdf[:, 0], edep_cdf[:, 1])
        # plt.show()

        last_chg_dep_point = np.copy(particle.position)

        while True:
            # particle.energy is in MeV !
            # particle.deposited_energy is in keV !
            if particle.energy <= self.energy_cut:
                # print('WARNING: Energy below cut value (100 keV)!')
                break   # TODO
            if electron_total > self.e_limit:
                # print('WARNING: Too many electrons !')
                break   # TODO

            current_step_size = np.power(10, sampling_distribution(stepsize_cdf)) * 1000.   # um
            self.step_size_lst_per_step += [current_step_size]

            # UPDATE POSITION OF IONIZING PARTICLES
            particle.position += particle.direction * current_step_size    # um

            # check if particle is still inside detector:
            particle_left_volume = self.is_particle_left_volume(particle.position)

            # if particle_left_volume:  # PARTICLE LEFT VOLUME...
            #     break
            # else:
            #     distance = np.linalg.norm(particle.position - last_chg_dep_point)    # um

            distance = np.linalg.norm(particle.position - last_chg_dep_point)                   # um
            remaining_distance = np.linalg.norm(particle.final_position - last_chg_dep_point)   # um

            # IF PARTICLE TRAVELLED THE GAUGE DIST AND THE CURRENT STEP IS SHORTER THAN WHOLE TRACK LENGTH:
            if distance >= self.thickness_gauge and current_step_size < particle.track_length:

                factor = distance / self.thickness_gauge
                relative_cluster_distance = distance * np.random.random()

                # TOTAL DEPOSITED ENERGY DURING LAST (NOT FINAL 2) STEP (>= thickness_gauge (2 um)),
                # THE DEPOSITED ENERGY IS PROPORTIONAL TO THE DISTANCE, and it is in keV
                edep_prev_step = factor * sampling_distribution(edep_cdf) * 1000  # keV
                # print(factor)

                # CALCULATE DEPOSITED ELECTRONS WITH MATERIAL DEPENDENT (Si) MEAN ELECTRON-HOLE PAIR CREATION ENERGY
                electron_number_prev_step = edep_prev_step / self.mean_ionization_energy

                # TOTAL EDEP AND ELEC PER EVENT
                edep_total += edep_prev_step
                electron_total += electron_number_prev_step

                # LIST OF ELEC PER STEP (CLUSTER SIZE) FOR WHOLE EVENT
                e_cluster_size_lst += [electron_number_prev_step]

                # GET RANDOM CLUSTER POSITION WITHIN PREVIOUS STEP

                cluster_position = last_chg_dep_point + particle.direction * relative_cluster_distance  # um
                e_pos0_lst += [cluster_position[0]]   # um
                e_pos1_lst += [cluster_position[1]]   # um
                e_pos2_lst += [cluster_position[2]]   # um

                # THE NEW LAST POINT WHERE CHARGE DEPOSITION CALCULATED, NEXT STEP STARTS AT THIS POINT
                last_chg_dep_point = np.copy(particle.position)

                # IF THE NEXT ONE IS THE FINAL STEP
                if 0. < remaining_distance < self.thickness_gauge:

                    relative_cluster_distance = self.thickness_gauge * np.random.random()
                    if relative_cluster_distance < remaining_distance:

                        factor = remaining_distance / self.thickness_gauge

                        edep_prev_step = factor * sampling_distribution(edep_cdf) * 1000  # keV
                        # print(factor)

                        # CALCULATE DEPOSITED ELECTRONS WITH MATERIAL DEPENDENT (Si)
                        # MEAN ELECTRON-HOLE PAIR CREATION ENERGY
                        electron_number_prev_step = edep_prev_step / self.mean_ionization_energy

                        # TOTAL EDEP AND ELEC PER EVENT
                        edep_total += edep_prev_step
                        electron_total += electron_number_prev_step

                        # LIST OF ELEC PER STEP (CLUSTER SIZE) FOR WHOLE EVENT
                        e_cluster_size_lst += [electron_number_prev_step]

                        # GET RANDOM CLUSTER POSITION WITHIN PREVIOUS STEP
                        cluster_position = last_chg_dep_point + particle.direction * relative_cluster_distance  # um
                        e_pos0_lst += [cluster_position[0]]  # um
                        e_pos1_lst += [cluster_position[1]]  # um
                        e_pos2_lst += [cluster_position[2]]  # um

                        particle.position = particle.final_position

                        # THE NEW LAST POINT WHERE CHARGE DEPOSITION CALCULATED, NEXT STEP STARTS AT THIS POINT
                        last_chg_dep_point = np.copy(particle.position)

            if particle_left_volume:  # PARTICLE LEFT VOLUME...
                break

            particle.trajectory = np.vstack((particle.trajectory, particle.position))

        # END of while loop

        self.p_init_energy_lst_per_event += [particle.initial_energy]
        self.p_final_energy_lst_per_event += [particle.energy]
        self.track_length_lst_per_event += [particle.track_length]

        self.angle_alpha_lst_per_event += [particle.alpha]
        self.angle_beta_lst_per_event += [particle.beta]
        self.direction_lst_per_event += [particle.direction]
        self.starting_pos_lst_per_event += [particle.starting_position]
        self.first_pos_lst_per_event += [particle.first_position]
        self.last_pos_lst_per_event += [particle.final_position]

        self.edep_per_event += [edep_total]
        self.electron_per_event += [electron_total]

        self.e_cluster_size_lst += [e_cluster_size_lst]
        self.e_pos0_lst_per_event += [e_pos0_lst]
        self.e_pos1_lst_per_event += [e_pos1_lst]
        self.e_pos2_lst_per_event += [e_pos2_lst]

        return e_cluster_size_lst, e_pos0_lst, e_pos1_lst, e_pos2_lst

    def is_particle_left_volume(self, position):
        """TBW."""
        particle_left_volume = False
        if position[0] <= 0.:
            particle_left_volume = True
            position[0] = 0.
        if position[0] >= self.detector['det_vert_dimension']:
            particle_left_volume = True
            position[0] = self.detector['det_vert_dimension']
        if position[1] <= 0.:
            particle_left_volume = True
            position[1] = 0.
        if position[1] >= self.detector['det_horz_dimension']:
            particle_left_volume = True
            position[1] = self.detector['det_horz_dimension']
        if position[2] >= 0.:
            particle_left_volume = True
            position[2] = 0.
        if position[2] <= -1 * self.detector['det_total_thickness']:
            particle_left_volume = True
            position[2] = -1 * self.detector['det_total_thickness']
        return particle_left_volume
