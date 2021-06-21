"""
Abstract environment setup module.
"""
import abc

from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.setup.setup import Setup


class EnvironmentSetup(Setup):
    """
    Abstract environment setup class.
    """

    @abc.abstractmethod
    def get_standard_env(self) -> EnvironmentGenerator:
        """
        Gets standard environment.
        :return: the standard environment.
        """
        raise NotImplementedError("Unimplemented")
