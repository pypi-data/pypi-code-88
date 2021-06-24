"""
Documentation for setup.py files is at http://setuptools.readthedocs.io/en/latest/setuptools.html
"""

import setuptools

setuptools.setup(name='heaserver-data-adapters',
                 version='1.0.0a10',
                 description='The HEA data adapter service.',
                 url='https://risr.hci.utah.edu',
                 author='Research Informatics Shared Resource, Huntsman Cancer Institute, Salt Lake City, UT',
                 author_email='Andrew.Post@hci.utah.edu',
                 package_dir={'': 'src'},
                 packages=['heaserver.dataadapter'],
                 package_data={'heaserver.dataadapter': ['wstl/*.json']},
                 install_requires=[
                     'heaserver==1.0.0a20'
                 ],
                 entry_points={
                     'console_scripts': [
                         'heaserver-data-adapters = heaserver.dataadapter.service:main'
                     ]
                 }
                 )
