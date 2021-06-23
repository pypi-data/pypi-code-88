#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeisureMan
# email:LeisureMam@gmail.com
# datetime:2021-06-09 14:04
# software: PyCharm

from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
        name = 'protocol_helper',  # 包名
        version = '0.1.6',  # 版本号
        description = 'Common protocol encapsulation classes',
        long_description = long_description,
        author = 'LeisureMan',
        author_email = 'leisuremam@gmail.com',
        url = '',
        install_requires = [
                'requests',
                'python-dotenv',
                'beautifulsoup4',
                'lxml',
                'loguru'
        ],
        license = 'BSD License',
        packages = find_packages(),
        platforms = ["all"],
        classifiers = [
                'Intended Audience :: Developers',
                'Operating System :: OS Independent',
                'Natural Language :: Chinese (Simplified)',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Topic :: Software Development :: Libraries'
        ],

)
