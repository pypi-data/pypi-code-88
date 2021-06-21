"""
MLLint setup module.
"""

from rpgt import templates
from rpgt.src.generators.cicd.cicd_generator import CICDGenerator
from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.setup.setup import Setup
from rpgt.src.utils.file_reader import get_file_contents


class MLLintSetup(Setup):
    """
    MLLint setup class.
    """

    def setup_dependencies(self, env_gen: EnvironmentGenerator) -> None:
        """
        Sets up project dependencies.
        """
        env_gen.add_requirement("mllint", "~=0.9.0", dev_only=True)
        env_gen.add_requirement("isort", "~=5.8.0", dev_only=True)
        env_gen.add_requirement("pylint", "~=2.8.2", dev_only=True)
        env_gen.add_requirement("mypy", "~=0.812", dev_only=True)
        env_gen.add_requirement("black", "==21.5b2", dev_only=True)
        env_gen.add_requirement("bandit", "~=1.7.0", dev_only=True)

    def setup_files(self, struct_gen: StructureGenerator) -> None:
        """
        Sets up project files.
        """
        struct_gen.add_file(
            ".bandit", get_file_contents(templates.configs, "bandit.txt")
        )
        struct_gen.add_file(
            ".mypy.ini", get_file_contents(templates.configs, "mypy.txt")
        )
        struct_gen.add_file(
            "pyproject.toml", get_file_contents(templates.configs, "pyproject.txt")
        )
        struct_gen.add_file(
            ".pylintrc", get_file_contents(templates.configs, "pylintrc.txt")
        )

    def setup_pipeline(self, cicd_gen: CICDGenerator) -> None:
        """
        Sets up project pipeline.
        """
        cicd_gen.add_job(
            "mllint",
            {
                "stage": "analysis",
                "script": ["pipenv run mllint -o mllint-report.md"],
                "artifacts": [{"paths": ["mllint-report.md"], "expire_in": "1 month"}],
            },
        )
