#!/usr/bin/env python
from setuptools import setup

NAME = "testypie"
setup(
    name=NAME,
    use_scm_version={
        "local_scheme": "dirty-tag",
        "write_to": f"{NAME}/_version.py",
        "fallback_version": "0.0.0",
    },
    author="Ross Fenning",
    author_email="github@rossfenning.co.uk",
    packages=[NAME],
    package_data={NAME: ["py.typed"]},
    url="https://github.com/avengerpenguin/testypie",
    description="HTTP proxy that generates and loads from fixtures for testing.",
    license="GPLv3+",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    install_requires=[
        "Flask",
        "requests",
        "httplib2",
        "PyYAML",
        "clize",
    ],
    setup_requires=[
        "setuptools_scm>=3.3.1",
        "pre-commit",
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-mypy",
            "pytest-pikachu",
            "types-requests",
            "types-Flask",
            "types-PyYAML",
            "types-Werkzeug",
        ],
    },
    entry_points={
        "console_scripts": [
            "testypie = testypie:cli",
        ],
    },
)
