"""
Github setup module.
"""

from rpgt import templates
from rpgt.src.generators.cicd.cicd_generator import CICDGenerator
from rpgt.src.generators.cicd.github_ci_generator import GithubCICDGenerator
from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.setup.vcp.vcp_setup import VCPSetup
from rpgt.src.utils.file_reader import get_file_contents


class GithubSetup(VCPSetup):
    """
    Github setup class.
    """

    def get_standard_pipeline(self) -> GithubCICDGenerator:
        """
        Sets up project pipeline.
        """
        return GithubCICDGenerator(self.args)

    def setup_files(self, struct_gen: StructureGenerator) -> None:
        """
        Sets up project files.
        """
        # Directories
        struct_gen.add_folder(".github", False)
        struct_gen.add_folder(".github/ISSUE_TEMPLATE", False)
        struct_gen.add_folder(".github/MERGE_REQUEST_TEMPLATE", False)

        # version_control files
        struct_gen.add_file(
            ".github/ISSUE_TEMPLATE/Bug.md",
            get_file_contents(templates.version_control.issue_templates, "Bug.md"),
        )
        struct_gen.add_file(
            ".github/ISSUE_TEMPLATE/Feature.md",
            get_file_contents(templates.version_control.issue_templates, "Feature.md"),
        )
        struct_gen.add_file(
            ".github/MERGE_REQUEST_TEMPLATE/Feature.md",
            get_file_contents(
                templates.version_control.merge_request_templates, "default.md"
            ),
        )

    def setup_dependencies(self, env_gen: EnvironmentGenerator) -> None:
        """
        Sets up project dependencies.
        """

    def setup_pipeline(self, cicd_gen: CICDGenerator) -> None:
        """
        Sets up project pipeline.
        """
