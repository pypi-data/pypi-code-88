import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Requirements
with open('requirements.txt') as f:
    required = f.read().splitlines()
    required.remove("pytest")
    required.remove("pytest-mock")

# This call to setup() does all the work
setup(
    name="leveropen",
    version="0.0.1",
    description="Python wrapper for Lever Open API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://leveropen.readthedocs.io/en/latest/",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=required,
    tests_require=["pytest", "pytest-mock"],
    download_url="https://github.com/n-n-s/leveropen"
)
