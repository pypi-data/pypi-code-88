import setuptools
from setuptools import version
from pathlib import Path

setuptools.setup(
    name="apurbapdf",
    version=1.0,
    long_discription=Path("README.MD").read_text,
    packages=setuptools.find_packages(exclude=["test", "data"])

)
