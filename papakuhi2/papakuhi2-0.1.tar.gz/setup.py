from setuptools import setup, find_packages
import numpy

setup(
    name='papakuhi2',
    version='0.1',
    include_dirs=[numpy.get_include()],
    packages=find_packages(),
    package_data = {"papakuhi2": ["data/*.dat"],
    }
)
 