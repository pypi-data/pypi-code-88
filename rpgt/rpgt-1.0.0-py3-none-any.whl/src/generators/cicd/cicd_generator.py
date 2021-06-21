"""
Abstract CICD generator module.
"""

import abc
import argparse
from typing import Any, Dict, List

from rpgt.src.generators.generator import Generator


class CICDGenerator(Generator):
    """
    Abstract CICD generator class.
    """

    def __init__(self, args: argparse.Namespace):
        """
        Initialize CICD generator with proper parameters.
        """

        super().__init__(args)
        self.stages: List[str] = []
        self.jobs: Dict[str, Any] = dict()

    @abc.abstractmethod
    def add_job(self, job: str, data: Any) -> None:
        """
        Add job to CI
        """
        raise NotImplementedError("Unimplemented")

    @abc.abstractmethod
    def generate_job(self, job: str, data: Any) -> str:
        """
        Generate job
        """
        raise NotImplementedError("Unimplemented")
