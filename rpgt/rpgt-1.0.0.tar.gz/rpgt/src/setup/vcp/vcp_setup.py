"""
Abstract VCP setup module.
"""
import abc

from rpgt.src.generators.cicd.cicd_generator import CICDGenerator
from rpgt.src.setup.setup import Setup


class VCPSetup(Setup):
    """
    Abstract VCP setup class.
    """

    @abc.abstractmethod
    def get_standard_pipeline(self) -> CICDGenerator:
        """
        Sets up project pipeline definition.
        """
        raise NotImplementedError("Unimplemented")
