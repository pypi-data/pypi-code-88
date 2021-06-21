#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
  requirements = fh.read()

setuptools.setup(
    name='wp_dso_publish',
    version='0.30',
    packages=[
        'wp_dso_publish'
    ],
    package_dir={'wp_dso_publish': 'wp_dso_publish/'},
    package_data={'wp_dso_publish': ['style.css', 'local_settings.py']},
    scripts=['wp-dso-publish.py'],
    url='https://github.com/RENCI-NRIG/impact-utils/tree/master/wp_dso_publish',
    license='MIT',
    long_description=long_description,
    author='ibaldin',
    author_email='ibaldin@renci.org',
    description='Utility to push SAFE policies for a specific dataset.',
    classifiers=[
	    "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    setup_requires=requirements,
)
