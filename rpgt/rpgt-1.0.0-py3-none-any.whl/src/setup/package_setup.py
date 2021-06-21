"""
 Package setup module.
 """

from rpgt.src.generators.cicd.cicd_generator import CICDGenerator
from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.setup.setup import Setup


class PackageSetup(Setup):
    """
    Package setup class.
    """

    def setup_dependencies(self, env_gen: EnvironmentGenerator) -> None:
        """
        Sets up project dependencies.
        """
        env_gen.add_requirement("setuptools", "~=57.0.0", dev_only=True)

    def setup_pipeline(self, cicd_gen: CICDGenerator) -> None:
        """
        Sets up project pipeline.
        """
        cicd_gen.add_job(
            "publish-package",
            {
                "stage": "production",
                "script": [
                    "pip install wheel twine",
                    "python3 setup.py sdist bdist_wheel",
                    "TWINE_PASSWORD=${CI_JOB_TOKEN} "
                    "TWINE_USERNAME=version_control-ci-token "
                    "python -m twine upload --repository-url "
                    "https://gitlab.com/api/v4/projects/${CI_PROJECT_ID}/packages/pypi dist/*",
                ],
                "only": ["tags"],
            },
        )

    def setup_files(self, struct_gen: StructureGenerator) -> None:
        """
        Sets up project files.
        """
