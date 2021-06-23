from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.2'
DESCRIPTION = 'Livestockcv'

# Setting up
setup(
    name="helloryan",
    version=VERSION,
    author="Ryan Jeon",
    author_email="<ryanjeon@iastate.edu>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
