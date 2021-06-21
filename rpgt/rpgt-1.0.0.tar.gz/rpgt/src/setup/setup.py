"""
Abstract setup module
"""

import abc
import argparse

from rpgt.src.generators.cicd.cicd_generator import CICDGenerator
from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.structure_generator import StructureGenerator


class Setup:
    """
    Abstract setup class.
    """

    def __init__(self, args: argparse.Namespace, cwd: str) -> None:
        """
        Initializes setup class with proper parameters.
        """
        self.args = args
        self.cwd = cwd

    @abc.abstractmethod
    def setup_dependencies(self, env_gen: EnvironmentGenerator) -> None:
        """
        Sets up project dependencies.
        """
        raise NotImplementedError("Unimplemented")

    @abc.abstractmethod
    def setup_files(self, struct_gen: StructureGenerator) -> None:
        """
        Sets up project files.
        """
        raise NotImplementedError("Unimplemented")

    @abc.abstractmethod
    def setup_pipeline(self, cicd_gen: CICDGenerator) -> None:
        """
        Sets up project pipeline.
        """
        raise NotImplementedError("Unimplemented")
