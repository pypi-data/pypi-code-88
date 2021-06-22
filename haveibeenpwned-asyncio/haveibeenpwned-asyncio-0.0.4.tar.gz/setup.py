#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
from setuptools import setup, find_packages
import codecs

from haveibeenpwned_asyncio import __version__

scripts = glob.glob("bin/*")
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


curr_dir = os.path.abspath(os.path.dirname(__file__))

long_description = (long_description,)
long_description_content_type = "text/markdown"

with codecs.open(os.path.join(curr_dir, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()

tests_require = [
    "pytest",
    "pytest-cov",
    "codecov",
    "flake8",
    "black",
    "bandit",
    "pytest-runner",
    "python-dateutil",
    "aioresponses",
    "pytest-asyncio",
    "asynctest",
    "pytest-mock"
]

setup(
    name="haveibeenpwned-asyncio",
    version=__version__,
    description="Asyncio and aiohttp based library and CLI to connect to haveibeenpwned.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c-goosen/haveibeenpwned-asyncio",
    author="Christo Goosen",
    author_email="christogoosen@gmail.com",
    python_requires=">=3.5.0",
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Typing :: Typed",
    ],
    keywords="South Africa ID Number",
    packages=find_packages(
        include=["haveibeenpwned_async", "haveibeenpwned_async", "bin/*"],
        exclude=["docs", "docs-src", "tests", "tests.*", "tutorial"],
    ),
    setup_requires=["aiohttp", "setuptools", "click"],
    install_requires=["aiohttp", "click"],
    test_suite="tests",
    tests_require=tests_require,
    extras_require={"dev": ["bandit", "black", "flake8"] + tests_require},
    scripts=scripts,
    zip_safe=True,
)
