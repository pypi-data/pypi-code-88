from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.3'
DESCRIPTION = 'API-Wrapper WhatIsMyMMR'
LONG_DESCRIPTION = '''

Simple-Async API Wrapper for WhatIsMyMMR Website (League of Legends)

Creator-Attribution:

Title: WhatIsMyMMR

Creator: Josh Kross / josh@whatismymmr.com

Source: https://euw.whatismymmr.com/ / https://dev.whatismymmr.com/

License: https://creativecommons.org/licenses/by/4.0/



'''

# Setting up
setup(
    name="mmrwrapper",
    version=VERSION,
    author="Sunta",
    author_email="noneofyour@business.com",
    license_files = ('LICENSE',),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['asyncio', 'aiohttp', 'datetime', 'functools'],
    keywords=['python', 'api', 'wrapper'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)