import unittest

from Alexandria.file import file_management


class Tests(unittest.TestCase):

    def test_file_management(self):
        print(file_management.find_file("txt", "resources"))

    def test_file_methods(self):
        pass

    def test_parsers(self):
        pass
