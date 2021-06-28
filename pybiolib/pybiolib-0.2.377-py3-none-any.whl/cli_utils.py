import os
import shutil
import sys
import platform
import time
from pathlib import Path
from zipfile import ZipFile
from termcolor import colored

import yaml
from biolib.validators.validate_app_version import validate_app_version  # type: ignore
from biolib.validators.validate_argument import validate_argument  # type: ignore
from biolib.validators.validate_module import validate_module  # type: ignore
from biolib.biolib_errors import BioLibError
from biolib.biolib_logging import logger


class BiolibValidationError(Exception):
    pass


def bl_colored(string, colour):
    # The colors does not seem to play nice with Windows PowerShell terminal
    if platform.system() == 'Windows':
        return string
    else:
        return colored(string, colour)


def validate_and_get_args(args):
    if args is None:
        args = []

    if isinstance(args, str):
        args = list(filter(lambda p: p != '', args.split(' ')))

    if not isinstance(args, list):
        raise Exception('The given input arguments must be list or str')

    return args


def get_files_dict_and_file_args(files, args):
    if files is None:
        files = []
        # TODO: Figure out how to make this slightly less error prone
        for idx, arg in enumerate(args):
            if not arg.startswith('/'):
                arg = f'{os.getcwd()}/{arg}'

            arg = Path(arg)
            if arg.is_file():
                files.append(arg)
                # Make sure that arg is only the filename
                args[idx] = arg.parts[-1]

    files_dict = {}
    for file_path in files:
        file = open(file_path, 'rb')
        path = '/' + file_path.parts[-1]

        files_dict[path] = file.read()
        file.close()

    return files_dict, args


def validate_and_get_app_path(provided_app_path):
    if provided_app_path.startswith('/'):
        app_path = Path(provided_app_path)
    else:
        app_path = Path(os.getcwd()) / provided_app_path

    if not app_path.exists():
        print(f'ERROR: Could not find path {app_path}')
        sys.exit(1)

    if not app_path.is_dir():
        print(f'ERROR: Path {app_path} is not a directory')
        sys.exit(1)

    return app_path


def get_source_files_zip(app_path, source_files_temp_dir):
    cwd = os.getcwd()
    os.chdir(app_path)
    zip_name = 'biolib_run_dev'
    zip_filename = f'{zip_name}.zip'
    logger.debug(f'Zipping app path {app_path}')
    shutil.make_archive(f'{source_files_temp_dir.name}/{zip_name}', 'zip', base_dir='.')
    # change back to old working directory
    os.chdir(cwd)
    return f'{source_files_temp_dir.name}/{zip_filename}'


def get_yaml_data(app_path):
    try:
        yaml_file = open(f'{app_path}/.biolib/config.yml', 'r', encoding='utf-8')

    except Exception as error:  # pylint: disable=broad-except
        raise BioLibError(f'Could not open the biolib config file at {app_path}/.biolib/config.yml') from error

    try:
        yaml_data = yaml.safe_load(yaml_file)

    except Exception as error:  # pylint: disable=broad-except
        raise BioLibError(f'Could not parse {app_path}/.biolib/config.yml. Please make sure it is valid YAML') \
            from error

    return yaml_data


def set_mappings_from_yaml(yaml_data, module, mapping_type):
    module[f'{mapping_type}_files_mappings'] = []
    for mapping in yaml_data.get(f'{mapping_type}_files'):
        _, from_path, to_path = mapping.split(' ')
        module[f'{mapping_type}_files_mappings'].append({'from_path': from_path, 'to_path': to_path})


def validate_arguments(yaml_data):
    error_dict = {'arguments': {}}
    # Arguments are optional
    if 'arguments' in yaml_data:
        for argument in yaml_data['arguments']:
            argument_errors = validate_argument(argument)
            if argument_errors:
                error_dict['arguments'].update(argument_errors)

    # Just return empty dict if we have no errors
    if error_dict['arguments']:
        return error_dict
    else:
        return {}


def validate_and_get_biolib_yaml_version(yaml_data, error_dict):
    if not 'biolib_version' in yaml_data.keys():
        error_dict['config_yml']['biolib_version'] = ['Your config file is missing the biolib_version field.']
        print_errors(error_dict)
        sys.exit(1)
    else:
        biolib_version = yaml_data['biolib_version']

    if biolib_version not in (1, 2):
        error_dict['config_yml']['biolib_version'] = \
            [f'Biolib version can only be either 1 or 2 for now, your version is {biolib_version}.']
        print_errors(error_dict)
        sys.exit(1)

    return biolib_version


def validate_modules(yaml_data, biolib_yaml_version):
    error_dict = {'modules': {}}
    if 'modules' in yaml_data:
        for name, task_data in yaml_data['modules'].items():
            task_errors = validate_module(name, task_data, biolib_yaml_version)
            if task_errors:
                error_dict['modules'].update(task_errors)

    # Just return empty dict if we have no errors
    if error_dict['modules']:
        return error_dict
    else:
        return {}


def validate_yaml_config(yaml_data, source_files_zip_path):
    source_files_zip = ZipFile(source_files_zip_path)
    error_dict = {'config_yml': {}}

    biolib_yaml_version = validate_and_get_biolib_yaml_version(yaml_data, error_dict)
    error_dict['config_yml'].update(validate_app_version(yaml_data, biolib_yaml_version, source_files_zip))
    error_dict['config_yml'].update(validate_modules(yaml_data, biolib_yaml_version))
    error_dict['config_yml'].update(validate_arguments(yaml_data))

    if error_dict['config_yml']:
        print_errors(error_dict)
        raise BiolibValidationError('Could not validate .biolib/config.yml')


def print_errors(error_dict):
    print(bl_colored("\nThe following validation errors were found in the .biolib/config.yml file:", 'red'))
    print(yaml.safe_dump(error_dict, allow_unicode=True, default_flow_style=False))


def get_main_module_from_yaml(yaml_data, validate_local_docker_only=False):
    for yaml_module_name, yaml_module in yaml_data['modules'].items():
        if yaml_module_name != 'main':
            continue
        main_module = {}
        set_mappings_from_yaml(yaml_module, main_module, mapping_type='input')
        set_mappings_from_yaml(yaml_module, main_module, mapping_type='source')
        set_mappings_from_yaml(yaml_module, main_module, mapping_type='output')

        main_module['working_directory'] = yaml_module.get('working_directory', '/')
        main_module['command'] = yaml_module.get('command', '')

        if validate_local_docker_only:
            main_module['image'] = validate_and_set_image(yaml_module)
        else:
            main_module['image'] = yaml_module.get('image')

        return main_module


def validate_and_set_image(module):
    image = module.get('image')
    # Image is validated to be of correct format at this point
    environment, image_name = image.split('://')

    if not environment == 'local-docker':
        logger.error("Your app must use a local docker image to use this command.")
        logger.error(f"Found image {image_name} using environment {environment}, please use 'local-docker://'")
        sys.exit(1)

    return image_name


def write_output_files(mapped_output_files=None):
    output_dir_path = 'biolib_results'

    if os.path.exists(output_dir_path):
        os.rename(output_dir_path, f'{output_dir_path}_old_{time.strftime("%Y%m%d%H%M%S")}')

    if mapped_output_files:
        logger.debug("Output Files:")

        for path, data in mapped_output_files.items():
            dirs, file = os.path.split(path)
            path_on_disk = f'{output_dir_path}{path}'

            if dirs:
                os.makedirs(f'{output_dir_path}{dirs}', exist_ok=True)
            if file:
                open(path_on_disk, 'wb').write(data)

            logger.debug(f"  - {path_on_disk}")

        logger.debug('\n')


def get_pretty_print_module_output_string(stdout=None, stderr=None, exitcode=None) -> str:
    stderr_string = f"\n{bl_colored('stderr:', 'red')}\n{stderr.decode()}" if stderr else ''
    return f'''{bl_colored('stdout:', 'green')}
{stdout.decode()}{stderr_string}
{bl_colored('exitcode:', 'green' if exitcode == 0 else 'red')} {exitcode}'''
