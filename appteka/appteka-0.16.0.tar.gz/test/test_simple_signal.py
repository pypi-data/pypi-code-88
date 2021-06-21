import unittest
from appteka.simple_signal import SimpleSignal


class TestSimpleSignal_Touch(unittest.TestCase):
    def test_signal_with_args(self):
        def func(a):
            a.append(1)

        a = []
        signal = SimpleSignal()
        signal.connect(func)
        signal.emit(a)
        self.assertEqual(len(a), 1)
