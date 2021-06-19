#!/usr/bin/env python

import sys
import setuptools
from distutils.core import setup

dependencies = ['dendropy==4.4.0']

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(name = "fishlifetraits",
      version = '0.2.1',
      maintainer = 'Ulises Rosas',
      long_description = readme,
      long_description_content_type = 'text/markdown',
      packages = ['fishlifetraits'],
      install_requires = dependencies,
      zip_safe = False,
      classifiers = [
          'Programming Language :: Python :: 3'
      ]
)