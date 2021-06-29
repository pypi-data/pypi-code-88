
from setuptools import setup
from setuptools import find_packages

setup(
    name = 'GooseMPL',
    license = 'MIT',
    author = 'Tom de Geus',
    author_email = 'tom@geus.me',
    description = 'Style and extension functions for matplotlib',
    long_description = 'Style and extension functions for matplotlib',
    keywords = 'matplotlib, style',
    url = 'https://github.com/tdegeus/GooseMPL',
    packages = find_packages(),
    use_scm_version = {'write_to': 'GooseMPL/_version.py'},
    setup_requires = ['setuptools_scm'],
    install_requires = ['matplotlib', 'numpy'],
)
