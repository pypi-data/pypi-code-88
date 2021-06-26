from io import open
from setuptools import find_packages, setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="deploymenthub",
    version=1.3,
    description='A CLI client for deployment-hub server.',
    license='MIT',
    author='Jared Wines',
    author_email='contact@jaredwines.com',
    url='https://github.com/jaredwines/deployment-hub-cli-client',
    packages=find_packages(exclude=['tests']),
    scripts=['bin/deploymenthub'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
