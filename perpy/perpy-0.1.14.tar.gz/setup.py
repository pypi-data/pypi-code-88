#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import setuptools
import os
import io

DESCRIPTION = "Functions commonly used in computer paper writing and scientific research."

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION



setuptools.setup(
    name = 'perpy',
    version = '0.1.14',
    author = 'Yongbiao Li',
    author_email = "yongbiaoli@yeah.net", #邮箱
    description = DESCRIPTION, #描述
    long_description = long_description, #描述
    long_description_content_type="text/markdown", #markdown
    url="https://github.com/Very-Handsome9/perpy.git", #github地址
    packages=setuptools.find_packages(),
    license = 'MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", #License
        "Operating System :: OS Independent",
    ],
    install_requires=['sklearn','numpy','matplotlib'],
    python_requires='>=3.0',  #支持python版本
)