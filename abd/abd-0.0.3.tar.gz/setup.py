#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# setup.py

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'abd'
DESCRIPTION = 'Abstract base class for decorators'
URL = 'https://github.com/w13b3/abstract_base_decorator'
EMAIL = 'wiebe@email.xom'
AUTHOR = 'wiebe'
REQUIRES_PYTHON = '>=3.6.0, <4'
VERSION = '0.0.3'
# If you do change the License, remember to change the Trove Classifier for that!
LICENSE = "Mozilla Public License Version 2.0"

# If your package is a single module, use this instead of 'packages':
PY_MODULES = [
    'abd'
]

# What packages are required for this module to be executed?
REQUIRED = [
    # None
]

# What packages are optional?
EXTRAS = {
    # None
}
# Trove Classifiers
CLASSIFIERS = [  # https://pypi.org/classifiers/
    "Development Status :: 2 - Pre-Alpha",
    "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3 :: Only",
    "Typing :: Typed",
    "Intended Audience :: Developers",
    "Topic :: Software Development",
    "Topic :: Software Development :: Build Tools",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
keywords = ["decorator abstract oop"],

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class CreateCommand(Command):
    """Support setup.py create."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…\n')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))
        self.status("\nReady to upload to PyPI.")

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=[
        "test",  "*.test",  "*.test.*",  "test.*",
        "tests", "*.tests", "*.tests.*", "tests.*",
    ]),
    py_modules=PY_MODULES,
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    # $ setup.py publish support.
    cmdclass={
        'create': CreateCommand,
    },
)
