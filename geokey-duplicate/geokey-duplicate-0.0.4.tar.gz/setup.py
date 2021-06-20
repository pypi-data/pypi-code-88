#!/usr/bin/env python

from os.path import dirname, join
from setuptools import setup, find_packages


def read(file_name):
    with open(join(dirname(__file__), file_name)) as file_object:
        return file_object.read()


name = 'geokey-duplicate'
version = __import__(name.replace('-', '_')).__version__
repository = join('https://github.com/ExCiteS', name)

setup(
    name=name,
    version=version,
    description='Duplicate projects and categories',
    long_description=read('README.rst'),
    url=repository,
    download_url=join(repository, 'tarball', version),
    author='Francisco Sanz',
    author_email='frasanz@bifi.es',
    license='MIT',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*']),
    include_package_data=True,
)
