from pathlib import Path
import numpy as np
import sys

from ase import io
from ase.parallel import parprint
from ase.neb import NEB

from cogef.minmax import first_maximum_index, second_minimum_index
from cogef.log import text_stream


def replace_constraint(image, constdict, replacement=None):
    """Replace constraint with the given replacement

    image: atoms object
    constdict: dictionary defining the contraint to be replaced
    replacement: constraint or None
      Deletes constraint if replacement is None (default)
    """
    constraints = []
    for cons in image.constraints:
        if cons.todict() == constdict:
            if replacement is not None:
                constraints.append(replacement)
        else:
            constraints.append(cons)
    image.set_constraint(constraints)


class FixedLength2D:
    """Fixed outer length generalized 2D cogef"""
    def __init__(self, cogef1d, propagator,
                 txt=sys.stdout):
        """
        Parameters:
        -----------

        cogef1d:
           Original cogef1d object that defines starting images and
           outer atoms under constraint.
        propagator:
           The propagator cogef1d changes the second pair
        initialize:
           Optional function to initialize new images
        """
        self.cogef1d = cogef1d
        self.prop = propagator
        self.prop_name = propagator.name

        self.fn = 'fd'
        self.txt = text_stream(txt)

    def _find_extremum(self, stepsize, indices,
                       extremum_function, energy_tolerance,
                       maxsteps, msg=None):
        if indices is None:
            indices = range(len(self.cogef1d.images))

        result = []

        for i in indices:
            energies = self.assign_image_to_propagator(i)
            extremum = extremum_function(energies, energy_tolerance)

            while len(energies) < maxsteps:
                if extremum is not None:
                    break

                # self.prop.pull(stepsize, 1, initialize=self.initialize)
                self.prop.move(stepsize, 1)
                energies.append(
                    self.prop.images[-1].get_potential_energy())
                extremum = extremum_function(energies, energy_tolerance)

            if msg:
                n = len(energies)
                log = f'Image {i}: '
                if extremum is not None:
                    log += f'{msg} at step {n - 1} '
                    log += '{0} eV, E - F*d = {1} eV'.format(
                        self.prop.images[extremum].get_potential_energy(
                            apply_constraint=False),
                        energies[extremum])
                else:
                    log += f'no {msg} within {n} steps'
                self.log(log)

            if extremum is not None:
                result.append(self.prop.images[extremum])
            else:
                result.append(None)

        return result

    def assign_image_to_propagator(self, i):
        """Assign image[i] to progator

        i: int, image index

        Returns all existing energies as a list.
        """
        image = self.set_constraint(i)

        name = Path(self.cogef1d.name) / f'{self.fn}_{i}' / self.prop_name
        self.prop.name = name

        if not len(self.prop.images):
            self.prop.images = [image]

        return [image.get_potential_energy() for image in self.prop.images]

    def find_barrier(self, stepsize,
                     indices=None, energy_tolerance=0.01,
                     maxsteps=100):
        """Evaluate barrier

        stepsize: float, length of propagation steps
        indices: int or list
          image indices to search for the barrier
        energy_tolerance: float, default 0.01
          determines what the criterium for a barrier
        maxsteps: int, maximal number of steps to take, default 100
        """
        return self._find_extremum(stepsize, indices,
                                   first_maximum_index, energy_tolerance,
                                   maxsteps, msg='barrier')

    def find_minimum(self, stepsize,
                     indices=None, energy_tolerance=0.01,
                     maxsteps=100):
        # we need to find the barrier first
        self.find_barrier(stepsize, indices, energy_tolerance, maxsteps)

        return self._find_extremum(stepsize, indices,
                                   second_minimum_index, energy_tolerance,
                                   maxsteps, msg='minimum')

    def set_constraint(self, index):
        # constraint should be present already
        return self.cogef1d.images[index]

    def log(self, messages):
        if isinstance(messages, str):
            messages = [messages]
        for message in messages:
            parprint(message, file=self.txt)

    def neb_barrier(self, indices, energy_tolerance=0.01,
                    nebcls=NEB,
                    nebkwargs={'method': 'eb',
                               'allow_shared_calculator': True}):
        """Recalculate the barrier using Nudged Elastic Bands

        indices: list
        energy_tolerance: float
           acceptance level
        nebcls: class
        nebkwargs: dict
          Arguments for NEB
        """
        for i in indices:
            energies = self.assign_image_to_propagator(i)
            extremum = first_maximum_index(energies, energy_tolerance)
            assert extremum is not None, f'No existing barrier for index {i}'
            barrier_before = energies[extremum] - energies[0]

            fname = Path(self.prop.name) / 'neb.traj'

            try:
                images = [image for image in io.Trajectory(fname)]
            except IOError:
                frestart = Path(self.prop.name) / 'neb_restart.traj'
                try:
                    images = [image for image in io.Trajectory(frestart)]
                except IOError:
                    # initialize inner images and delete propagator constraint
                    images = self.prop.images

                    # XXX NEB does not like changing unit cells -> fix there ?
                    cell = images[-1].cell  # assume last to be the largest

                    assert self.prop.initialize is not None
                    for j, image in enumerate(self.prop.images[:-1]):
                        replace_constraint(image, self.prop.constdict)

                        images[j] = self.prop.initialize(image)

                        # XXX NEB does not like changing unit cells
                        # -> fix there ?
                        images[j].cell = cell

                def write_restart_file(images):
                    with io.Trajectory(frestart, 'w') as traj:
                        for image in images:
                            traj.write(image)

                neb = nebcls(images, **nebkwargs)
                optimizer = self.prop.optimizer(neb)
                optimizer.attach(write_restart_file, 1, images)
                optimizer.run(self.prop.fmax)

                with io.Trajectory(fname, 'w') as traj:
                    for image in images:
                        traj.write(image)

            energies = np.array([image.get_potential_energy()
                                 for image in images])
            extremum = first_maximum_index(energies, energy_tolerance)
            self.log('NEB image {0}: barrier {1:.3f} -> {2:.3f} eV'.format(
                i, barrier_before, energies[extremum] - energies[0]))

    def collect_barriers(self, energy_tolerance=0.01):
        """Return forces and barriers

        energy_tolerance:
          energy tolarance to consider a variation in energy
        """
        forces1d = self.cogef1d.get_forces()
        forces = []
        barriers = []
        for i, _ in enumerate(self.cogef1d.images):
            energies = self.assign_image_to_propagator(i)
            extremum = first_maximum_index(energies, energy_tolerance)

            if extremum is not None:
                barrier = energies[extremum] - energies[0]
                log = 'Image {0} has a barrier of {1:.2f} eV'.format(
                    i, barrier)
                barriers.append(barrier)
                forces.append(forces1d[i])
            elif len(energies) > 1:
                log = 'Image {0} has no barrier in {1} images'.format(
                    i, len(energies))
            else:
                log = []
            self.log(log)

        return np.array(forces), np.array(barriers)
