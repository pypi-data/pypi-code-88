import unittest

from tap_file.dipole import Dipole


class TestDipole(unittest.TestCase):

    def test_invalid(self):
        d = Dipole()
        self.assertEqual(d.classify(5), 'X')
        self.assertEqual(d.classify(2000), 'X')

    def test_short(self):
        d = Dipole()
        self.assertEqual(d.classify(48*8), 'S')
        self.assertEqual(d.classify(56*8), 'S')

    def test_medium(self):
        d = Dipole()
        self.assertEqual(d.classify(66*8), 'M')
        self.assertEqual(d.classify(75*8), 'M')
        d = Dipole()
        for _ in range(0, 25):
            d.classify(38*8)
        self.assertEqual(d.classify(56*8), 'M')
        d = Dipole()
        for _ in range(0, 25):
            d.classify(56*8)
        self.assertEqual(d.classify(70*8), 'M')

    def test_long(self):
        d = Dipole()
        self.assertEqual(d.classify(86*8), 'L')
        self.assertEqual(d.classify(95*8), 'L')
