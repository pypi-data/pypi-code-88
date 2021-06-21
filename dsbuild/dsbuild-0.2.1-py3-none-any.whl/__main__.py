#!/usr/bin/env python

import glob
import os
import re
import shutil
import subprocess
import sys

from argparse import ArgumentParser, RawTextHelpFormatter
from collections import namedtuple
from configparser import ConfigParser
from distutils.spawn import find_executable
from setuptools import find_packages, find_namespace_packages


from .version import get_version
from .__init__ import __version__


# path to the directories
_VENV_NAME = '.venv'
_WHEELS_DIR_NAME = 'wheels'
_BUILD_DIR_NAME = 'build'
_VENV_BIN_SEARCH_DIRS = ['Scripts', 'bin']

##################################################

PYTHON_PREFIX_DIR = sys.prefix

# This script can only be executed from a suitable virtual environment.
if not os.path.basename(PYTHON_PREFIX_DIR) == _VENV_NAME:
    # The following is a workaround for the fact that:
    #       - dsbuild still contains the versioning logic; and
    #       - when doing editable installs of a dependency in the context of docker image
    #         creation, there is no venv, but only system Python.
    # To deal with this problem, an environment variable DSBUILD_ALLOW_NON_VENV allows
    # continuing also when this script is not run from inside a venv. This is a
    # temporary measure (and as such is not announced in the changelog) and will
    # disappear as soon as versioning logic is split off from dsbuild.
    if not os.environ.get('DSBUILD_ALLOW_NON_VENV', False):
        raise RuntimeError('Running from a non-virtual environment is unsupported.')
    else:
        import warnings

        warnings.warn(
            'Running outside of a virtual environment because the environment '
            'variable `DSBUILD_ALLOW_NON_VENV=1`. Continuing without any '
            'guarantees!!'
        )


def get_venv_dir():
    """
    Get the full path to the directory that is supposed to contain the local virtual
    environment.
    """
    return PYTHON_PREFIX_DIR


def get_project_root_dir():
    """
    Get the root directory for this project or package.

    This dir is determined using the assumption that the venv dir is created at this
    top-level.

    Returns:
        str: A path to the root directory of the project.
    """
    return os.path.realpath(os.path.join(get_venv_dir(), '..'))


def get_venv_executable(executable, required=True):
    """
    Return the full path to an executable inside a given virtual environment.

    Args:
        executable (str): Name of the executable.
        required (bool): Whether to consider it a fatal error if the executable is not found.

    Returns:
        str or None: Full path to an executable inside the virtual environment. In case it cannot be found,
                     either an exception is raised or None is returned, depending on whether the executable is
                     required or not.

    Raises:
        FileNotFoundError: When the executable is required and could not be found.
    """
    search_path = [os.path.join(get_venv_dir(), p) for p in _VENV_BIN_SEARCH_DIRS]
    venv_executable = find_executable(
        executable=executable, path=os.pathsep.join(search_path)
    )

    if required and not venv_executable:
        raise FileNotFoundError(
            f'The virtual environment executable could not be '
            f'found: {venv_executable_path}'
        )

    return venv_executable


def get_venv_python(required=True):
    """
    Return the Python executable inside a given virtual environment.

    Args:
        required (bool): Whether to consider it a fatal error if the executable is not found.

    Returns:
        str or None: Full path to the Python executable inside the virtual environment. In case it cannot be
                     found, either an exception is raised or None is returned, depending on whether the
                     executable is required or not.

    Raises:
        FileNotFoundError: When the executable is required and could not be found.
    """
    return get_venv_executable(
        executable=os.path.basename(sys.executable), required=required
    )


def get_lib_version(changelog_path=None):
    """
    A wrapper around version.get_lib_version to provide a sensible default argument.
    """
    if changelog_path is None:
        changelog_path = os.path.join(get_project_root_dir(), 'Changelog.md')

    return get_version(changelog_path=changelog_path)


##################################################
# Helpers to define the modes of this script.

modes = dict()

ModeFunction = namedtuple('ModeFunction', 'func description')


def register(description):
    def decorator_register(func):
        global modes
        function_prefix = 'mode_'
        if not func.__name__.startswith(function_prefix):
            raise ValueError(
                f'Function name of a mode should start with a '
                f"literal '{function_prefix}'."
            )
        modes[func.__name__[len(function_prefix) :]] = ModeFunction(func, description)
        return func

    return decorator_register


def get_valid_modes():
    return list(modes.keys())


def format_mode_description():
    max_len = len(max(get_valid_modes(), key=len))

    result = []
    for k, v in modes.items():
        result.append('{0:>{max_len}}: {1}'.format(k, v.description, max_len=max_len))

    return '\n'.join(result)


def read_dsbuild_config(config_path=None):
    """
    This function reads the config file that contains a dsbuild section.
    If the file does not exist, the default config is returned.
    """
    # default config
    dsbuild_conf = {'package_prefix': '', 'test_dir': 'lib/tests'}

    # default config path
    if config_path is None:
        config_path = os.path.join(get_project_root_dir(), 'setup.cfg')

    # try to read the configuration file
    try:
        config = ConfigParser()
        config.read(config_path)
        dsbuild_conf = {s: dict(config.items(s)) for s in config.sections()}['dsbuild']
    except FileNotFoundError:
        # if the file does not exist, we just return defaults
        pass
    except KeyError:
        # if the [dsbuild] section does not exist, we just return defaults
        pass

    return dsbuild_conf


def find_library(folder):
    """
    Find the python library in a folder and check if it is a normal library or part
    of a namespace package.

    Args:
        folder (str): the folder containing the setup.py file

    Returns:
        str, bool: path to library, False if normal library, True if namespace package
    """
    # try to find a normal library first
    try:
        package = find_packages(folder)
        package = [p for p in package if '.' not in p]
        if len(package) > 1:
            raise ValueError(
                'dsbuild supports only repos with a single library or'
                'multiple namespace packages.'
            )
        return os.path.join(folder, package[0]), False
    except IndexError:
        pass

    # try to find a namespace package
    try:
        package = find_namespace_packages(folder)
        package = [p for p in package if '.' not in p]
        package = package[0]
        is_namespace_pkg = True
    except IndexError:
        raise FileNotFoundError('No library could be found in:', folder)
    return os.path.join(folder, package), is_namespace_pkg


def get_library_dirs():
    """
    Get the paths to the Python library-containing folders.

    A folder contains a library if it contains a `setup.py` file. There are two
    options:
    1. Simple library: A single `setup.py` file is present in the top-level.
    2. Namespace packages: Possibly multiple `setup.py` files can be found
                           underneath the `./lib` directory.

    Returns:
        list of str:
            a list of folders that contain the python library
            (the folder containing the setup.py file)
    """
    project_root_dir = get_project_root_dir()

    # Option 1: Simple library, `setup.py` in top-level.
    if os.path.exists(os.path.join(project_root_dir, 'setup.py')):
        return [project_root_dir]

    # Option 2: Namespace packages.
    setup_files = glob.glob(
        os.path.join(project_root_dir, 'lib', '**', 'setup.py'), recursive=True
    )

    return [os.path.dirname(f) for f in setup_files]


@register(description='Print help.')
def mode_help():
    subprocess.check_call([sys.executable, __file__, '--help'])


@register(description='Clean the project root directory to ensure a clean build.')
def mode_clean():
    """
    Clean the root directory of the project to ensure a clean build.
    """
    dirs_to_clean = [_WHEELS_DIR_NAME, _BUILD_DIR_NAME, 'docs/build']

    project_root_dir = get_project_root_dir()
    for dirname in dirs_to_clean:
        path = os.path.abspath(os.path.join(project_root_dir, dirname))
        try:
            shutil.rmtree(path)
        except FileNotFoundError:
            pass
        except (PermissionError, OSError):
            raise OSError(
                f"The folder '{path}' could not be deleted, "
                'so we are not sure that all build files are fresh.'
            )
        print(f"Cleaned directory '{path}'.")


@register(description='Build documentation.')
def mode_docs():
    """
    Build the documentation.
    """
    lib_version = get_lib_version()
    project_root_dir = get_project_root_dir()

    docs_dir = os.path.join(os.path.join(project_root_dir, 'docs'))
    if not os.path.exists(docs_dir):
        print(
            f"Directory '{docs_dir}' does not exist. "
            f'No documentation will be generated.'
        )
        return

    build_dir = os.path.join(docs_dir, 'build')
    html_dir = os.path.join(build_dir, 'html')
    source_dir = os.path.join(docs_dir, 'source')

    # python and sphinx-apidoc executable
    vpython = get_venv_python()
    sphinx_apidoc = get_venv_executable(executable='sphinx-apidoc.exe')

    # get all libraries
    libs = get_library_dirs()
    if not libs:
        raise ValueError(f'No python libraries could be found in {project_root_dir}')

    # run sphinx-apidoc on all libraries
    for lib_dir in libs:
        lib_folder, is_namespace_pkg = find_library(lib_dir)

        command = [sphinx_apidoc, '-o', source_dir, lib_folder, '-f', '-e']
        if is_namespace_pkg:
            command += ['--implicit-namespaces']
        subprocess.check_call(command, cwd=project_root_dir)
    library_name = os.path.basename(lib_folder)

    # run sphinx
    command = [vpython, '-m', 'sphinx', source_dir, html_dir]
    subprocess.check_call(command, cwd=project_root_dir)

    # Copy and version docs
    dsbuild_config = read_dsbuild_config()
    package_name = dsbuild_config['package_prefix'] + library_name
    wheels_dir = os.path.abspath(os.path.join(project_root_dir, _WHEELS_DIR_NAME))
    wheels_lib_dir = os.path.join(wheels_dir, package_name)
    docs_dst = os.path.join(wheels_lib_dir, f'docs_{lib_version}')
    # TODO: The following will fail if `wheel_docs` already exists.
    shutil.copytree(src=html_dir, dst=docs_dst)
    print('Docs copied to:', docs_dst)


@register(description='Publish the changelog file.')
def mode_changelog():
    """
    Publish the changelog file.
    """
    project_root_dir = get_project_root_dir()
    lib_version = get_lib_version()

    # get all libraries
    libs = get_library_dirs()
    if not libs:
        raise ValueError(f'No python libraries could be found in {project_root_dir}')

    for lib_dir in libs:
        lib_folder, is_namespace_pkg = find_library(lib_dir)
    library_name = os.path.basename(lib_folder)

    # define the target directory to save the changelog file in
    dsbuild_config = read_dsbuild_config()
    # Take into account an optional "package prefix". This allows to create a package
    # `DS-imetric` with library `imetric`.
    package_name = dsbuild_config['package_prefix'] + library_name
    wheels_dir = os.path.abspath(os.path.join(project_root_dir, _WHEELS_DIR_NAME))
    wheels_lib_dir = os.path.join(wheels_dir, package_name)

    # Copy Changelog.md
    changelog_src = os.path.join(project_root_dir, 'Changelog.md')
    changelog_dst = os.path.join(wheels_lib_dir, f'Changelog_{lib_version}.md')

    if os.path.exists(changelog_src):
        with open(changelog_src, 'rt') as fid:
            changelog_text = fid.read()

        os.makedirs(os.path.dirname(changelog_dst), exist_ok=True)
        txt = re.sub(_CHANGELOG_REGEX, f'## {lib_version}', changelog_text, 1)

        with open(changelog_dst, 'wt') as fid:
            fid.write(txt)

        print('Changelog copied to:', changelog_dst)


@register(description='Build wheel.')
def mode_wheel():
    """
    Build a wheel of the library.
    """
    project_root_dir = get_project_root_dir()
    wheels_dir = os.path.abspath(os.path.join(project_root_dir, _WHEELS_DIR_NAME))
    all_build_dir = os.path.abspath(os.path.join(project_root_dir, _BUILD_DIR_NAME))

    dsbuild_config = read_dsbuild_config()

    libraries = get_library_dirs()
    if not libraries:
        raise ValueError(f'No python libraries could be found in {project_root_dir}')

    for library in libraries:
        lib_folder, is_namespace_pkg = find_library(library)

        if is_namespace_pkg:
            lib_name = os.path.basename(library)
        else:
            lib_name = os.path.basename(lib_folder)

        package_name = dsbuild_config['package_prefix'] + lib_name
        build_dir = os.path.join(all_build_dir, f'build-{lib_name}')
        bdist_dir = os.path.join(all_build_dir, f'bdist-{lib_name}')
        this_wheel_dir = os.path.join(wheels_dir, package_name)

        # run the wheel creation command
        command = [
            get_venv_python(),
            'setup.py',
            'build',
            '-b',
            build_dir,
            'bdist_wheel',
            f'--bdist-dir={bdist_dir}',
            f'--dist-dir={this_wheel_dir}',
            '-k',
        ]
        subprocess.check_call(command, cwd=library)

    print(f"Wheel(s) created in '{wheels_dir}'")


@register(description='Run unittests + coverage.')
def mode_test():
    """
    Run unittests and coverage report. The tests are being picked up from a directory
    with name matching the pattern `*_test` or from `lib/tests`. Note that at most a
    single directory on disk should match. If not, this is considered a fatal error.
    """
    project_root_dir = get_project_root_dir()

    # check if we can find libraries, otherwise raise exception
    libs = get_library_dirs()
    if not libs:
        raise ValueError(f'No python libraries could be found in {project_root_dir}')

    # Get a list of (existing) folders that can contain tests.
    test_folders = []
    # 1. Legacy: dirs of the form `*_test`
    test_folders += [
        f
        for f in glob.glob(os.path.join(project_root_dir, '*_test'))
        if os.path.isdir(f)
    ]
    # 2. Custom (or new): By default `lib/tests`, but can be configured in `setup.cfg`.
    dsbuild_config = read_dsbuild_config()
    test_dir = os.path.join(project_root_dir, dsbuild_config['test_dir'])
    test_folders += [f for f in [test_dir] if os.path.isdir(test_dir)]

    if len(test_folders) == 0:
        print(f'Could not find a folder with unittests. No tests will be run.')
        return

    if len(test_folders) > 1:
        raise FileNotFoundError(
            f'Could not find a unique folder with unittests. Found: {test_folders}.'
        )

    test_folder = test_folders[0]

    # We only want to report coverage info for the source files in our library (i.e. we
    # need to provide a suitable filter to `--cov=...` when running pytest).
    # For this purpose we use the library directories found in the project. Each of them
    # needs to have it's own '--cov' argument.
    cov_args = [f'--cov={os.path.relpath(lib, project_root_dir)}' for lib in libs]

    # run tests
    command = [
        get_venv_python(),
        '-m',
        'pytest',
        test_folder,
        f'--junitxml={test_folder}_results/test-results.xml',
        *cov_args,
        f'--cov-report=term',
        f'--cov-report=xml:{test_folder}_results/coverage.xml',
        f'--cov-report=html:{test_folder}_results/html',
    ]
    subprocess.check_call(command, cwd=project_root_dir)

    print('Ran all unittests.')


@register(description='Print the library version.')
def mode_version():
    """
    Print library version.
    """
    parser = ArgumentParser(
        prog='dsbuild version',
        formatter_class=RawTextHelpFormatter,
        description='Determine the version of a library.',
    )

    parser.add_argument(
        '--changelog',
        '-clog',
        default=None,
        help='Path to the Changelog.md file for version parsing.',
    )

    args = parser.parse_args(args=sys.argv[2:])

    lib_version = get_lib_version(changelog_path=args.changelog)
    print(lib_version)


@register(description='Generate a self-sufficient version.py at the project root.')
def mode_generate_version_py():
    """
    Generate a self-sufficient version.py script.
    """
    parser = ArgumentParser(
        prog='dsbuild generate-version-py',
        formatter_class=RawTextHelpFormatter,
        description='Generate a self-sufficient version.py at the project root.',
    )

    args = parser.parse_args(args=sys.argv[2:])

    src = os.path.join(os.path.dirname(__file__), 'version.py')
    dst = os.path.join(get_project_root_dir(), 'version.py')

    with open(src, 'r') as fin, open(dst, 'w') as fout:
        header = (
            f'#########################################################################'
            f'###############\n'
            f'#\n'
            f'# THIS FILE WAS AUTO-GENERATED BY DSBUILD {__version__}.\n'
            f'#\n'
            f'# IT SHOULD BE COMMITTED TO THE PROJECT ROOT DIRECTORY AND PREFERABLY '
            f'NOT MODIFIED\n'
            f'# MANUALLY.\n'
            f'#\n'
            f'# YOU CAN ALWAYS REGENERATE IT BY RUNNING:\n'
            f'#   $ dsbuild generate_version_py\n'
            f'#\n'
            f'#########################################################################'
            f'###############\n\n\n'
        )

        fout.write(header)
        fout.write(fin.read())

    print(f'Version.py file generated at {dst}')


@register(description='clean + test + docs + wheel.')
def mode_all():
    """
    Convenience mode that does 'everything' from scratch (build, test, packaging).
    """
    mode_clean()
    mode_test()
    mode_docs()
    mode_wheel()


@register(description='clean + docs + wheel.')
def mode_package():
    """
    Convenience mode that does a clean packaging.
    """
    mode_clean()
    mode_docs()
    mode_wheel()


def main():
    parser = ArgumentParser(
        prog='dsbuild',
        formatter_class=RawTextHelpFormatter,
        description=(
            'This script helps to build and package python libraries.\n'
            + format_mode_description()
        ),
    )
    parser.add_argument(
        '--version', '-v', action='version', version=f'%(prog)s {__version__}'
    )
    parser.add_argument(
        'mode', default='all', const='all', nargs='?', choices=get_valid_modes()
    )

    # Only parse the mode argument here so that sub commands can parse the rest
    args, _ = parser.parse_known_args(args=sys.argv[1:])

    try:
        modes[args.mode].func()
    except KeyError:
        raise ValueError(f"Bad input mode '{args.mode}'.")


if __name__ == '__main__':
    main()
