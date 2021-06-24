from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.2'
DESCRIPTION = 'API-Wrapper WhatIsMyMMR'
LONG_DESCRIPTION = 'All rights reserved to the creator of the Website. https://euw.whatismymmr.com/ - Email: josh@whatismymmr.com'

# Setting up
setup(
    name="mmrwrapper",
    version=VERSION,
    author="Sunta",
    author_email="noneofyour@business.com",
    license_files = ('LICENSE.txt',),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['asyncio', 'aiohttp', 'datetime', 'functools'],
    keywords=['python', 'api', 'wrapper'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)