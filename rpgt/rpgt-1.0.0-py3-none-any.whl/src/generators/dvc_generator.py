"""
DVC generator module.
"""
import argparse
import subprocess  # nosec

from rpgt import templates
from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.generator import Generator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.utils.file_reader import get_file_contents


class DVCGenerator(Generator):
    """
    DVC generator class.
    """

    def __init__(
        self,
        args: argparse.Namespace,
        env_gen: EnvironmentGenerator,
        struct_gen: StructureGenerator,
    ):
        """
        Abstract initialize function definition.
        """
        super().__init__(args)
        self.struct_gen = struct_gen
        env_gen.add_requirement("dvc", "~=2.3.0", dev_only=True)

        field = self.args.field
        if field == "RL":
            filename = "rl.yaml"
        elif field == "DL":
            filename = "dl.yaml"
        elif field == "ML":
            filename = "ml.yaml"
        else:
            raise Exception(f"'{field}' is not supported as a field")

        self.struct_gen.add_file(
            "dvc.yaml",
            get_file_contents(templates.dvc, filename),
        )

    def generate(self, cwd: str) -> None:
        """
        Generates the DVC configuration file.
        """
        with subprocess.Popen(  # nosec
            ["dvc", "init"], stdout=subprocess.PIPE
        ) as process:
            process.wait()
