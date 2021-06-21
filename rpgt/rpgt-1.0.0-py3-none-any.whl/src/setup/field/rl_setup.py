"""
RL setup module.
"""

from rpgt import templates
from rpgt.src.generators.cicd.cicd_generator import CICDGenerator
from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.setup.field.field_setup import FieldSetup
from rpgt.src.utils.file_reader import get_file_contents


class RLSetup(FieldSetup):
    """
    RL setup class.
    """

    def setup_dependencies(self, env_gen: EnvironmentGenerator) -> None:
        """
        Sets up project dependencies.
        """
        env_gen.add_requirement("stable-baselines3", "*", dev_only=False)
        env_gen.add_requirement("gym", "~=0.18.3", dev_only=False)

    def setup_files(self, struct_gen: StructureGenerator) -> None:
        """
        Sets up project files.
        """
        struct_gen.add_src_file(
            "__main__.py",
            get_file_contents(templates.code.stablebaselines, "__main__.txt"),
        )
        struct_gen.add_src_file(
            "model_loader.py",
            get_file_contents(templates.code.stablebaselines, "model_loader.txt"),
        )
        struct_gen.add_src_file(
            "get_environment.py",
            get_file_contents(templates.code.stablebaselines, "get_environment.txt"),
        )

    def setup_pipeline(self, cicd_gen: CICDGenerator) -> None:
        """
        Sets up project pipeline.
        """
