
import os

from base import TestBase

class ListsTest(TestBase):
    snippet_dir = "lists"

    def test_comprehension(self):
        self.validate_snippet(self.get_snippet_path("comprehension"))

    def test_list_str(self):
        self.validate_snippet(self.get_snippet_path("list_str"))
