"""
Structure generator module.
"""

import argparse
import os
from typing import List, Tuple

from rpgt.src.generators.generator import Generator


class StructureGenerator(Generator):
    """
    Structure generator class.
    """

    def __init__(self, args: argparse.Namespace):
        """
        Initializes the structure generator.
        """
        super().__init__(args)
        self.files: List[Tuple[str, str]] = []
        self.folders: List[Tuple[str, bool]] = []

    def add_folder(self, path: str, is_module: bool = True) -> None:
        """
        Adds a folder at specified path.
        """
        self.folders.append((path, is_module))

    def add_file(self, path: str, content: str) -> None:
        """
        Adds a file at specified path.
        """
        content = content.replace("[=NAME=]", self.args.name)
        self.files.append((path, content))

    def add_src_file(self, path: str, content: str) -> None:
        """
        Adds a source file at specified path.
        """
        content = content.replace("[=NAME=]", self.args.name)
        self.add_file(f"src/{self.args.name}/{path}", content)

    def add_unit_test_file(self, path: str, content: str) -> None:
        """
        Adds a unit test file at specified path.
        """
        content = content.replace("[=NAME=]", self.args.name)
        self.add_file(f"tests/unit_tests/{self.args.name}/{path}", content)

    def generate(self, cwd: str) -> None:
        """
        Writes the structure to files.
        """
        for path, is_module in self.folders:
            os.mkdir(f"{path}")
            if is_module:
                with open(f"{cwd}/{path}/__init__.py", "w"):
                    pass

        for path, content in self.files:
            with open(f"{cwd}/{path}", "w") as file:
                file.write(content)
