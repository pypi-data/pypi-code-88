import sys
from argparse import ArgumentParser
from typing import List, Union

from loguru import logger

from . import BaseELGCommand


def docker_create_command_factory(args):
    return DockerCreateCommand(
        classname=args.classname,
        path=args.path,
        requirements=args.requirements,
        requirements_file=args.requirements_file,
        required_files=args.required_files,
        required_folders=args.required_folders,
    )


class DockerCreateCommand(BaseELGCommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        info_parser = parser.add_parser("create", description="Create requirements.txt and Docker files.")
        info_parser.add_argument(
            "-n", "--classname", type=str, default=None, required=True, help="Name of the Service Class"
        )
        info_parser.add_argument(
            "-p",
            "--path",
            type=str,
            default="",
            required=None,
            help="Path the python script containing the Service Class definition from the current location",
        )
        info_parser.add_argument(
            "-r",
            "--requirements",
            type=str,
            action="append",
            default=None,
            required=False,
            help="Pypi requirements for the Service Class, e.g. `nltk==3.5`",
        )
        info_parser.add_argument(
            "--requirements_file",
            type=str,
            default=None,
            required=False,
            help="Pypi requirements file, e.g. `requirements.txt`",
        )
        info_parser.add_argument(
            "-f",
            "--required_files",
            type=str,
            action="append",
            default=None,
            required=False,
            help="Name of the files from the directory of the Service Class",
        )
        info_parser.add_argument(
            "--required_folders",
            type=str,
            action="append",
            default=None,
            required=False,
            help="Name of the folders from the directory of the Service Class",
        )

        info_parser.set_defaults(func=docker_create_command_factory)

    def __init__(
        self,
        classname: str = None,
        path: str = "",
        requirements: Union[str, List[str]] = None,
        requirements_file: str = None,
        required_files: Union[str, List[str]] = None,
        required_folders: Union[str, List[str]] = None,
    ):
        self._classname = classname
        self._path = path
        self._requirements = requirements
        self._requirements_file = requirements_file
        self._required_files = required_files
        self._required_folders = required_folders

    def run(self):
        from ..flask_service import FlaskService

        try:
            logger.info(f"Creation of `requirements.txt`")
            if self._requirements is None:
                requirements = []
            elif isinstance(self._requirements, str):
                requirements = [self._requirements]
            else:
                requirements = self._requirements
            if self._requirements_file is None:
                pass
            else:
                with open(self._requirements_file) as f:
                    requirements += f.read().split("\n")
            FlaskService.create_requirements(requirements=requirements, path=self._path)
            logger.info(f"Creation of `Dockerfile` and `docker-entrypoint.sh`")
            if self._required_files is None:
                required_files = []
            elif isinstance(self._required_files, str):
                required_files = [self._required_files]
            else:
                required_files = self._required_files
            if self._required_folders is None:
                required_folders = []
            elif isinstance(self._required_folders, str):
                required_folders = [self._required_folders]
            else:
                required_folders = self._required_folders
            FlaskService.create_docker_files(
                required_files=required_files, required_folders=required_folders, path=self._path
            )
        except Exception as e:
            logger.error(f"Error during the creation of docker files - {e}")
            sys.exit(1)
