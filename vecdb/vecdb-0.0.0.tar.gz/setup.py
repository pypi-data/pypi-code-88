import os
from setuptools import setup, find_packages

name = 'vecdb'
version = '0.0.0'

setup(
    name=name,
    version=version,
    author="OnSearch Pty Ltd",
    author_email="dev@vecdb.com",
    description="VecDB",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="VecDB.",
    license="Apache",
    packages=find_packages(exclude=["tests*"]),
    python_requires=">=3",
    #install_requires=['requirements.txt'],
)
