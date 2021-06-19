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

setup(
    name="astralbot",
    author="Nicolas Gargaud <jacen92@gmail.com>",
    license='MIT',
    version=get_version_from_file(),
    packages=find_packages(),
    entry_points={'console_scripts': ['astralbot = src.main:main']},
    zip_safe=False,
    install_requires=[
        "requests>=2.22.0",
        "websocket-client>=0.53.0"
    ]
)
