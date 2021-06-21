"""
ML setup module.
"""

from rpgt import templates
from rpgt.src.generators.cicd.cicd_generator import CICDGenerator
from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.setup.field.field_setup import FieldSetup
from rpgt.src.utils.file_reader import get_file_contents


class MLSetup(FieldSetup):
    """
    ML setup class.
    """

    def setup_dependencies(self, env_gen: EnvironmentGenerator) -> None:
        """
        Sets up project dependencies.
        """
        env_gen.add_requirement("scipy", "*", dev_only=False)
        env_gen.add_requirement("numpy", "~=1.20.3", dev_only=False)
        env_gen.add_requirement("pandas", "~=1.2.4", dev_only=False)
        env_gen.add_requirement("sklearn", "*", dev_only=False)

    def setup_files(self, struct_gen: StructureGenerator) -> None:
        """
        Sets up project files.
        """
        struct_gen.add_src_file(
            "get_data.py",
            get_file_contents(templates.code.sklearn, "get_data.txt"),
        )
        struct_gen.add_src_file(
            "preprocess.py",
            get_file_contents(templates.code.sklearn, "preprocess.txt"),
        )
        struct_gen.add_src_file(
            "train.py",
            get_file_contents(templates.code.sklearn, "train.txt"),
        )
        struct_gen.add_src_file(
            "validate.py",
            get_file_contents(templates.code.sklearn, "validate.txt"),
        )

    def setup_pipeline(self, cicd_gen: CICDGenerator) -> None:
        """
        Sets up project pipeline.
        """
