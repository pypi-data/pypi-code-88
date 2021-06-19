#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

from setuptools import setup, find_packages
import os

def get_version_from_file():
    """ Read the file and return the value """
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'VERSION')) as version_file:
        version = version_file.read().strip()
    return version

def get_readme_from_file():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'README.md')) as readme_file:
        readme = readme_file.read()
    return readme

setup(
    name="astralbot",
    author="Nicolas Gargaud <jacen92@gmail.com>",
    url="https://github.com/AstralBotAI/AstralBot-py",
    description="Library to interact with an astralBot instance.",
    version=get_version_from_file(),
    packages=find_packages(),
    long_description=get_readme_from_file(),
    long_description_content_type="text/markdown",
    entry_points={'console_scripts': ['astralbot = src.main:main']},
    license='MIT',
    zip_safe=False,
    install_requires=[
        "requests>=2.22.0",
        "websocket-client>=0.53.0"
    ],
    classifiers=[
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Games/Entertainment :: Simulation",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
)
