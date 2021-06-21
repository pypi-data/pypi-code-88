# coding: utf-8

import io
import os
import re
from setuptools import setup, find_packages


def find_version():
    file_dir = os.path.dirname(__file__)
    with io.open(os.path.join(file_dir, 'Approw', 'v2', '__init__.py')) as f:
        version = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read())
        if version:
            return version.group(1)
        else:
            raise RuntimeError("Unable to find version string.")


with io.open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='approw-py-sdk',
    version=find_version(),
    description="Approw SDK for Python",  
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='approw sso AaaS IdaaS',
    author='approw', 
    author_email='info@approw.com',  
    maintainer='approw',
    maintainer_email='info@approw.com',
    url='https://github.com/approw/approw-py-sdk', 
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'gql==2.0.0',
        'graphql-core>=2.3.2,<3',
        'requests',
        'python-dateutil',
        'rsa==4.0'
    ]
)
