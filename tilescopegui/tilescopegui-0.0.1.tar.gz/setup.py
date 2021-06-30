#!/usr/bin/env python
import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8").read()


def get_version():
    with open("tilescopegui/__init__.py", encoding="utf-8") as init_file:
        for line in init_file.readlines():
            if line.startswith("__version__"):
                return line.split(" = ")[1].rstrip()[1:-1]
    raise ValueError("Version not found in tilescopegui/__init__.py")


setup(
    name="tilescopegui",
    version=get_version(),
    author="Permuta Triangle",
    author_email="permutatriangle@gmail.com",
    description="A graphical user interface for TileScope.",
    license="GPLv3",
    keywords=("gui permutation tiling tilescope flask"),
    url="https://github.com/PermutaTriangle/TileScopeGUI",
    project_urls={
        "Source": "https://github.com/PermutaTriangle/TileScopeGUI",
        "Tracker": "https://github.com/PermutaTriangle/TileScopeGUI/issues",
    },
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    long_description_content_type="text/x-rst",
    long_description=read("README.rst"),
    install_requires=["tilings==3.0.0", "Flask==2.0.0", "Flask-Cors==3.0.10"],
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    entry_points={"console_scripts": ["tilescopegui=tilescopegui.main:main"]},
)
