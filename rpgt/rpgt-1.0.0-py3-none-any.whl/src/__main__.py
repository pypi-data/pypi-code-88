"""
Main file
"""
import argparse
import os
from typing import List

from rpgt import templates
from rpgt.src.cli.cli import start_cli
from rpgt.src.factories.env_factory import get_env
from rpgt.src.factories.field_factory import get_field
from rpgt.src.factories.vcp_factory import get_vcp
from rpgt.src.generators.changelog_generator import ChangelogGenerator
from rpgt.src.generators.cicd.cicd_generator import CICDGenerator
from rpgt.src.generators.contributing_generator import ContributingGenerator
from rpgt.src.generators.dockerfile_generator import DockerfileGenerator
from rpgt.src.generators.dvc_generator import DVCGenerator
from rpgt.src.generators.environment.environment_generator import EnvironmentGenerator
from rpgt.src.generators.generator import Generator
from rpgt.src.generators.githooks_generator import GitHooksGenerator
from rpgt.src.generators.licence_generator import LicenseGenerator
from rpgt.src.generators.readme_generator import ReadmeGenerator
from rpgt.src.generators.setup_py_generator import SetupGenerator
from rpgt.src.generators.structure_generator import StructureGenerator
from rpgt.src.setup.mllint_setup import MLLintSetup
from rpgt.src.setup.package_setup import PackageSetup
from rpgt.src.setup.pytest_setup import PytestSetup
from rpgt.src.setup.setup import Setup
from rpgt.src.utils.file_reader import get_file_contents
from rpgt.src.utils.file_system import clear_cwd


def main() -> None:
    """
    Main function
    """
    args: argparse.Namespace = start_cli()
    cwd = os.getcwd()

    generators: List[Generator] = []
    setups: List[Setup] = []

    struct_gen = StructureGenerator(args)

    # Field
    setups.append(get_field(args.field, args, cwd))

    # VCP
    vcp_setup = get_vcp(args.version_control, args, cwd)
    setups.append(vcp_setup)
    cicd_gen: CICDGenerator = vcp_setup.get_standard_pipeline()

    # ENV
    env_setup = get_env(args.environment, args, cwd)
    setups.append(env_setup)
    env_gen: EnvironmentGenerator = env_setup.get_standard_env()

    # generators
    # these only configure
    generators.extend(
        [
            LicenseGenerator(args, struct_gen),
            ReadmeGenerator(args, env_gen),
            ContributingGenerator(args, struct_gen),
            ChangelogGenerator(args, struct_gen),
            DockerfileGenerator(args, struct_gen),
        ]
    )

    # these actually generate
    generators.extend([struct_gen, env_gen, cicd_gen])
    generators.append(GitHooksGenerator(args))
    generators.append(DVCGenerator(args, env_gen, struct_gen))

    add_base_files_and_folders(args, struct_gen)

    clear_cwd(cwd)

    # Lint
    if args.lint:
        mllint_setup = MLLintSetup(args, cwd)
        setups.append(mllint_setup)

    # Tests
    if args.test:
        pytest_setup = PytestSetup(args, cwd)
        setups.append(pytest_setup)

    # Package
    if args.package:
        package_setup = PackageSetup(args, cwd)
        setups.append(package_setup)
        setup_gen = SetupGenerator(args, env_gen)
        setup_gen.generate(cwd)
        generators.append(setup_gen)

    for setup in setups:
        setup.setup_dependencies(env_gen)
        setup.setup_files(struct_gen)
        setup.setup_pipeline(cicd_gen)

    for generator in generators:
        generator.generate(cwd)

    print(
        "All set! "
        "Please follow the instructions in the 'Next steps' section on:\n"
        "https://gitlab.com/tweet.dimitri/rpgt/-/wikis/Next%20steps"
    )


def add_base_files_and_folders(
    args: argparse.Namespace, struct_gen: StructureGenerator
) -> None:
    """
    Add the minimally required folders and files
    :param args:
    :param struct_gen:
    :return:
    """
    # Directories
    struct_gen.add_folder("src", False)
    struct_gen.add_folder(f"src/{args.name}", True)
    struct_gen.add_folder(f"src/{args.name}/utils", True)

    struct_gen.add_folder("data", False)
    struct_gen.add_folder("results", False)
    struct_gen.add_folder("results/plots", False)
    struct_gen.add_folder("results/models", False)
    struct_gen.add_folder(".githooks", False)

    struct_gen.add_folder("preprocessed_data", False)

    # Code
    struct_gen.add_src_file(
        "utils/math_utils.py", get_file_contents(templates.code, "math_utils.py")
    )

    # Static files
    struct_gen.add_file(
        ".gitignore", get_file_contents(templates.gitignore, "gitignore.txt")
    )


if __name__ == "__main__":
    main()
