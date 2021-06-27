#!/bin/bash

from distutils.core import setup

setup(
    name='docker-recreate',
    version='1.0',
    description='Get docker run command from container',
    author='Jeffrey Zhang',
    author_email='zhang.lei.fly@gmail.com',
    url='https://www.python.org/sigs/distutils-sig/',
    entry_points={
        'console_scripts': [
            'docker-recreate=main:main'
        ]},
    py_modules=['main'],
    )
