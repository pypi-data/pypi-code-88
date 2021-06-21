import unittest
from pyopencell import helpers


class HelpersTest(unittest.TestCase):
    def test_getenv_fails_if_not_defined_envvar(self):
        with self.assertRaises(Exception):
            helpers.getenv_or_fail('Fooo')
