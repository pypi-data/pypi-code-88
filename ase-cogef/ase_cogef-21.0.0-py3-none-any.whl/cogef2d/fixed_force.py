import numpy as np

from ase.constraints import ExternalForce

from .fixed_length import FixedLength2D, replace_constraint


class FixedForce2D(FixedLength2D):
    """Fixed outer force generalized 2D cogef"""
    def __init__(self, *args, **kwargs):
        FixedLength2D.__init__(self, *args, **kwargs)
        self.fn = 'ff'

    def set_constraint(self, index):
        """Replace FixBondlength with FixForce

        """
        f_ext = self.cogef1d.constraint_force(index)
        image = self.cogef1d.images[index]

        a1, a2 = self.cogef1d.atom1, self.cogef1d.atom2
        replace_constraint(image, self.cogef1d.constdict,
                           ExternalForce(a1, a2, f_ext))

        return image
