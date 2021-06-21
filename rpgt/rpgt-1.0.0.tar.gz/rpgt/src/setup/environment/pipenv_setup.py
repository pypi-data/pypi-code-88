"""
PipEnv setup module.
"""

from rpgt.src.generators.cicd.cicd_generator import CICDGenerator
from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.environment.pipenv_generator import PipEnvGenerator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.setup.environment.environment_setup import EnvironmentSetup


class PipEnvSetup(EnvironmentSetup):
    """
    PipEnv setup class.
    """

    def get_standard_env(self) -> PipEnvGenerator:
        """
        Gets standard environment.
        :return: the standard environment.
        """
        return PipEnvGenerator(self.args)

    def setup_pipeline(self, cicd_gen: CICDGenerator) -> None:
        """
        Sets up project pipeline.
        """
        cicd_gen.add_job(
            "install",
            {
                "stage": "install",
                "script": ["pipenv install --dev"],
            },
        )

    def setup_files(self, struct_gen: StructureGenerator) -> None:
        """
        Sets up project files.
        """

    def setup_dependencies(self, env_gen: EnvironmentGenerator) -> None:
        """
        Sets up project dependencies.
        """
