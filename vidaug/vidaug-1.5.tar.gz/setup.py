import setuptools

import pathlib
import sys
from distutils.core import setup
from os import path

import setuptools
from setuptools import setup

version_name = sys.argv[1].replace("refs/tags/", "")
del sys.argv[1]

setuptools.setup(name='vidaug',
                 version=version_name,
                 description='Video Augmentation Library',
                 url='https://github.com/okankop/vidaug',
                 author='Okan Kopuklu',
                 author_email='okankopuklu@gmail.com',
                 license='MIT',
                 packages=setuptools.find_packages(),
                 zip_safe=False)
