#!/usr/bin/env python
from setuptools import setup, find_packages
import os
import sys

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(name='junitmgr',
      version="1.0.3",
      description='Manages Surefire XML (JUnit) XML files, especially huge files,, for generating reports.',
      long_description="JUnit Manager",
      url='https://github.com/h20dragon/junitmgr.git',
      author='H20Dragon',
      author_email='h20dragon@outlook.com',
      license='Apache 2.0',
      install_requires=['future', 'junitparser', 'lxml'],
      keywords='junit surefire nunit xunit xml parser h20dragon',
      packages=find_packages(exclude=["tests"]),
      scripts=['bin/junitmgr'],
      zip_safe=False)
