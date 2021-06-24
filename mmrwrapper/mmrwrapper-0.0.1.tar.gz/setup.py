from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'API-Wrapper WhatIsMyMMR'
LONG_DESCRIPTION = 'All rights reserved to the creator of the Website. https://euw.whatismymmr.com/ - Email: josh@whatismymmr.com'

# Setting up
setup(
    name="mmrwrapper",
    version=VERSION,
    author="Sunta",
    author_email="noneofyour@business.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
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