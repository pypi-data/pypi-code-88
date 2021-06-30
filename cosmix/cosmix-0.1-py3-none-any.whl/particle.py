"""CosmiX model to generate charge by ionization."""
import numpy as np
import typing as t
from cosmix.util import sampling_distribution


class Particle:
    """Particle class define a particle together with its characteristics."""

    def __init__(self,
                 detector,
                 simulation_mode=None,
                 particle_type=None,
                 input_energy=None, spectrum_cdf=None,
                 starting_pos: t.Optional[t.List[float]] = None,
                 starting_dir: t.Optional[t.List[float]] = None,
                 ) -> None:
        """Creation of a particle according to some parameters.

        :param detector:
        :param simulation_mode:
        :param particle_type:
        :param input_energy:
        :param spectrum_cdf: list
        :param starting_pos: list
        :param starting_dir: list
        """
        self.detector = detector

        # mode_1 = ['cosmic_ray', 'cosmics']
        # mode_2 = ['radioactive_decay', 'snowflakes']
        if simulation_mode == 'cosmic_ray':                 # cosmic rays coming from OUTSIDE the detector volume
            self.starting_position, self.direction, self._surface_points_ = self.isotropic_outer_flux()

            # self._surface_points_ = self.det_surf_intersections(start_point=self.starting_position,
            #                                                     direction=self.direction)

        elif simulation_mode == 'irradiation_beam':         # monoenergetic particle beam in one direction
            self.starting_position, self.direction = np.array(starting_pos), np.array(starting_dir)
            self._surface_points_ = self.det_surf_intersections(start_point=self.starting_position,
                                                                direction=self.direction)

        elif simulation_mode == 'radioactive_decay':        # radioactive decay INSIDE the detector volume
            x0 = self.detector['det_vert_dimension'] * np.random.random()
            y0 = self.detector['det_horz_dimension'] * np.random.random()
            z0 = -1 * self.detector['det_total_thickness'] * np.random.random()
            self.starting_position = np.array([x0, y0, z0])
            self.direction = random_particle_direction()

        # if starting_pos is not None and (isinstance(starting_pos, list) or isinstance(starting_pos, tuple)):
        #     self.starting_position = np.array(starting_pos)
        # if starting_dir is not None and (isinstance(starting_dir, list) or isinstance(starting_dir, tuple)):  # TODO
        #     self.direction = np.array(starting_dir)

        # self._surface_points_ = self.det_surf_intersections(start_point=self.starting_position,
        #                                                     direction=self.direction)

        self.first_position, self.final_position, self.track_length = get_track_length(
            intersection_points=self._surface_points_,
            start_point=self.starting_position,
            direction=self.direction
        )
        self.alpha, self.beta = self.get_angles()  # rad        # TODO CHECK THIS

        self.trajectory = np.copy(self.starting_position)
        self.position = np.copy(self.first_position)
        self.trajectory = np.vstack((self.trajectory, self.position))

        if input_energy is None:
            self.initial_energy = sampling_distribution(spectrum_cdf)
        else:
            self.initial_energy = input_energy
        self.energy = np.copy(self.initial_energy)
        self.deposited_energy = 0.
        self.total_edep = 0.

        self.type = particle_type
        ionizing_particles = ['proton', 'ion', 'alpha', 'beta', 'electron']
        non_ionizing_particles = ['gamma', 'x-ray']     # 'photon'
        if self.type in ionizing_particles:
            # todo: call direct ionization func when needed - already implemented in simulation
            pass
        elif self.type in non_ionizing_particles:
            # todo: call NON-direct ionization func when needed - need to be implemented
            raise NotImplementedError('Given particle type simulation is not yet implemented')
        else:
            raise ValueError('Given particle type can not be simulated')

    def det_surf_intersections(self, start_point, direction):
        """Get surface points intersected by track based on a given point INSIDE or OUTSIDE the detector.

        Good for particles coming from outside the detector.
        :return:
        """
        norm_vectors = [np.array([0., 0., -1.]),    # top plane
                        np.array([0., 0., 1.]),     # bottom plane
                        np.array([0., 1., 0.]),
                        np.array([-1., 0., 0.]),
                        np.array([0., -1., 0.]),
                        np.array([1., 0., 0.])]

        surf_points = [np.array([0., 0., 0.]),                        # top plane
                       np.array([0., 0., -1 * self.detector['det_total_thickness']]),  # bottom plane
                       np.array([0., 0., 0.]),
                       np.array([self.detector['det_vert_dimension'], 0., 0.]),
                       np.array([self.detector['det_vert_dimension'], self.detector['det_horz_dimension'], 0.]),
                       np.array([0., self.detector['det_horz_dimension'], 0.])]

        plane_intersect_points = []
        for i in range(6):
            pts = find_intersection(n=norm_vectors[i], p0=surf_points[i], ls=start_point, lv=direction)
            if pts is not None:
                plane_intersect_points += [pts]

        eps = 1E-8
        det_intersect_points = []
        is_det_intersected = False
        for point in plane_intersect_points:
            if 0.0 - eps <= point[0] <= self.detector['det_vert_dimension'] + eps:
                if 0.0 - eps <= point[1] <= self.detector['det_horz_dimension'] + eps:
                    if -1 * self.detector['det_total_thickness'] - eps <= point[2] <= 0.0 + eps:
                        if np.dot(direction, point - start_point) >= 0.:
                            point = intersection_correction(vert_dim=self.detector['det_vert_dimension'],
                                                            horz_dim=self.detector['det_horz_dimension'],
                                                            thickness=self.detector['det_total_thickness'],
                                                            array=point)
                            det_intersect_points += [point]
                            is_det_intersected = True

        if is_det_intersected:
            return det_intersect_points
        else:
            return None

    def isotropic_outer_flux(self):
        """Random direction from outer sphere uniformly distributed on a sphere.

        Isotropic from a single particle point of view.
        :return:
        """
        diagonal = np.sqrt((self.detector['det_vert_dimension'] ** 2 +
                            self.detector['det_horz_dimension'] ** 2) +
                           self.detector['det_total_thickness'] ** 2)
        rand_normal_vector = random_particle_direction()
        pos_on_sphere = np.array([self.detector['det_vert_dimension'],
                                  self.detector['det_horz_dimension'],
                                  -1 * self.detector['det_total_thickness']]) / 2. + diagonal / 2. * rand_normal_vector
        while True:
            dir = random_particle_direction()
            if np.dot(dir, rand_normal_vector) < 0.:
                det_points = self.det_surf_intersections(start_point=pos_on_sphere, direction=dir)
                if det_points is not None:
                    return pos_on_sphere, dir, det_points

    def get_angles(self):
        """TBW.

        :return:
        """
        beta = np.arccos(np.dot(np.array([1., 0.]), self.direction[0:2]))   # X-Y plane
        alpha = np.arccos(np.dot(np.array([0., 0., 1.]), self.direction))   #
        if self.direction[1] < 0.:      # horizontal direction
            beta += np.pi
            alpha += np.pi
        return alpha, beta


def get_track_length(intersection_points, start_point, direction):
    """Get starting point and length of the track in detector."""
    dist_0 = abs(np.dot(direction, intersection_points[0] - start_point))
    if len(intersection_points) == 1:
        intersection_points += [start_point]
    dist_1 = abs(np.dot(direction, intersection_points[1] - start_point))

    if min(dist_0, dist_1) == dist_0:
        surface_start_point = intersection_points[0]
        surface_end_point = intersection_points[1]
    else:
        surface_start_point = intersection_points[1]
        surface_end_point = intersection_points[0]
    if np.all(surface_start_point == surface_end_point):
        raise ValueError('This should not happen')

    track_length = np.linalg.norm(surface_end_point - surface_start_point)
    return surface_start_point, surface_end_point, track_length


def intersection_correction(vert_dim: float, horz_dim: float,
                            thickness: float, array: np.ndarray):
    """TBW.

    :param vert_dim:
    :param horz_dim:
    :param thickness:
    :param array:
    :return:
    """
    eps = 1E-8
    if abs(array[0] - vert_dim) < eps:
        array[0] = vert_dim
    if abs(array[0]) < eps:
        array[0] = 0.
    if abs(array[1] - horz_dim) < eps:
        array[1] = horz_dim
    if abs(array[1]) < eps:
        array[1] = 0.
    if abs(array[2] + thickness) < eps:
        array[2] = -1 * thickness
    if abs(array[2]) < eps:
        array[2] = 0.
    return array


def find_intersection(n, p0, ls, lv):
    """TBW.

    https://en.wikipedia.org/wiki/Line%E2%80%93plane_intersection
    :param n: normal vector of the plane
    :param p0: point of the plane
    :param ls: starting point of particle track
    :param lv: direction of particle track
    :return:
    """
    if np.dot(lv, n) == 0:   # No intersection of track and detector plane
        return None
    else:
        d = np.dot((p0 - ls), n) / np.dot(lv, n)
        p = d * lv + ls
        return p


def random_particle_direction():
    """Random direction (unit vector) uniformly distributed on a sphere.

    Isotropic from a single particle point of view.
    :return:
    """
    u = 2 * np.random.random() - 1
    r = np.sqrt(1 - u ** 2)
    kszi = np.random.random()
    v = r * np.cos(2 * np.pi * kszi)
    w = r * np.sin(2 * np.pi * kszi)
    return np.array([u, v, w])


# def non_isotropic_direction(n):
#     """TBW.
#
#     THIS IS NOT ISOTROPIC AT ALL!
#     :param n:
#     :return:
#     """
#     alpha = 2 * np.pi * np.random.random(n)
#     beta = 2 * np.pi * np.random.random(n)
#     x = np.cos(alpha) * np.sin(beta)
#     y = np.cos(alpha) * np.cos(beta)
#     z = np.sin(alpha)
#     return x, y, z
