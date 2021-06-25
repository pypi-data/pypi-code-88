import sys
import unittest
sys.path.append('../')

import numpy as np
from galpak import merge_where_nan, safe_exp

from tests.tools.numpy_ndarray_assertions import NumpyNdArrayAssertions


class MathUtilsTest(unittest.TestCase, NumpyNdArrayAssertions):

    longMessage = True

    def test_merge_where_nan(self):
        target = np.array([float('NaN'), 1.0])
        filler = np.array([2.0, 3.0])
        expected = np.array([2.0, 1.0])

        merge_where_nan(target, filler)

        self.assertArrayEqual(target, expected)

    def test_safe_exp(self):

        a = safe_exp(-1e100000000000000000)
        self.assertEqual(a, 0)

        a = safe_exp(-3950.)
        self.assertEqual(a, 0)

        a = safe_exp(1e1000000000000000000)
        self.assertEqual(a, float('inf'))

        a = safe_exp(3950.)
        self.assertEqual(a, float('inf'))


