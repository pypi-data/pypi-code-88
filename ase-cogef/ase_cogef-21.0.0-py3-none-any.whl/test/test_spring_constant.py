import pytest

from ase.build import molecule
from ase.calculators.morse import MorsePotential
from ase.optimize import FIRE
from cogef import COGEF


# XXX see ase-gui tests how to automatically close windows
@pytest.mark.xfail(reason='bug: test fails and should close window again')
def test_fit(tmp_path):
    image = molecule('H2')
    image.calc = MorsePotential()
    fmax = 0.01
    FIRE(image, logfile=None).run(fmax=fmax)

    atom1 = 0
    atom2 = 1
    steps = 15
    stepsize = 0.01

    cogef = COGEF(atom1, atom2, fmax=fmax, optimizer_logfile=None)
    cogef.images = [image]
    cogef.pull(stepsize, steps)

    IMIN = 0
    IMAX = 15

    # XXX close window automatically
    plot = False
    k = cogef.get_spring_constant(atom1, atom2, IMIN=IMIN, IMAX=IMAX,
                                  images=cogef.images, plot=plot)
    assert k == pytest.approx(573)
