#!/usr/bin/env python3
from setuptools import setup

setup(
    name = "goo-pm",
    description = "Plugin/dependency manager for Godot",
    version = "1.0.0",
    author = "nanom",
    packages = ["goo"],
    entry_points = {
        "console_scripts": [
            "goo = goo.goo:__main__",
        ]
    },
    url = "https://gitlab.com/nanom_/goo",
    license = "0BSD",
    install_requires = [
        "click",
        "validators",
        "requests",
        "gitpython",
        "beautifulsoup4",
    ],
    keywords = "godot package manager plugin plugins gd python",
    python_requires = ">=3.0",
)
