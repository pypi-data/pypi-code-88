"""
Docker file generator module.
"""
import argparse

from rpgt import templates
from rpgt.src.generators.generator import Generator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.utils.file_reader import get_file_contents


class DockerfileGenerator(Generator):
    """
    Docker file generator class.
    """

    def __init__(self, args: argparse.Namespace, struct_gen: StructureGenerator):
        """
        Initialize Changelog generator with proper parameters.
        """

        super().__init__(args)
        self.struct_gen = struct_gen

    def generate(self, cwd: str) -> None:
        """
        Generates the docker file.
        :return: a docker configuration file
        """
        self.struct_gen.add_file(
            "Dockerfile", get_file_contents(templates.docker, "Dockerfile.txt")
        )
        self.struct_gen.add_file(
            ".dockerignore", get_file_contents(templates.gitignore, "gitignore.txt")
        )
