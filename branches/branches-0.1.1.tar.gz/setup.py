import pathlib
from setuptools import setup

from branches import __version__

HERE = pathlib.Path().cwd()
DESCRIPTION = HERE.joinpath("README.md").read_text()
VERSION = __version__


setup(
    name="branches",
    version=VERSION,
    description="A pure-Python replacement for tree",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author="douglas.duhaime@gmail.com",
    author_email="douglas.duhaime@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=["branches"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "branches=branches.__main__:main",
        ]
    },
)
