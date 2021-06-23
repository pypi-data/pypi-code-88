import pytest

from ase import Atoms
from ase.calculators.morse import MorsePotential

from cogef.generalized import COGEF1D
from cogef import Dissociation


@pytest.fixture
def cogef1d(H6):
    cogef = COGEF1D(0, 5, txt=None)
    cogef.images = [H6]

    cogef.move(0.2, 5)
    return cogef


@pytest.fixture
def dimer():
    H2 = Atoms('H2', positions=[[0, 0, 0], [1, 0, 0]])
    H2.calc = MorsePotential()

    cogef = COGEF1D(0, 1, txt=None)
    cogef.images = [H2]
    cogef.move(0.02, 20)
    return cogef


def test_modified_energies_H6(cogef1d):
    energies = cogef1d.get_energies()
    diss = Dissociation(cogef1d)

    assert diss.modified_energies(0., False) == pytest.approx(energies, 1.e-8)
    energies -= energies.min()
    assert diss.modified_energies(0.) == pytest.approx(energies, 1.e-8)

    # applied force should lower energies
    assert (diss.modified_energies(0.2)[1:] < energies[1:]).all()


def test_modified_energies_H2(dimer):
    energies = dimer.get_energies()
    diss = Dissociation(dimer)

    assert diss.modified_energies(0., False) == pytest.approx(energies, 1.e-8)
    assert (diss.modified_energies(0.)
            == pytest.approx(energies - energies.min(), 1.e-8))

    F = 6 / 5
    distances = dimer.get_distances()
    assert (diss.modified_energies(F, False)
            == pytest.approx(energies - F * distances))


def test_force_T(cogef1d):
    diss = Dissociation(cogef1d)

    LOADING_RATE = 1  # [nN/s]
    T = 300      # Temperature [K]
    P = 101325.  # Pressure    [Pa]

    fstep = 0.1
    method = 'electronic'
    fmin, fmax = diss.get_force_limits(
        T, P, LOADING_RATE, force_step=fstep, method=method)
    force, error = diss.rupture_force_and_uncertainty(
        T, P, LOADING_RATE, fmax, fmin, fstep, method=method)
    # XXX assert something


def not_test_force_Gibbs_T(cogef1d):
    cogef1d.move(0.2, 5)

    def initialize(image):
        image.calc = MorsePotential()
        return image

    diss = Dissociation(cogef1d, initialize=initialize)

    LOADING_RATE = 10  # [nN/s]
    T = 300      # Temperature [K]
    P = 101325.  # Pressure    [Pa]

    fstep = 0.1
    method = 'Gibbs'
    fmin, fmax = diss.get_force_limits(
        T, P, LOADING_RATE, force_step=fstep, method=method)
    force, error = diss.rupture_force_and_uncertainty(
        T, P, LOADING_RATE, fmax, fmin, fstep, method=method)
    # XXX assert something
