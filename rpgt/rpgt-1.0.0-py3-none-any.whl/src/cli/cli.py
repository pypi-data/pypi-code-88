"""
Command line interface
"""
import argparse
import os
import sys


def get_parser() -> argparse.ArgumentParser:
    """
    Creates a parser which parses the arguments and returns the parser.
    :return: the parser
    """
    parser = argparse.ArgumentParser(
        description="Generator to automatically set up your new project!"
    )

    # name
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        dest="name",
        type=str,
        required=True,
        help="Name of the project.",
    )

    # target directory
    parser.add_argument(
        "-d",
        "--directory",
        metavar="target_directory",
        dest="target_directory",
        type=str,
        required=True,
        help="Directory where your project will generated.",
    )

    # field
    fields = ["ML", "RL", "DL"]
    parser.add_argument(
        "-f",
        "--field",
        metavar="field",
        dest="field",
        type=str,
        default="ML",
        choices=fields,
        help=f"Research field of the project. Allowed values are {', '.join(fields)}.",
    )

    # license
    licenses = ["agpl30", "apache20", "gpl30", "lgpl30", "mit", "mpl20", "unlicense"]
    parser.add_argument(
        "-l",
        "--license",
        metavar="license",
        dest="license",
        type=str,
        default="mit",
        choices=licenses,
        help=f"License of the project. Allowed values are {', '.join(licenses)}.",
    )

    # version control
    vcs = ["gitlab", "github"]
    parser.add_argument(
        "-g",
        "--version-control",
        metavar="",
        dest="version_control",
        type=str,
        default="gitlab",
        choices=vcs,
        help=f"Version control of the project. Allowed values are {', '.join(vcs)}.",
    )

    # environment
    envs = ["pipenv"]
    parser.add_argument(
        "-e",
        "--environment",
        metavar="",
        dest="environment",
        type=str,
        default="pipenv",
        choices=envs,
        help=f"Environment of the project. Allowed values are {', '.join(envs)}.",
    )

    # package
    parser.add_argument(
        "-p",
        "--package",
        metavar="value",
        dest="package",
        type=bool,
        default=True,
        help="Whether the tool is a package.",
    )

    # linting
    parser.add_argument(
        "-i",
        "--lint",
        metavar="value",
        dest="lint",
        type=bool,
        default=True,
        help="Whether the tool should be linted.",
    )

    # testing
    parser.add_argument(
        "-t",
        "--test",
        metavar="value",
        dest="test",
        type=bool,
        default=True,
        help="Whether the tool should be tested.",
    )

    return parser


def start_cli() -> argparse.Namespace:
    """
    Starts the cli program.
    :return:
    """
    parser = get_parser()
    args = parser.parse_args()

    args.name = args.name.replace("-", "_")

    target_directory = args.target_directory.replace("-", "_")
    dir_path = f"{target_directory}"
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    os.chdir(dir_path)

    cwd = os.getcwd()

    # Check if current working directory is empty
    if len(os.listdir(cwd)) != 0:
        answer = input(
            f"The current working directory is not empty! Directory: {target_directory}\n"
            "Everything inside will be removed! Are you sure you want to continue? (y/n)\n"
        )
        if answer != "y":
            sys.exit(0)

    return args
