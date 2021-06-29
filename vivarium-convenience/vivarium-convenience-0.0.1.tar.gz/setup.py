import os
import glob
import setuptools
from distutils.core import setup

with open("README.md", 'r') as readme:
    long_description = readme.read()

setup(
    name='vivarium-convenience',  # TODO: Put your package name here.
    version='0.0.1',
    packages=[
        'vivarium_convenience',
        'vivarium_convenience.processes',
        'vivarium_convenience.composites',
        'vivarium_convenience.experiments',
    ],
    author='Eran Agmon',
    author_email='agmon.eran@gmail.com',
    url='',
    license='MIT',
    entry_points={
        'console_scripts': []},
    short_description='provides a vivarium process with a configurable convenience kinetics',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={},
    include_package_data=True,
    install_requires=[
        'vivarium-core>=0.3.0',
        'vivarium-multibody',
        'pytest',
    ],
)
