#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Gabor Parti",
    author_email='partigaborhk@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Sktalk is a Python package that helps processing real-world conversational speech data.",
    entry_points={
        'console_scripts': [
            'sktalk=sktalk.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sktalk',
    name='sktalk',
    packages=find_packages(include=['sktalk', 'sktalk.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/partigabor/sktalk',
    version='0.0.1',
    zip_safe=False,
)
