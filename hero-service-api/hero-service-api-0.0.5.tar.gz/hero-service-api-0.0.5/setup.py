'''to be filled'''
from setuptools import find_packages
from setuptools import setuptools

setuptools.setup(name="hero-service-api", version="0.0.5", author="Harold Carter", description="A library for providing the angular app tour of heroes with a remote service.", url="http://ccvmgit/Harold.Carter/hero-service-api/edit", packages=find_packages(include=('hero_api*'), exclude=('tests*', 'reports*', 'gradle*', 'build*', '.vscode*', '.gradle*')), python_requires='>=3.6')
