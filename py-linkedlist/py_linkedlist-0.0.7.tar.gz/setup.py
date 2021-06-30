from setuptools import setup, find_packages

import os

VERSION = '0.0.7'
DESCRIPTION = "LinkedList Package"

#Setting up
setup(
    name="py_linkedlist",
    version=VERSION,
    author="Rajesh Kumar Patnala",
    author_email="patnala04@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'dsa', 'data structures', 'linkedlist', 'linked list', 'algorithms'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
),

