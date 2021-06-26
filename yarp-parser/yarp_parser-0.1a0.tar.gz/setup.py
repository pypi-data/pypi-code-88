#!/usr/bin/env python

from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='yarp_parser',
      version='0.1-alpha',
      description='YARP - Yet Another Recursive Parser.',
      author='Eric Wimberley',
      packages=['yarp_parser'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/ewimberley/yarp",
      project_urls={
          "Bug Tracker": "https://github.com/ewimberley/yarp/issues",
      },
      python_requires=">=3.6",
      )
