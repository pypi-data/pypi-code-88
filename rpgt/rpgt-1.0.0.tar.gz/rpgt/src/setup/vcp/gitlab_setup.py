"""
Gitlab setup module.
"""

from rpgt import templates
from rpgt.src.generators.cicd.cicd_generator import CICDGenerator
from rpgt.src.generators.cicd.gitlab_ci_generator import GitlabCICDGenerator
from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.setup.vcp.vcp_setup import VCPSetup
from rpgt.src.utils.file_reader import get_file_contents


class GitlabSetup(VCPSetup):
    """
    Gitlab setup class.
    """

    def get_standard_pipeline(self) -> GitlabCICDGenerator:
        """
        Sets up project pipeline.
        """
        return GitlabCICDGenerator(self.args)

    def setup_files(self, struct_gen: StructureGenerator) -> None:
        """
        Sets up project files.
        """
        # Directories
        struct_gen.add_folder(".gitlab", False)
        struct_gen.add_folder(".gitlab/issue_templates", False)
        struct_gen.add_folder(".gitlab/merge_request_templates", False)

        # version_control files
        struct_gen.add_file(
            ".gitlab/issue_templates/Bug.md",
            get_file_contents(templates.version_control.issue_templates, "Bug.md"),
        )
        struct_gen.add_file(
            ".gitlab/issue_templates/Feature.md",
            get_file_contents(templates.version_control.issue_templates, "Feature.md"),
        )
        struct_gen.add_file(
            ".gitlab/merge_request_templates/default.md",
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
