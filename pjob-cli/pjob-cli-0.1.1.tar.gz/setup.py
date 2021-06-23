#!/usr/bin/python
# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name="pjob-cli",
    version="0.1.1",
    license="MIT Licence",
    url="https://github.com/ChenJiangxu/pjob-cli",
    author="Joncy",
    author_email="chenjiangxu@foxmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['requests']
)
