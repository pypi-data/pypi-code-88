import unittest
import warnings


class TestImport(unittest.TestCase):
    def test_phasor(self):
        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            from appteka.pyqt.testing import TestApp
