import unittest
from pymuplot import __version__


class TestInit(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")
