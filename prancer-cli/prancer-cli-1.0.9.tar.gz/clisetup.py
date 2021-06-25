"""A setup module for prancer-enterprise cli."""


# setuptools for distribution
from setuptools import find_packages, setup
from entcli import cli_enterprise
import os

with open('clirequirements.txt') as f:
    required = f.read().splitlines()

LONG_DESCRIPTION = """
 Prancer Enterprise CLI allows to users to run cloud validation using
 web APIs.  The supported cloud frameworks are azure, aws and git.
"""

setup(
    name='prancer-cli',
    version='1.0.9',
    description='Prancer CLI, http://prancer.io/',
    long_description=LONG_DESCRIPTION,
    license = "Propietary",
    # The project's main homepage.
    url='https://ebizframework.visualstudio.com/whitekite',
    # Author(s) details
    author='Farshid M/Ajey Khanapuri',
    author_email='ajey.khanapuri@liquware.com',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "License :: OSI Approved :: BSD License",
    ],
    packages=find_packages(where="entcli",
                           exclude=['adv', 'log', 'rundata', 'utilities', 'tests']),
    include_package_data=True,
    package_dir={'': 'entcli'},
    install_requires=required,
    python_requires='>=3.0',
    entry_points={
        'console_scripts': [
            'prutil = cli_enterprise.entcli.cli:run_cli'
        ],
    }
)

