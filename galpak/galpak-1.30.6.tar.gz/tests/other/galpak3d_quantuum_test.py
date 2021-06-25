# coding=utf-8

## GENERAL PACKAGES
import os
import unittest

import numpy as np

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('GalPaK Q-test')

from astropy.io import fits

import galpak
from galpak import GalPaK3D
from galpak import GalaxyParameters
from galpak import MUSEWFM
from galpak import HyperspectralCube as Cube

root_folder = os.path.dirname(os.path.abspath(galpak.__file__))
fits_folder = os.path.join(root_folder, '../../data/input/ref')

from tests.tools.numpy_ndarray_assertions import NumpyNdArrayAssertions


class GalPaK3DQuantuumTest(unittest.TestCase, NumpyNdArrayAssertions):
    """
    These are miscellaneous tests that may or may not pass. (hence the name)
    They're kept because they are useful, but they're not part of the testing suite.
    You are NOT supposed to run them, but you may, at your expense and risk.
    WARNING : some of these tests take a very long time (they run many deconvolutions) !
    """

    longMessage = True

    fits_muse_filename = os.path.join(fits_folder, 'GalPaK_cube_1101_from_v191_noised.fits')

    def assertArrayEqualishNico(self, expected, actual, expected_similarity=99.):
        """
        expected_similarity (in %)
        """
        # Avoid rounding errors and infinity errors
        good = lambda x: np.where(np.abs(x) > 1e-32, np.float32(x), 1e-32)
        expected_good = good(expected)
        actual_good = good(actual)
        differences = np.abs((expected_good - actual_good) / actual_good)
        #differences = good(differences)
        differences_not_nan = differences[~np.isnan(differences)]
        actual_precision = 100. * (1 - np.mean(differences_not_nan))
        self.assertTrue(actual_precision >= expected_similarity, "Expected %f%%, got %f%%" % (expected_similarity, actual_precision))
        return actual_precision


    def test_psf3d(self):
        expected_similarity = 99.999  # in %

        psf_cube_file = os.path.join(fits_folder, 'psf3d_current_pair_Seeing08.fits')
        psf_expected = fits.open(psf_cube_file)[0].data

        instr = MUSEWFM(psf_fwhm=0.8)

        glpk3d = GalPaK3D(Cube(data=np.ones((20,30,30))), instrument=instr)

        image = instr.psf.as_image(glpk3d.cube)
        lsf1d = instr.lsf.as_vector(glpk3d.cube)
        #self.psf.as_image(cube), self.lsf.as_vector(cube), cube
        psf3d_galpak = instr.extrude_psf(image, lsf1d)

        print("PSF3D precision =", self.assertArrayEqualish(psf_expected, psf3d_galpak, expected_similarity))

    def test_galfitness(self):
        """
        Compare GalPaK3D results with galfit results
        This is a debugging test
        """
        expected_similarity = 98.  # in %
        clean_cube_file = os.path.join(fits_folder, 'cubeclean_current_pair-2.fits')
        conv_cube_file = os.path.join(fits_folder, 'cubetest_current_pair_Seeing0.8.fits')

        # P=[15,15,11,3,55,45,1,250,100,0]
        params = GalaxyParameters.from_ndarray([15, 15, 11, 100, 3 * 1.6721, 55, 45, 1, 250, 0])

        glpk3d = GalPaK3D(Cube(data=np.ones((20,30,30))), instrument=MUSEWFM(psf_fwhm=0.8))
        glpk3d.model = galpak.DiskModel()

        cube_clean = glpk3d.create_clean_cube(params, (20, 30, 30))
        cube_clean_expected = fits.open(clean_cube_file)[0]

        print("Clean precision =", self.assertArrayEqualishNico(cube_clean_expected.data, cube_clean.data, expected_similarity))

        cube_conv_expected = fits.open(conv_cube_file)[0]
        cube_conv = glpk3d.create_convolved_cube(params, (20, 30, 30))

        print("Conv precision =", self.assertArrayEqualish(cube_conv_expected.data, cube_conv.data, expected_similarity))
        #print "Conv precision =", self.assertArrayEqualishNico(cube_conv_expected.data, cube_conv.data, expected_similarity)





