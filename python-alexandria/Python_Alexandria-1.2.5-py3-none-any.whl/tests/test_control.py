import unittest

from Alexandria.control import signals


s1 = signals.ControlSignals(10, 1)
s2 = signals.ControlSignals(10, 0.01)


class Tests(unittest.TestCase):

    def test_t(self):
        assert s1.t().size == 10

    def test_seconds_to_n(self):
        assert s1.seconds_to_n(0, 2) == 2
        assert s2.seconds_to_n(0, 2) == 200

    def test_u_step(self):
        assert s1.u_step(5, 0, 10).mean() == 5

    def test_u_ramp(self):
        assert s1.u_ramp(0, 5, 0, 10).mean() == 2.5
