"""
Documentation for setup.py files is at https://setuptools.readthedocs.io/en/latest/setuptools.html
"""

from setuptools import setup, find_namespace_packages


# Import the README.md file contents
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='heaserver',
      version='1.0.0a21',
      description='The server side of HEA.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://risr.hci.utah.edu',
      author='Research Informatics Shared Resource, Huntsman Cancer Institute, Salt Lake City, UT',
      author_email='Andrew.Post@hci.utah.edu',
      package_dir={'': 'src'},
      packages=find_namespace_packages(where='src'),
      package_data={'heaserver.service': ['py.typed']},
      install_requires=[
          'heaobject==1.0.0a5',
          'aiohttp[speedups]~=3.6.2',
          'aiohttp-remotes~=0.1.2',
          'motor~=2.1.0',
          'pytz~=2020.1',
          'tzlocal~=2.0.0',
          'uritemplate~=3.0.1',
          'accept-types~=0.4.1',
          'mongoquery~=1.3.6',
          'jsonschema~=3.2.0',
          'jsonmerge~=1.7.0'
      ]
      )
