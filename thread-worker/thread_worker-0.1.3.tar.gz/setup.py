#!/usr/bin/python
# coding=utf-8
'''
Date: 2021-06-24 17:56:20
LastEditors: recar
LastEditTime: 2021-06-24 18:33:11
'''
from setuptools import setup
from os import path as os_path


this_directory = os_path.abspath(os_path.dirname(__file__))
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

setup(name='thread_worker',  
      version='0.1.3',
      author='recar',
      author_email='recar@recar.com',
      long_description=read_file('README.md'),
      long_description_content_type="text/markdown",
      description='thread work',
      url='https://github.com/Ciyfly/thread_work',
      packages=['thread_worker'],
      install_requires=[],
      zip_safe=False)
