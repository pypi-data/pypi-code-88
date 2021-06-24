import unittest
from appteka.config import Config


class TestConfig(unittest.TestCase):
    def test_touch(self):
        Config("desired", "resource", "appteka")
