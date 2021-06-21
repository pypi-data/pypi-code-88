"""
Changelog generator module.
"""
import argparse
import datetime

from rpgt.src.generators.generator import Generator
from rpgt.src.generators.structure_generator import StructureGenerator


class ChangelogGenerator(Generator):
    """
    Changelog generator class.
    """

    def __init__(self, args: argparse.Namespace, struct_gen: StructureGenerator):
        """
        Initialize Changelog generator with proper parameters.
        """

        super().__init__(args)
        self.struct_gen = struct_gen

    def generate(self, cwd: str) -> None:
        """
        Writes the CHANGELOG.md to file.
        """
        self.struct_gen.add_file("CHANGELOG.md", self.generate_changelog())

    @staticmethod
    def generate_changelog() -> str:
        """
        Generates the CHANGELOG.md file.
        :return: a stringual representation of the changelog file.
        """
        return f"""# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 1.0.0 - {datetime.datetime.now().strftime('%Y-%m-%d')}
### Added
- Initial project setup.

### Changed
- None

### Fixed
- None
"""
