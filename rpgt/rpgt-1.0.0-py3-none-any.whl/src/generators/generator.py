"""
Abstract generator module.
"""

import abc
import argparse


class Generator:
    """
    Abstract generator class.
    """

    def __init__(self, args: argparse.Namespace):
        """
        Abstract initialize function definition.
        """
        self.args = args

    @abc.abstractmethod
    def generate(self, cwd: str) -> None:
        """
        Abstract generate function definition.
        """
        raise NotImplementedError("Unimplemented")
