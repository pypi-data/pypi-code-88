#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from setuptools import setup, find_packages
from pathlib import Path
import speedup_work_lib


# Get long description from relevant file
here = Path(__file__).absolute().parent
with open(here.joinpath('README.md'), 'r', encoding='utf-8') as in_fh:
    long_desc = in_fh.read().replace('`', '')

version = speedup_work_lib.__version__

setup(
    name="speedup_work_lib",
    version=version,
    author="Darren Xie",
    author_email="mndarren@gmail.com",
    description="A Python library to speed up work",
    license="Apache",
    url="https://github.com/mndarren/Speedup-Work-Lib.git",
    packages=find_packages(exclude=["tests", "test*"]),
    include_package_data=True,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    python_require='>=3.9',
    install_requires=[
        'paramiko'
    ],
)
