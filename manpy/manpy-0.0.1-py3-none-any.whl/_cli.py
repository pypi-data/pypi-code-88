import os
import re
import argparse
import configparser

from manpy._template import VERSION, SETUP
from manpy._utils import checking_special_character, modify_setup


# def main():
#     pkg_name = checking_special_character('Package name ?')
#     if os.path.exists(pkg_name):
#         raise FileExistsError(f'A directory with the name {pkg_name} already exist')
#     if os.path.exists('setup.py'):
#         raise FileExistsError(f'A file setup.py already exist')
#     if os.path.exists('conda'):
#         raise FileExistsError(f'A directory conda already exist')
#
#     DEFAULT_VALUES = default_values(pkg_name)
#
#     os.mkdir(pkg_name)
#     with open(pkg_name+'/__init__.py', 'w') as f:
#         pass
#     setup_file = re.sub('{PKG_NAME}', pkg_name, SETUP)
#
#     print(f'Author (default: {DEFAULT_VALUES.pkg_auth}) ?')
#     pkg_auth = input('>')
#     if pkg_auth.strip() == '':
#         pkg_auth = DEFAULT_VALUES.pkg_auth
#     setup_file = re.sub('{PKG_AUTH}', pkg_auth, setup_file)
#
#     print(f'Author email (default: {DEFAULT_VALUES.pkg_email}) ?')
#     pkg_email = input('>')
#     if pkg_email.strip() == '':
#         pkg_email = DEFAULT_VALUES.pkg_email
#     setup_file = re.sub('{PKG_EMAIL}', pkg_email, setup_file)
#
#     print(f'Package version (default: {DEFAULT_VALUES.pkg_ver}) ?')
#     pkg_ver = input('>')
#     if pkg_ver.strip() == '':
#         pkg_ver = DEFAULT_VALUES.pkg_ver
#     setup_file = re.sub('{PKG_VER}', pkg_ver, setup_file)
#
#     with open('setup.py', 'w') as f:
#         f.write(setup_file)
#
#     conda_create = checking_boolean_input('making conda package')
#     if conda_create:
#         os.mkdir('conda')
#
#         print(f'Conda environnement name (default: {DEFAULT_VALUES.conda_name}) ?')
#         conda_name = input('>')
#         if conda_name.strip() == '':
#             conda_name = DEFAULT_VALUES.conda_name
#         conda_file = re.sub('{CONDA_NAME}', conda_name, CONDA_ENV)
#
#         print(f'Conda channels separate by a space (default: {DEFAULT_VALUES.conda_channels}) ?')
#         conda_channels = input('>')
#         if conda_channels.strip() == '':
#             conda_channels = '  - ' + DEFAULT_VALUES.conda_channels
#         else:
#             conda_channels = ''.join('  - '+c+'\n' for c in conda_channels)
#         conda_file = re.sub('{CONDA_CHANNELS}', conda_channels, conda_file)
#
#         print(f'Conda dependencies (default: {DEFAULT_VALUES.conda_deps}) ?')
#         conda_deps = input('>')
#         if conda_deps is None:
#             conda_deps = '[]'
#         else:
#             pass
#         conda_file = re.sub('{CONDA_DEPS}', conda_deps, conda_file)
#
#         with open('conda/env.yaml', 'w') as f:
#             f.write(conda_file)

def main():
    parser = argparse.ArgumentParser(prog='manpy')
    subparsers = parser.add_subparsers()

    parser_gen = subparsers.add_parser('gen', help='gen python package')
    parser_gen.add_argument('pkg_name', help='The name of your package')
    parser_gen.set_defaults(func=_gen_struct)

    parser_distrib = subparsers.add_parser('distrib', help='add distribution tool of your package')
    parser_distrib.add_argument('D', choices=['conda', 'pypi'], help='The chosen distribution tool')

    parser_update = subparsers.add_parser('update', help='update package config')
    parser_update.set_defaults(func=_update)

    args = parser.parse_args()
    args.func(args)


def _gen_struct(_args):
    print('Generating package structure')
    pkg_name = _args.pkg_name
    if os.path.exists('.manpy/'):
        raise FileExistsError(f'Manpy package already generated')
    if os.path.exists('src'):
        raise FileExistsError(f'A directory with the name {pkg_name} already exist')
    if os.path.exists('setup.py'):
        raise FileExistsError(f'A file setup.py already exist')

    os.mkdir("src")
    os.mkdir("src/"+pkg_name)
    with open("src/"+pkg_name+'/__init__.py', 'w') as f:
        version_file = re.sub('{PKG_VER}', '0.0.1', VERSION)
        f.write(version_file)

    os.mkdir('.manpy')
    with open('.manpy/config.ini', 'w') as f:
        config = configparser.ConfigParser()
        config['PACKAGE'] = dict(name=pkg_name,
                                 version='0.0.1',
                                 author='MY_NAME',
                                 author_email='MY_EMAIL',
                                 description='Short description',
                                 long_description='Long description',
                                 url="")
        config.write(f)

    with open('setup.py', 'w') as f:
        setup_file = re.sub('{PKG_NAME}', pkg_name, SETUP)
        setup_file = re.sub('{PKG_VER}', '0.0.1', setup_file)
        setup_file = re.sub('{PKG_AUTH}', 'MY_NAME', setup_file)
        setup_file = re.sub('{PKG_EMAIL}', 'MY_EMAIL', setup_file)
        setup_file = re.sub('{PKG_SHORT_DESC}', 'Short description', setup_file)
        setup_file = re.sub('{PKG_LONG_DESC}', 'Long description', setup_file)
        setup_file = re.sub('{PKG_URL}', '', setup_file)
        f.write(setup_file)


def _update(_args):
    config = configparser.ConfigParser()
    config.read('.manpy/config.ini')

    modify_setup('setup.py', config['PACKAGE'], "    ", '="', '",')
    modify_setup(f"src/{config['PACKAGE']['name']}/__init__.py",
                 {"__version__": config['PACKAGE']['version']},
                 "",
                 ' = "',
                  '"')


