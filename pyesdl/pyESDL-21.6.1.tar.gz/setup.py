# from distutils.core import setup
import sys
import unittest

import versioneer
import setuptools

version = tuple(sys.version_info[:2])

if version < (3, 7):
    sys.exit('pyESDL requires at least Python >= 3.7')


def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='*_test.py')
    return test_suite


setuptools.setup(
    name='pyESDL',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    # package_dir = {'': 'heatmatcher'},
    url="https://energytransition.gitbook.io/esdl/",
    # packages=['agents', 'bid', 'configurator',
    #           'data_provider', 'observation_framework', 'orchestrator', 'visualisation', 'version'],
    # packages=['heatmatcher', 'esdl', 'heatmatcher.agents', 'heatmatcher.bid', 'heatmatcher.configurator',
    #           'heatmatcher.data_provider', 'heatmatcher.observation_framework', 'heatmatcher.orchestrator',
    #           'heatmatcher.visualisation', 'heatmatcher.version'],
    packages=setuptools.find_packages(),
    # py_modules=['heatmatcher.heatmatcher'],
    package_data={'': ['README.md', 'LICENSE.md']},
    include_package_data=True,
    license='Apache 2.0',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    description="Python implementation of the Energy System Description Language (ESDL) for modelling Energy systems",
    author='Ewoud Werkman',
    author_email='ewoud.werkman@tno.nl',
    python_requires='>=3.7',
    install_requires=[
        'pyecore>=0.12.0'
    ],
    test_suite='setup.my_test_suite'
)
