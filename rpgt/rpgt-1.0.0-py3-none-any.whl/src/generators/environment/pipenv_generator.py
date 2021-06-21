"""
Pipenv generator module.
"""

import argparse

from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator


class PipEnvGenerator(EnvironmentGenerator):
    """
    Pipenv generator class.
    """

    def __init__(self, args: argparse.Namespace):
        """
        Initialize pipenv generator with proper parameters.
        """
        super().__init__(args)
        self.add_requirement("pipenv", "~=2021.5.29", dev_only=True)

    def add_requirement(
        self, requirement: str, version: str, dev_only: bool = False
    ) -> None:
        """
        Add requirement to env.
        """
        self.requirements[requirement] = {"version": version, "dev_only": dev_only}

    def generate(self, cwd: str) -> None:
        """
        Generate the pipenv.
        """
        text = []

        text.append("[[source]]")
        text.append('url = "https://pypi.org/simple"')
        text.append("verify_ssl = true")
        text.append('name = "pypi"\n')

        text.append("[packages]")

        for requirement, data in self.requirements.items():
            if not data["dev_only"]:
                text.append(f'{requirement} = "{data["version"]}"')

        text.append("\n[dev-packages]")

        for requirement, data in self.requirements.items():
            if data["dev_only"]:
                text.append(f'{requirement} = "{data["version"]}"')

        text.append("\n[requires]")
        text.append('python_version = "3.8"')

        with open(f"{cwd}/Pipfile", "w") as file:
            file.write("\n".join(text))
