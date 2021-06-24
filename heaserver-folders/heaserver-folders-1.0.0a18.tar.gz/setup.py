"""
Documentation for setup.py files is at http://setuptools.readthedocs.io/en/latest/setuptools.html
"""

import setuptools

setuptools.setup(name='heaserver-folders',
                 version='1.0.0a18',
                 description='The HEA folder service.',
                 url='https://risr.hci.utah.edu',
                 author='Research Informatics Shared Resource, Huntsman Cancer Institute, Salt Lake City, UT',
                 author_email='Andrew.Post@hci.utah.edu',
                 package_dir={'': 'src'},
                 packages=['heaserver.folder'],
                 package_data={'heaserver.folder': ['wstl/*.json']},
                 install_requires=[
                     'heaserver==1.0.0a20'
                 ],
                 entry_points={
                     'console_scripts': [
                         'heaserver-folders = heaserver.folder.service:main'
                     ]
                 }
                 )
