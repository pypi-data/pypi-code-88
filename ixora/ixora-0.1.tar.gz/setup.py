#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(
    name='ixora',
    author='QeeqBox',
    author_email='gigaqeeq@gmail.com',
    description="Automate force-directed graph",
    long_description=long_description,
    version='0.1',
    license='AGPL-3.0',
    url='https://github.com/qeeqbox/ixora',
    packages=['ixora'],
    include_package_data=True,
    entry_points={'console_scripts': ['ixora = ixora.__main__:main']},
    install_requires=['termcolor'],
    python_requires='>=3',
    )
