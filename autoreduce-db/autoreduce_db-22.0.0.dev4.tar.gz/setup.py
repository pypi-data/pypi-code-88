# pylint:skip-file
"""
Wrapper for the functionality for various installation and project setup commands
see:
    `python setup.py help`
for more details
"""
from os import path
from setuptools import setup, find_packages

# read the contents of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='autoreduce_db',
      version='22.0.0.dev4',
      description='ISIS Autoreduce',
      author='ISIS Autoreduction Team',
      url='https://github.com/ISISScientificComputing/autoreduce-db/',
      install_requires=['autoreduce-utils==22.0.0.dev3', 'Django==3.2.4'],
      packages=find_packages(),
      long_description=long_description,
      long_description_content_type='text/markdown')
