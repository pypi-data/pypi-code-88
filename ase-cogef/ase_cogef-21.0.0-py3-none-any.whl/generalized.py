from pathlib import Path
import sys
import numpy as np

from ase import io
from ase.constraints import FixBondLength
from ase.parallel import parprint
from ase.utils import deprecated

from cogef import COGEF
from cogef.utilities import mkparent
from cogef.log import text_stream


class COGEF1D(COGEF):
    def __init__(self, atom1, atom2, initialize=None,
                 txt=sys.stdout, **kwargs):
        self.initialize = initialize
        self.txt = text_stream(txt)
        COGEF.__init__(self, atom1, atom2, **kwargs)

    def shift_and_optimize(self, mother, dstep, index):
        """Shift atoms by dstep and optimze

        mother: Atoms
          the Atoms object to be shifted
        dstep: float
          value of the shift
        index:
          index of atoms needed for optimizer trajectory filename

        retruns relaxed atoms
        """
        atoms = mother.copy()

        # file name for optimizer trajectory
        optimizer_traj = (Path(self.name)
                          / 'image{0}.traj'.format(index))

        # check for already existing optimization history
        try:
            atoms = io.read(optimizer_traj)
        except FileNotFoundError:
            mkparent(optimizer_traj)
            atoms = mother.copy()
            self.shift_atoms(atoms, dstep)

        if self.initialize is None:
            atoms.calc = self.images[-1].calc
        else:
            # let the user provided function take care about the image
            atoms = self.initialize(atoms)

        return self._optimize(atoms)

    def _optimize(self, atoms):
        opt = self.optimizer(atoms, logfile=self.optimizer_logfile)
        opt.run(fmax=self.fmax)
        return atoms

    def move(self, dstep, steps):
        if len(self.images) == 1:
            # make sure first image is relaxed
            self.images[0] = self._optimize(self.images[0])

        filename = Path(self.trajname)
        if filename.is_file():
            trajectory = io.Trajectory(filename, 'a')
            assert len(trajectory) == len(self.images)
        else:
            mkparent(filename)
            trajectory = io.Trajectory(filename, 'w')
            for image in self.images:
                trajectory.write(image)

        for i in range(steps):
            parprint(self.__class__.__name__, f'step {i + 1}/{steps}',
                     file=self.txt)
            self.images.append(
                self.shift_and_optimize(
                    self.images[-1], dstep=dstep, index=len(self.images)))
            trajectory.write(self.images[-1])

    @deprecated(DeprecationWarning('Please use move'))
    def pull(self, dstep, steps, initialize=None):
        self.move(dstep, steps)

    def __len__(self):
        return len(self.images)

    def shift_atoms(self, atoms, stepsize):
        # save constraints not equal to own
        myconstraint = self.get_constraint()
        constraints = []
        for constraint in atoms.constraints:
            if constraint.todict() != myconstraint.todict():
                constraints.append(constraint)

        COGEF.shift_atoms(self, atoms, stepsize)

        constraints.append(myconstraint)
        atoms.set_constraint(constraints)

    def get_constraint(self):
        # we need to create a new constraint for every image
        return FixBondLength(self.atom1, self.atom2)

    def get_distances(self):
        return np.array([img.get_distance(self.atom1, self.atom2)
                         for img in self.images])

    def get_energies(self):
        return np.array([img.get_potential_energy()
                         for img in self.images])

    def get_forces(self):
        """Return forces due to constraint"""
        # XXX implement yourself?
        forces, distances = self.get_force_curve('use_forces')
        return forces

    def forces_from_energies(self):
        """Forces from energy derivatives

        returns: distances and corresponding forces
        """
        # XXX implement yourself?
        forces, distances = self.get_force_curve('use_energies')
        return distances, forces

    def look_for_images(self):
        """Check whether there are images already based on the name"""
        try:
            self.images = io.Trajectory(self.trajname)
            parprint(self.__class__.__name__ + ': read', len(self.images),
                     'images from', self.trajname, file=self.txt)
        except FileNotFoundError:
            pass
