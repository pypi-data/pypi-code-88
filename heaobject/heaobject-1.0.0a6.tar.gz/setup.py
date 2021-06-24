"""
Documentation for setup.py files is at https://setuptools.readthedocs.io/en/latest/setuptools.html
"""

import setuptools


# Import the README.md file contents
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(name='heaobject',
                 version='1.0.0a6',
                 description='Data and other classes that are passed into and out of HEA REST APIs.',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 url='https://risr.hci.utah.edu',
                 author='Research Informatics Shared Resource, Huntsman Cancer Institute, Salt Lake City, UT',
                 author_email='Andrew.Post@hci.utah.edu',
                 package_dir={'': 'src'},
                 packages=['heaobject'],
                 package_data={'heaobject': ['py.typed']},
                 install_requires=[
                     'python-dateutil~=2.8.1',
                     'yarl~=1.5.1'
                 ]
                 )
