#!/usr/bin/env python
# coding: utf-8
from setuptools import setup
setup(
    name='barwet',
    version='0.0.6',
    author='barwe',
    author_email='barwechin@163.com',
    url='https://pypi.org/project/barwet/',
    description='',
    packages=[
        'barwet', 
        'barwet.bio', 
        'barwet.algo.stringMatch'
    ],
    install_requires=[],
    # entry_points={
    #     'console_scripts': [
    #         'jujube=jujube_pill:jujube',
    #         'pill=jujube_pill:pill'
    #     ]
    # }
)