import unittest

from Alexandria.general import console
from Alexandria.general import logic
from Alexandria.general import project
from Alexandria.general import runtime


class Tests(unittest.TestCase):

    def test_console(self):
        console.print_color("Color", "blue")
        console.units(35, "V", 5)
        console.result("A", 2, "Kg", 3)
        console.print_numbered_list(["a", "b", "c"], 5)

    def test_logic(self):
        assert logic.if_none("a", "b") == "a"
        assert logic.if_none(None, "b") == "b"

    def test_project(self):
        print(project.root())

    def test_runtime(self):
        pass

