#!/usr/bin/env python

import setuptools
from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='GraDiAn',
      version='0.0.0.1',
      description='A grammatical distribution analyser for NLP datasets.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/adamjhawley/GraDiAn",
      classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering"
      ],
      author='Adam Hawley',
      author_email='ajh651@york.ac.uk',
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      python_requires=">=3.6",
     )
