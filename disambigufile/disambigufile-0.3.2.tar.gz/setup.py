#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Brendan Strejcek",
    author_email='brendan@datagazing.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Class with file-like interface to a file found in provided search path",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='disambigufile',
    name='disambigufile',
    packages=find_packages(include=['disambigufile', 'disambigufile.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/datagazing/disambigufile',
    version='0.3.2',
    zip_safe=False,
)
