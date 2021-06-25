import unittest
import numpy as np

from Alexandria.signals.standard import square, triangular


class Tests(unittest.TestCase):

    def test_square(self):
        from mpl_plotter.presets.publication import two_d

        t = np.linspace(0, 4, 1000)
        s = square((t-2)/2, t)

        two_d.line(t, s, show=True)

    def test_triangular(self):
        from mpl_plotter.presets.publication import two_d

        t = np.linspace(0, 4, 1000)
        s_c = 2*triangular((t-2)/2, t)

        two_d.line(t, s_c, show=True)
