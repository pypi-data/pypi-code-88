"""
Setup generator module.
"""

import argparse

from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.generator import Generator


class SetupGenerator(Generator):
    """
    Setup generator class.
    """

    def __init__(self, args: argparse.Namespace, env_gen: EnvironmentGenerator):
        """
        Initializes the setup generator.
        """
        super().__init__(args)
        self.env_gen = env_gen

    def generate(self, cwd: str) -> None:
        """
        Writes the setup to file.
        """
        reqs = []

        for requirement, data in self.env_gen.requirements.items():
            if not data["dev_only"]:
                reqs.append(f'"{requirement}"')

        reqs_str = ", ".join(reqs)

        text = "\n".join(
            [
                '"""',
                "setup.py file for package management",
                '"""\n',
                "import setuptools\n",
                'with open("README.md", "r", encoding="utf-8") as fh:',
                "    long_description = fh.read()\n",
                "setuptools.setup(",
                f'    name="{self.args.name}",',
                '    version="0.0.1",',
                '    package_dir={"": "src"},',
                '    packages=setuptools.find_packages(where="src"),',
                '    python_requires=">=3.6",',
                f"    install_requires=[{reqs_str}],",
                ")\n",
            ]
        )

        with open(f"{cwd}/setup.py", "w") as file:
            file.write(text)
