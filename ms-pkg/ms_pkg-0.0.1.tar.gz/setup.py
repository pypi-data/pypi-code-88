import setuptools
from setuptools import version

setuptools.setup(
    name = 'ms_pkg',
    version = '0.0.1',
    description = 'My first PyPI package',
    packages = setuptools.find_packages(),
)