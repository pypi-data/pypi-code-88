"""
Abstract env generator module.
"""

import abc
import argparse
from typing import Any, Dict

from rpgt.src.generators.generator import Generator


class EnvironmentGenerator(Generator):
    """
    Abstract env generator class.
    """

    def __init__(self, args: argparse.Namespace):
        """
        Initialize env generator with proper parameters.
        """
        super().__init__(args)
        self.requirements: Dict[str, Any] = dict()

    @abc.abstractmethod
    def add_requirement(
        self, requirement: str, version: str, dev_only: bool = False
    ) -> None:
        """
        Add requirement to env.
        """
        raise NotImplementedError("Unimplemented")
