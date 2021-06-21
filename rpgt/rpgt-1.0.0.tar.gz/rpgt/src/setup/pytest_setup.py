"""
 Pytest setup module.
 """

from rpgt import templates
from rpgt.src.generators.cicd.cicd_generator import CICDGenerator
from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.setup.setup import Setup
from rpgt.src.utils.file_reader import get_file_contents


class PytestSetup(Setup):
    """
    Pytest setup class.
    """

    def setup_dependencies(self, env_gen: EnvironmentGenerator) -> None:
        """
        Sets up project dependencies.
        """
        env_gen.add_requirement("pytest", "~=6.2.4", dev_only=True)
        env_gen.add_requirement("pytest-html", "~=3.1.1", dev_only=True)

    def setup_files(self, struct_gen: StructureGenerator) -> None:
        """
        Sets up project files.
        """
        struct_gen.add_folder("tests", True)
        struct_gen.add_folder("tests/unit_tests", True)
        struct_gen.add_folder(f"tests/unit_tests/{self.args.name}", True)
        struct_gen.add_folder(f"tests/unit_tests/{self.args.name}/utils", True)

        # Example test
        struct_gen.add_unit_test_file(
            "utils/test_math_utils.py",
            get_file_contents(templates.tests.unit, "test_math_utils.txt"),
        )

    def setup_pipeline(self, cicd_gen: CICDGenerator) -> None:
        """
        Sets up project pipeline.
        """
        cicd_gen.add_job(
            "unit-test",
            {
                "stage": "test",
                "script": [
                    "pipenv run pytest --html=unit-report.html --junitxml=report.xml tests/unit_tests",
                ],
                "artifacts": [
                    {
                        "paths": ["unit-report.html", "report.xml"],
                        "expire_in": "1 month",
                        "reports": {"junit": ["report.xml"]},
                    }
                ],
            },
        )
