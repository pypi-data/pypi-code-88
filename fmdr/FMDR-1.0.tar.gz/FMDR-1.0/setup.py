#!/usr/bin/env python
import setuptools
from setuptools import setup, find_packages

setup(
    name='FMDR',
    version='1.0',
    description='Find drivers on linux',
    author='strotic',
    author_email='strotic@protonmail.com',
    url='https://github.com/strotic/fmdr',
    packages=find_packages(include=['fmdr', 'fmdr.*'])
     )