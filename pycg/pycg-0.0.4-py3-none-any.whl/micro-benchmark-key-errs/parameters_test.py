
import os

from base import TestBase

class ParametersTest(TestBase):
    snippet_dir = "parameters"

    def test_assigned_call(self):
        self.validate_snippet(self.get_snippet_path("assigned_call"))

    def test_imported_assigned_call(self):
        self.validate_snippet(self.get_snippet_path("imported_assigned_call"))

    def test_call(self):
        self.validate_snippet(self.get_snippet_path("call"))
