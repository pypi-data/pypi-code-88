#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["numpy>=1.19", "matplotlib>=3.3", "scipy>=1.7"]
dev_requirements = ["pylint", "black", "Sphinx", "sphinx-autobuild"]
dist_requirements = ["twine", "coverage"]
test_requirements = ["pytest>=3", "tox>=3.23"]

setup(
    author="Bionet Lab",
    author_email="",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Python Module for Book 4020",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="compneuro",
    name="compneuro",
    packages=find_packages(include=["compneuro", "compneuro.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    extras_require={
        "dev": dev_requirements,
        "dist": dev_requirements + dist_requirements,
    },
    url="https://github.com/TK-21st/CompNeuro",
    version="0.1.0",
    zip_safe=False,
)
