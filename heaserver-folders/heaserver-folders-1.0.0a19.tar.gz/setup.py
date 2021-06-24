"""
Documentation for setup.py files is at https://setuptools.readthedocs.io/en/latest/setuptools.html
"""

import setuptools

# Import the README.md file contents
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(name='heaserver-folders',
                 version='1.0.0a19',
                 description='The HEA folder service.',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 url='https://risr.hci.utah.edu',
                 author='Research Informatics Shared Resource, Huntsman Cancer Institute, Salt Lake City, UT',
                 author_email='Andrew.Post@hci.utah.edu',
                 package_dir={'': 'src'},
                 packages=['heaserver.folder'],
                 package_data={'heaserver.folder': ['wstl/*.json']},
                 install_requires=[
                     'heaserver==1.0.0a21'
                 ],
                 entry_points={
                     'console_scripts': [
                         'heaserver-folders = heaserver.folder.service:main'
                     ]
                 }
                 )
