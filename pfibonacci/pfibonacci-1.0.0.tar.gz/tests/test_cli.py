import os
import unittest
import fibonacci


class CLITestCase(unittest.TestCase):

    def test_cli_success(self):
        assert os.system('fibonacci 5') == 0

    def test_cli_failure(self):
        assert os.system('fibonacci -1') != 0
