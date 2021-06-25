
import os

from base import TestBase

class DictsTest(TestBase):
    snippet_dir = "dicts"

    def test_return_direct(self):
        self.validate_snippet(self.get_snippet_path("return_direct"))

    def test_type_coercion(self):
        self.validate_snippet(self.get_snippet_path("type_coercion"))

    def test_update(self):
        self.validate_snippet(self.get_snippet_path("update"))

    def test_ext_key(self):
        self.validate_snippet(self.get_snippet_path("ext_key"))

    def test_mutable_param(self):
        self.validate_snippet(self.get_snippet_path("mutable_param"))

    def test_return(self):
        self.validate_snippet(self.get_snippet_path("return"))

    def test_simple(self):
        self.validate_snippet(self.get_snippet_path("simple"))

    def test_nested(self):
        self.validate_snippet(self.get_snippet_path("nested"))

    def test_add_key(self):
        self.validate_snippet(self.get_snippet_path("add_key"))
