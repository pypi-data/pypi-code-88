# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='timench',
    version='0.2.0',
    packages=['timench', ],
    url='https://github.com/ndrwpvlv/timench',
    license='MIT',
    author='Andrei S. Pavlov',
    author_email='ndrw.pvlv@gmail.com',
    description='Timench is a small framework for measure execution time of one function, multiple functions and code',
    download_url='https://github.com/ndrwpvlv/timench/archive/refs/tags/0.2.0.tar.gz',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['time', 'measure execution time', 'measure time', ],

    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
