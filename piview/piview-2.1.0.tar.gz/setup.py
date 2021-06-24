#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['psutil']

test_requirements = []

setup(
    author="Adrian Gould",
    author_email='adrian.gould@nmtafe.wa.edu.au',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Open Software License 3.0 (OSL-3.0)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Raspberry Pi System/Hardware Information",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description_content_type="text/markdown",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='piview',
    name='piview',
    packages=find_packages(include=['piview', 'piview.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/AdyGCode/piview',
    version='2.1.0',
    zip_safe=False,
)
