
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="JoeLiu-RF Refactoring",
    version="1.0.8",
    author="Joe Liu&GeneWu",
    author_email="qq555520qq@gmail.com",
    description="RF Refactoring package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoeLiu1321/RF-Refactoring",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['robotframework']
)