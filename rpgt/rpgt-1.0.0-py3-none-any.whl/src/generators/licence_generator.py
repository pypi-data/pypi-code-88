"""
License generator module.
"""

import argparse

from rpgt import templates
from rpgt.src.generators.generator import Generator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.utils.file_reader import get_file_contents


class LicenseGenerator(Generator):
    """
    License generator class.
    """

    def __init__(self, args: argparse.Namespace, struct_gen: StructureGenerator):
        """
        Initializes the license generator.
        """
        super().__init__(args)
        self.struct_gen = struct_gen

        self.license_templates = [
            "agpl30",
            "apache20",
            "gpl30",
            "mit",
            "mpl20",
            "unlicense",
        ]

    def generate(self, cwd: str) -> None:
        """
        Writes the LICENSE.md to file.
        """
        #   | AGPL30       | agpl30            |
        #   | APACHE20     | apache20          |
        #   | GPL30        | gpl30             |
        #   | LGPL30       | lgpl30            |
        #   | MIT          | mit               |
        #   | MPL20        | mpl20             |
        #   | UNLICENSE    | unlicense         |

        license_type = self.args.license.lower()
        if license_type not in self.license_templates:
            raise Exception(f"License {license_type} is not supported")

        self.struct_gen.add_file(
            "LICENSE.md", get_file_contents(templates.licenses, f"{license_type}.txt")
        )
