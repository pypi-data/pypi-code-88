from setuptools import setup, find_packages


import argteller

VERSION = argteller.__version__

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
	name="argteller", 
	version=VERSION,
	author="Jay Kim",
	description="Decorator for stylized interactive constructor using DSL and parser.",
	long_description=long_description,
	long_description_content_type="text/x-rst",
	url="https://github.com/mozjay0619/argteller",
	license="DSB 3-clause",
	packages=find_packages(),
	#install_requires=["numpy>=1.18.2", "pandas>=0.25.3", "psutil>=5.7.0"]
	)