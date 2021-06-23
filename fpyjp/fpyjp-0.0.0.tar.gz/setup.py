#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='fpyjp',
    version='0.0.0',
    packages=find_packages(),
    description='',
    author='well-living',
    license='MIT',
    classfiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=['pandas', 'requests'],
)
