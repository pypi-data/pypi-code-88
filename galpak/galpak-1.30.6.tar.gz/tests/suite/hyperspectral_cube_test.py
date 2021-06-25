# coding=utf-8
from __future__ import division

## GENERAL PACKAGES
import os, sys
import logging
import unittest

import numpy
sys.path.append('../')


## GALPAK PACKAGES -- galpak is served both standalone and as part of mpdaf

from galpak import HyperspectralCube

from tests.tools.numpy_ndarray_assertions import NumpyNdArrayAssertions

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('HyperspectralCubeTest')


class HyperspectralCubeTest(unittest.TestCase, NumpyNdArrayAssertions):

    longMessage = True

    root_folder = os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir
    ))
    fits_folder = os.path.join(root_folder, 'data/input')

    fits_muse_filename = os.path.join(fits_folder, 'cube/subcube_MUSE.fits')
    fits_test_filename = os.path.join(fits_folder, 'cube/subcube_MUSE.fits')

    def test_init_empty_cube(self):
        cube = HyperspectralCube()
        self.assertTrue(cube.is_empty())

    def test_init_with_unfit_filename(self):
        with self.assertRaises(IOError):
            cube = HyperspectralCube.from_file('this_is_not_a_fits_file')

    def test_init_with_all_of_our_input_cube_fits(self):
        for filename in os.listdir(os.path.join(self.fits_folder, 'cube')):
            filepath = os.path.join(self.fits_folder, filename)
            if os.path.isfile(filepath) and filepath.endswith('.fits'):
                # This should not throw (that IS our assertion)
                cube = HyperspectralCube.from_file(filepath, verbose=True)
                log.info(filename)
                log.info("\n"+cube.header.tostring("\n").strip())

    def test_shape_property(self):
        data_a = numpy.array([
            [[0, 1], [2, 3], [-1, +0]],
            [[1, 0], [3, 2], [+3, +2]],
            [[1, 1], [2, 2], [-3, +0]],
        ], dtype=float)
        cube_a = HyperspectralCube(data=data_a)

        self.assertArrayEqual((3, 3, 2), cube_a.shape,
                              "cube.shape should return the shape")

    def test_arithmetic(self):
        inf = numpy.inf
        nan = numpy.nan

        # BRAIN COMPUTED TEST DATA
        data_a = numpy.array([
            [[0, 1], [2, 3], [-1, +0]],
            [[1, 0], [3, 2], [+3, +2]],
            [[1, 1], [2, 2], [-3, +0]],
        ], dtype=float)
        data_b = numpy.array([
            [[1, 1], [0, 0], [+1, -1]],
            [[0, 0], [3, 1], [+3, -2]],
            [[2, 2], [1, 2], [-1, +0]],
        ], dtype=float)
        data_i = numpy.array([
            [[2, 0], [1, 1], [+1, -1]],
        ], dtype=float)
        data_a_plus_1 = numpy.array([
            [[1, 2], [3, 4], [+0, +1]],
            [[2, 1], [4, 3], [+4, +3]],
            [[2, 2], [3, 3], [-2, +1]],
        ], dtype=float)
        data_a_plus_b = numpy.array([
            [[1, 2], [2, 3], [+0, -1]],
            [[1, 0], [6, 3], [+6, -0]],
            [[3, 3], [3, 4], [-4, +0]],
        ], dtype=float)
        data_a_plus_i = numpy.array([
            [[2, 1], [3, 4], [+0, -1]],
            [[3, 0], [4, 3], [+4, +1]],
            [[3, 1], [3, 3], [-2, -1]],
        ], dtype=float)
        data_a_minus_1 = numpy.array([
            [[-1, +0], [1, 2], [-2, -1]],
            [[+0, -1], [2, 1], [+2, +1]],
            [[+0, +0], [1, 1], [-4, -1]],
        ], dtype=float)
        data_1_minus_a = numpy.array([
            [[+1, +0], [-1, -2], [+2, +1]],
            [[+0, +1], [-2, -1], [-2, -1]],
            [[+0, +0], [-1, -1], [+4, +1]],
        ], dtype=float)
        data_a_times_2 = numpy.array([
            [[0, 2], [4, 6], [-2, +0]],
            [[2, 0], [6, 4], [+6, +4]],
            [[2, 2], [4, 4], [-6, +0]],
        ], dtype=float)
        data_a_times_b = numpy.array([
            [[0, 1], [0, 0], [-1, +0]],
            [[0, 0], [9, 2], [+9, -4]],
            [[2, 2], [2, 4], [+3, +0]],
        ], dtype=float)
        data_a_div_2 = numpy.array([
            [[.0, .5], [1.0,  3./2], [-.5,   0]],
            [[.5, .0], [3./2,  1.0], [3./2,  1]],
            [[.5, .5], [1.0,   1.0], [-3./2, 0]],
        ], dtype=float)
        data_a_div_b = numpy.array([
            [[0,     1], [inf, inf], [-1,  -0.]],
            [[inf, nan], [1,     2], [+1,  -1.]],
            [[.5,   .5], [2,     1], [+3,  nan]],
        ], dtype=float)
        data_a_pow_2 = numpy.array([
            [[0, 1], [4, 9], [+1, +0]],
            [[1, 0], [9, 4], [+9, +4]],
            [[1, 1], [4, 4], [+9, +0]],
        ], dtype=float)
        data_2_pow_a = numpy.array([
            [[1, 2], [4, 8], [0.5,  1]],
            [[2, 1], [8, 4], [8,    4]],
            [[2, 2], [4, 4], [1./8, 1]],
        ], dtype=float)
        data_b_pow_a = numpy.array([
            [[1, 1], [0,  0], [+1, +1]],
            [[0, 1], [27, 1], [27, +4]],
            [[2, 2], [1,  4], [-1, +1]],
        ], dtype=float)

        self.assertArrayEqual(data_a_div_b, data_a_div_b,
                              "Sanity check with inf and nan")

        cube_a = HyperspectralCube(data=data_a)
        cube_b = HyperspectralCube(data=data_b)
        cube_i = HyperspectralCube(data=data_i)  # image
        cube_e = HyperspectralCube()             # empty

        # CUBE + NUMBER
        cube_a_plus_1 = cube_a + 1.
        self.assertIsInstance(cube_a_plus_1, HyperspectralCube,
                              "Addition result is a HyperspectralCube")
        self.assertArrayEqual(data_a_plus_1, cube_a_plus_1.data,
                              "Supports addition of cube and number using +")

        # NUMBER + CUBE
        cube_a_plus_1 = 1. + cube_a
        self.assertIsInstance(cube_a_plus_1, HyperspectralCube,
                              "Addition result is a HyperspectralCube")
        self.assertArrayEqual(data_a_plus_1, cube_a_plus_1.data,
                              "Supports addition of number and cube using +")

        # CUBE A + CUBE B
        cube_a_plus_b = cube_a + cube_b
        self.assertIsInstance(cube_a_plus_b, HyperspectralCube,
                              "Addition result is a HyperspectralCube")
        self.assertArrayEqual(data_a_plus_b, cube_a_plus_b.data,
                              "Supports addition of two cubes using +")

        # CUBE A + NDARRAY
        cube_a_plus_b = cube_a + data_b
        self.assertIsInstance(cube_a_plus_b, HyperspectralCube,
                              "Addition result is a HyperspectralCube")
        self.assertArrayEqual(data_a_plus_b, cube_a_plus_b.data,
                              "Supports addition of cube and ndarray using +")

        # CUBE + IMAGE
        cube_a_plus_i = cube_a + cube_i
        self.assertIsInstance(cube_a_plus_i, HyperspectralCube,
                              "Addition result is a HyperspectralCube")
        self.assertArrayEqual(data_a_plus_i, cube_a_plus_i.data,
                              "Supports addition of cube and image using +")

        # IMAGE + CUBE
        cube_a_plus_i = cube_i + cube_a
        self.assertIsInstance(cube_a_plus_i, HyperspectralCube,
                              "Addition result is a HyperspectralCube")
        self.assertArrayEqual(data_a_plus_i, cube_a_plus_i.data,
                              "Supports addition of image and cube using +")

        # ADDITION EXPECTED ERRORS
        with self.assertRaises(TypeError):
            cube_a + cube_e  # right-hand empty cube
        with self.assertRaises(TypeError):
            cube_e + cube_b  # left-hand empty cube
        with self.assertRaises(TypeError):
            cube_b + 'rock'  # left-hand "garbage"
        with self.assertRaises(TypeError):
            '666.' + cube_a  # right-hand "garbage"

        # CUBE - NUMBER
        cube_a_minus_1 = cube_a - 1
        self.assertIsInstance(cube_a_minus_1, HyperspectralCube,
                              "Subtraction result is a HyperspectralCube")
        self.assertArrayEqual(data_a_minus_1, cube_a_minus_1.data,
                              "Supports subtraction of number from cube using -")

        # NUMBER - CUBE
        cube_1_minus_a = 1 - cube_a
        self.assertIsInstance(cube_1_minus_a, HyperspectralCube,
                              "Subtraction result is a HyperspectralCube")
        self.assertArrayEqual(data_1_minus_a, cube_1_minus_a.data,
                              "Supports subtraction of cube from number using -")

        # CUBE * NUMBER
        cube_a_times_2 = cube_a * 2
        self.assertIsInstance(cube_a_times_2, HyperspectralCube,
                              "Multiplication result is a HyperspectralCube")
        self.assertArrayEqual(data_a_times_2, cube_a_times_2.data,
                              "Supports multiplication of cube and number using *")

        # NUMBER * CUBE
        cube_a_times_2 = 2 * cube_a
        self.assertIsInstance(cube_a_times_2, HyperspectralCube,
                              "Multiplication result is a HyperspectralCube")
        self.assertArrayEqual(data_a_times_2, cube_a_times_2.data,
                              "Supports multiplication of number and cube using *")

        # CUBE A * CUBE B
        cube_a_times_b = cube_a * cube_b
        self.assertIsInstance(cube_a_times_b, HyperspectralCube,
                              "Multiplication result is a HyperspectralCube")
        self.assertArrayEqual(data_a_times_b, cube_a_times_b.data,
                              "Supports multiplication of two cubes using *")

        # CUBE / NUMBER
        cube_a_div_2 = cube_a / 2.
        self.assertIsInstance(cube_a_div_2, HyperspectralCube,
                              "Division result is a HyperspectralCube")
        self.assertArrayEqual(data_a_div_2, cube_a_div_2.data,
                              "Supports division of cube and number using /")

        # CUBE / CUBE
        cube_a_div_b = cube_a / cube_b
        self.assertIsInstance(cube_a_div_b, HyperspectralCube,
                              "Division result is a HyperspectralCube")
        self.assertArrayEqual(data_a_div_b, cube_a_div_b.data,
                              "Supports division of two cubes using /")

        # CUBE ** NUMBER
        cube_a_pow_2 = cube_a ** 2
        self.assertIsInstance(cube_a_pow_2, HyperspectralCube,
                              "Exponentiation result is a HyperspectralCube")
        self.assertArrayEqual(data_a_pow_2, cube_a_pow_2.data,
                              "Supports exponentiation of cube by number using **")

        # NUMBER ** CUBE
        cube_2_pow_a = 2 ** cube_a
        self.assertIsInstance(cube_2_pow_a, HyperspectralCube,
                              "Exponentiation result is a HyperspectralCube")
        self.assertArrayEqual(data_2_pow_a, cube_2_pow_a.data,
                              "Supports exponentiation of number by cube using **")

        # CUBE A ** CUBE B
        cube_b_pow_a = cube_b ** cube_a
        self.assertIsInstance(cube_b_pow_a, HyperspectralCube,
                              "Exponentiation result is a HyperspectralCube")
        self.assertArrayEqual(data_b_pow_a, cube_b_pow_a.data,
                              "Supports exponentiation of cube by cube using **")

    def test_slicing_and_indexing(self):
        data_a = numpy.array([
            [[0, 1], [2, 3], [-1, 0]],
            [[1, 0], [3, 2], [+3, 2]],
            [[1, 1], [2, 2], [-3, 0]],
        ], dtype=float)

        cube_a = HyperspectralCube(data=data_a)

        # SLICING USING [:,:,:]
        cube_t = cube_a[0:1, :, :-1]
        data_t = numpy.array([[[0.], [2.], [-1.]]], dtype=float)
        self.assertIsInstance(cube_t, HyperspectralCube,
                              "Truncation result is a HyperspectralCube")
        self.assertArrayEqual(data_t, cube_t.data,
                              "Supports extraction of sub-cube using [:,:,:]")

        # SLICING [min:max] <=> [min:max,:,:]
        cube_t = cube_a[0:1]
        data_t = numpy.array([[[0, 1], [2, 3], [-1, 0]]], dtype=float)
        self.assertArrayEqual(data_t, cube_t.data,
                              "Unspecified axes are defaulted to `:` in slicing")

        # TODO : SLICING UPDATES HEADERS
        # Needs to create test cubes

        # MUTATING ONE VALUE USING [λ,y,x] INDICES
        data_t = numpy.array([
            [[0, 1], [2, 3], [-1, 0]],
            [[1, 0], [3, 9], [+3, 2]],
            [[1, 1], [2, 2], [-3, 0]],
        ], dtype=float)
        cube_t = cube_a.copy()
        cube_t[1, 1, 1] = 9
        self.assertArrayEqual(data_t, cube_t.data,
                              "Supports mutation cube[λ,y,x] = n")

        # MUTATING MULTIPLE VALUES USING [:,y,x] INDICES
        data_t = numpy.array([
            [[0, 1], [2, 9], [-1, 0]],
            [[1, 0], [3, 9], [+3, 2]],
            [[1, 1], [2, 9], [-3, 0]],
        ], dtype=float)
        cube_t = cube_a.copy()
        cube_t[:, 1, 1] = 9
        self.assertArrayEqual(data_t, cube_t.data,
                              "Supports mutation cube[:,y,x] = n")

    #def test_getting_steps(self):
        #cube = HyperspectralCube.from_file(self.fits_test_filename)

        # We merely test the success/failure of the API
        #self.assertArrayEqual(cube.get_steps(), [cube.get_step(0), cube.get_step(1), cube.get_step(2)],
        #                      "cube.get_step(axis) == cube.get_steps()[axis]")

        # Value-checking should be done by the test_compatibility routine
        # self.assertEqual(cube.get_step(0), 0.000194999995074)  # this is a poor test

    def test_wavelength_conversion(self):
        cube = HyperspectralCube.from_file(self.fits_test_filename)
        pixel_index = 3
        self.assertEqual(round(cube.pixel_from_lambda(cube.wavelength_of(pixel_index))), pixel_index,
                         "Wavelength conversion from pixel index to λ and from λ to pixel index")

    def test_write_to_file(self):
        cube = HyperspectralCube.from_file(self.fits_test_filename)
        fits_out_filename = os.path.join(self.fits_folder, 'tmp_output.fits')

        self.assertFalse(os.path.isfile(fits_out_filename),
                         "Sanity check : Output FITS file should not exist ; "
                         "Please remove it by hand and then re-run this test : %s" % fits_out_filename)
        cube.write_to(fits_out_filename)
        self.assertTrue(os.path.isfile(fits_out_filename),
                        "Output FITS file should be created")

        with self.assertRaises(IOError):
            cube.write_to(fits_out_filename)  # clobber option should be false by default

        cube.write_to(fits_out_filename, overwrite=True)  # overwrites without raising
        os.remove(fits_out_filename)  # cleanup
