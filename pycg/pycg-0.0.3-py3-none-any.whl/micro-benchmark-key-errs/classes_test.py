
import os

from base import TestBase

class ClassesTest(TestBase):
    snippet_dir = "classes"

    def test_base_class_const(self):
        self.validate_snippet(self.get_snippet_path("base_class_const"))

    def test_return_str(self):
        self.validate_snippet(self.get_snippet_path("return_str"))

    def test_assigned_str(self):
        self.validate_snippet(self.get_snippet_path("assigned_str"))

    def test_self_const(self):
        self.validate_snippet(self.get_snippet_path("self_const"))

    def test_self_dict(self):
        self.validate_snippet(self.get_snippet_path("self_dict"))

    def test_self_assignment(self):
        self.validate_snippet(self.get_snippet_path("self_assignment"))
