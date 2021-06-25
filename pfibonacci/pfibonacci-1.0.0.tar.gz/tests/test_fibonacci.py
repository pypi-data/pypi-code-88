import unittest
import fibonacci


class FibonacciTestCase(unittest.TestCase):

    def test_compute_0(self):
        assert fibonacci.compute(0) == 0

    def test_compute_1(self):
        assert fibonacci.compute(1) == 1

    def test_compute_2(self):
        assert fibonacci.compute(2) == 1

    def test_compute_5(self):
        assert fibonacci.compute(5) == 5

    def test_compute_6(self):
        assert fibonacci.compute(6) == 8
