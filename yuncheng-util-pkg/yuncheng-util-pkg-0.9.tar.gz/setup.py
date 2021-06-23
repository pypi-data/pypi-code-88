#!/usr/bin/python
# encoding: utf-8
from setuptools import setup, find_packages

setup(
    name="yuncheng-util-pkg",
    version="0.9",
    url="https://e.coding.net/yuncheng/yuncheng-python-package/python-util.git",
    author="wangwei",
    author_email="wangwei@ikangtai.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    platforms="any",
    install_requires=["requests>=2.20.0","matplotlib","opencv-python"],
    python_requires=">=3.6",
)