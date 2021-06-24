"""
Documentation for setup.py files is at http://setuptools.readthedocs.io/en/latest/setuptools.html
"""

import setuptools

setuptools.setup(name='heaserver-registry',
                 version='1.0.0a8',
                 description='The HEA registry service.',
                 url='https://risr.hci.utah.edu',
                 author='Research Informatics Shared Resource, Huntsman Cancer Institute, Salt Lake City, UT',
                 author_email='Andrew.Post@hci.utah.edu',
                 package_dir={'': 'src'},
                 packages=['heaserver.registry'],
                 package_data={'heaserver.registry': ['wstl/*.json']},
                 install_requires=[
                     'heaserver==1.0.0a20'
                 ],
                 entry_points={
                     'console_scripts': [
                         'heaserver-registry = heaserver.registry.service:main'
                     ]
                 }
                 )
