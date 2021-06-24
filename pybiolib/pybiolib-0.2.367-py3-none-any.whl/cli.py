import argparse
import logging
import os
import sys
import tempfile

from docker.errors import ImageNotFound  # type: ignore

from biolib import cli_utils, utils
from biolib.app import BioLibApp, BioLib
from biolib.cli_utils import BiolibValidationError
from biolib.validators.validate_zip_file import validate_zip_file  # type: ignore
from biolib.biolib_docker_client import BiolibDockerClient
from biolib.biolib_logging import logger


class IllegalArgumentError(ValueError):
    pass


def file_path(path):
    if path.startswith('/'):
        full_path = path
    else:
        full_path = os.path.normpath(os.path.join(os.getcwd(), path))
    if not os.path.exists(full_path):
        raise IllegalArgumentError(f'The path {full_path} does not exist')
    return full_path


def port_number(port):
    if not port.isdigit():
        raise IllegalArgumentError(f'Port number {port} is not a number. Ports can only be numbers')

    if not (0 < int(port) < 65000):  # pylint: disable=superfluous-parens
        raise IllegalArgumentError('Port can only be between 0 and 65000')

    return port


def main():
    # set more restrictive default log level for CLI
    logger.configure(default_log_level=logging.WARNING)

    if len(sys.argv) > 2 and sys.argv[1] == 'run':
        app = BioLibApp(uri=sys.argv[2])
        stdin = None
        if not sys.stdin.isatty() and not utils.IS_DEV:
            stdin = sys.stdin.read()
        app_args = sys.argv[3:]
        result = app(args=app_args, stdin=stdin, files=None)
        sys.stdout.buffer.write(result.stdout)
        sys.stderr.buffer.write(result.stderr)
        sys.exit(result.exitcode)

    elif len(sys.argv) > 2 and sys.argv[1] == 'run-dev':
        provided_app_path = sys.argv[2]
        app_path = cli_utils.validate_and_get_app_path(provided_app_path)
        logger.info(f'Running BioLib application in local directory {app_path}...')
        source_files_temp_dir = tempfile.TemporaryDirectory()
        source_files_zip_path = cli_utils.get_source_files_zip(app_path, source_files_temp_dir)
        try:
            validate_zip_file(source_files_zip_path, app_path)
            yaml_data = cli_utils.get_yaml_data(app_path)
            cli_utils.validate_yaml_config(yaml_data, source_files_zip_path)
            module = cli_utils.get_main_module_from_yaml(yaml_data, validate_local_docker_only=True)

            try:
                BiolibDockerClient.get_docker_client().images.get(module['image'])
            except ImageNotFound:
                logger.error(
                    f"Could not find local docker image {module['image']} specified in .biolib/config.yml")
                sys.exit(1)

            app_args = sys.argv[3:]
            args = cli_utils.validate_and_get_args(app_args)
            files_dict, args = cli_utils.get_files_dict_and_file_args(files=None, args=args)

            BioLib.run_local_docker_app(files_dict, args, module, source_files_temp_dir)

        except Exception as exception:
            # Exit on BiolibValidationError as we have already printed the validation errors
            if isinstance(exception, BiolibValidationError):
                logger.error('Validation check failed for config file at .biolib/config.yml')
                sys.exit(1)
            raise exception

    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('--version', action='version', version=utils.BIOLIB_PACKAGE_VERSION)

        subparsers = parser.add_subparsers(help='command', dest='command')

        # Add subparser for run to help message makes sense
        # The actual code for running applications is above this
        _parser_run = subparsers.add_parser('run', help='Run an application on BioLib')

        # Add subparser for run to help message makes sense
        # The actual code for running local applications is above this
        _parser_run_dev = subparsers.add_parser('run-dev', help='Run an application from a local directory')

        # add subparser for push
        parser_push = subparsers.add_parser('push', help='Push an application to BioLib')
        parser_push.add_argument('author_and_app_name')
        parser_push.add_argument('--path', default='.', required=False)

        parser_compute_process = subparsers.add_parser('start-compute-process', help='Start a compute process')
        parser_compute_process.add_argument('--enclave', required=False, action='store_true')
        parser_compute_process.add_argument('--port', required=False, type=port_number)

        # add subparser for run-compute-node
        parser_start = subparsers.add_parser('start', help='Start a compute node')
        parser_start.add_argument('--enclave', required=False, action='store_true')
        parser_start.add_argument('--port', default='5000', required=False, type=port_number)
        parser_start.add_argument('--host', default='127.0.0.1', required=False)

        args = parser.parse_args()

        if args.command == 'push':
            # at least use INFO logging for push
            logger.configure(default_log_level=logging.INFO)
            BioLib.push(args.author_and_app_name, args.path)
        elif args.command == 'start':
            # at least use INFO logging for start
            logger.configure(default_log_level=logging.INFO)
            BioLib.start_compute_node(args.port, args.host, args.enclave)
        elif args.command == 'start-compute-process':
            BioLib.start_compute_process(socket_port=args.port, is_running_in_enclave=args.enclave)
        else:
            print('Unrecognized command, please run biolib --help to see available options.')
            sys.exit(1)
