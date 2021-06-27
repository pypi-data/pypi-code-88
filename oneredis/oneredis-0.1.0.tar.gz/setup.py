from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="oneredis",
    version="0.1.0",
    author="onebula",
    author_email="",
    description="Fast, simple, safe python wrapper for redis.",
    license="MIT",
    url="https://github.com/onebula/oneredis",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
            'ciso8601>=2.0.0',
            'redis>=3.5.0',
            'orjson'
    ],
    zip_safe=True,
)