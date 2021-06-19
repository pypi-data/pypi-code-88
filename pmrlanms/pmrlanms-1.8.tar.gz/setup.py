#! /usr/bin/env python3
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import os
import subprocess

import setuptools
from setuptools.dist import Distribution


# This is a hack around python wheels not including the adaptor.so library.
class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

    def has_ext_modules(self):
        return True


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

if subprocess.call(['make', '--always-make','-C', BASE_DIR]) != 0:
    raise RuntimeError('Cannot compile lanms in the directory: {}'.format(BASE_DIR))

setuptools.setup(
    name='pmrlanms',

    version='1.8',

    description='Locality-Aware Non-Maximum Suppression for PMR',

    # The project's main homepage.
    url='https://github.com/Parquery/lanms',

    # Author details
    author='argmen (boostczc@gmail.com) is code author, '
           'Dominik Walder (dominik.walder@parquery.com) and Marko Ristin (marko@parquery.com) only packaged the code' 'Yash Bhambhu(basyambhu@gmail.com) packaged for other versions',
    author_email='basyambhu@gmail.com',

    # Choose your license
    license='GNU General Public License v3.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent'
    ],

    keywords='locality aware non-maximum suppression',

    packages=setuptools.find_packages(exclude=[]),

   

    include_package_data=True,
    distclass=BinaryDistribution,
    python_requires='==3.8.*',
)
