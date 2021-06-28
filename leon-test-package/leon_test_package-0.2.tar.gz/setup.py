# -*- coding: utf-8 -*-
"""
Created by Leon at 6/28/2021

"""
__author__ = "Leon"
__version__ = "0.0.1"
__email__ = "yang.li@zillnk.com"
from setuptools import setup

setup(name='leon_test_package',
      version='0.2',
      description='The funniest joke in the world',
      url='http://github.com/yangli0534/leon_test_package',
      author='yangli0534',
      author_email='yangli0534@yahoo.com',
      license='MIT',
      packages=['leon_test_package'],
      zip_safe=False,
      username='yangli0534',
      package_dir={'leon_test_package':'leon_test_package'},
      package_data={'leon_test_package':['*.*', 'leon_test_package/*']})