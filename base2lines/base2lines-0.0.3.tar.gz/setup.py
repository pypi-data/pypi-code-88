from setuptools import setup, find_packages
import codecs
import os



VERSION = '0.0.3'
DESCRIPTION = 'a python package to benchmarks algorithms against various datasets'


# Setting up
setup(
    name="base2lines",
    version=VERSION,
    author="Vishwas",
    author_email="vishwasgoyal47@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[],
    # package_dir={'':'baseline'},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)