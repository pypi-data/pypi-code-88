"""
Github CI generator module.
"""

from typing import Any

from rpgt.src.generators.cicd.cicd_generator import CICDGenerator


class GithubCICDGenerator(CICDGenerator):
    """
    Gitlab CI generator class.
    """

    def add_job(self, job: str, data: Any) -> None:
        """
        Add job to CI
        """

    def generate(self, cwd: str) -> None:
        """
        Generate CI
        """

    def generate_job(self, job: str, data: Any) -> str:
        """
        Generate job
        """
