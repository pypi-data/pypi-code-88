import unittest
import numpy as np
from numpy import ndarray
import os, sys
sys.path.append('../')

import galpak
from tests.tools.numeric_assertions import NumericAssertions

GalaxyParameters = galpak.DefaultModel().parameters_class()

class GalaxyParametersTest(unittest.TestCase, NumericAssertions):

    longMessage = True

    def test_init_from_array(self):
        g = GalaxyParameters()
        g.from_ndarray(np.arange(len(g)))
        self.assertIsInstance(g, GalaxyParameters)

    def test_init_without_data(self):
        g = GalaxyParameters()
        self.assertIsNan(g.x)

    def test_init_with_data(self):
        g = GalaxyParameters(y=2.0)
        self.assertIsNan(g.x)
        self.assertEqual(g.y, 2.0)

    def test_init_from_ndarray(self):
        a = ndarray(shape=10, dtype=float)
        a[1] = 2.0
        g = GalaxyParameters()
        t = g.from_ndarray(a)
        # self.assertIsNan(g.x)
        # => instead yields 1.88532209e-316 or equalish infinitesimal value
        self.assertEqual(t.y, 2.0)

    def test_init_readwrite_file(self):

        a = ndarray(shape=10, dtype=float)
        a[1] = 2.0
        g = GalaxyParameters()
        g.from_ndarray(a)
        g.save_to_file('test_param.txt', overwrite=True)
        self.assertTrue(os.path.isfile('test_param.txt'))
        empty = GalaxyParameters()
        empty.from_file('test_param.txt')
        test=np.allclose(g,empty,equal_nan=True)
        self.assertTrue(test)
        os.system('rm -f test_param.txt')


    def test_accessors_and_mutators(self):

        # Explicit instantiation
        g1 = GalaxyParameters(0., 1., 2., 3., 4., 5., 6., 7., 8., 9.)

        # Testing accessors after instantiation
        self.assertEqual(0., g1[0])
        self.assertEqual(0., g1.x)
        self.assertEqual(0., g1['x'])
        self.assertEqual(1., g1[1])
        self.assertEqual(1., g1.y)

        # Mutating using numeric keys
        g1[0] = 11.
        self.assertEqual(11., g1[0], "Mutating a key-based value should change the key-based value")
        self.assertEqual(11., g1.x,  "Mutating a key-based value should change the attribute")

        # Mutating using attribute
        g1.x = 13.
        self.assertEqual(13., g1.x,  "Mutating an attribute should change the attribute")
        self.assertEqual(13., g1[0], "Mutating an attribute should change the key-based value")

        # Mutating using dict
        g1['x'] = 1.618
        self.assertEqual(1.618, g1.x,  "Mutating through dict should change the attribute")
        self.assertEqual(1.618, g1[0], "Mutating through dict should change the key-based value")
        self.assertEqual(1.618, g1['x'], "Mutating through dict should change the dict-based value")

        # Using another instance
        g2 = GalaxyParameters(9., 8., 7., 6., 5., 4., 3., 2., 1., 0.)

        # Sanity checks
        self.assertEqual(9., g1[9])
        self.assertEqual(0., g2[9])

    def test_copy(self):

        g1 = GalaxyParameters(0., 1., 2., 3., 4., 5., 6., 7., 8., 9.)
        g2 = g1.copy()

        self.assertEqual(g1[0], g2[0], "Copy should copy key-based values")
        self.assertEqual(g1.x, g2.x,   "Copy should copy attributes too")

    def test_to_string(self):

        # No assertions, just print the galaxy so we can see
        g = GalaxyParameters(0., 1., 2., 3., 4., 5., 6., 7., 8., 9.)
        w = GalaxyParameters(x=0., z=1.)  # warnings flags
        e = GalaxyParameters(z=0.02)  # stdev margin

        print("Using print()")
        print(g)
        print("Using repr()")
        print(repr(g))
        print("Long info")
        print(g.long_info())
        print("Structured info")
        print(g.structured_info())
        print("Colored info")
        print(g.colored_info(w))

        g.error = e
        print("Detailed info w/ stdev")
        print(g.long_info())
        print("Detailed info w/ % stdev")
        print(g.long_info(True))
