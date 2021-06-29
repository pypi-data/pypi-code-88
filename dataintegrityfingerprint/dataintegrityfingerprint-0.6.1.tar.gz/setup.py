#!/usr/bin/env python3
"""
Installer
"""

from setuptools import setup
import codecs
import os
from dataintegrityfingerprint import PACKAGE_NAME

application_name = PACKAGE_NAME
install_requires = []
entry_points = {'console_scripts':
                ['{}={}.__main__:run'.format(application_name, PACKAGE_NAME)]}
repository = "https://github.com/expyriment/dataintegrityfingerprint-python"

def readme():
    directory = os.path.dirname(os.path.join(
        os.getcwd(), __file__, ))
    with codecs.open(
        os.path.join(directory, "README.md"),
        encoding="utf8",
        mode="r",
        errors="replace",
        ) as file:
        return file.read()


def get_version(package):
    """Get version number"""

    with open(os.path.join(package, "__init__.py")) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("'")[1]
    return "None"


if __name__ == '__main__':
    setup(
        name = PACKAGE_NAME,
        version=get_version(PACKAGE_NAME),
        description='Create a Data Integrity Fingerprint',
        author='Oliver Lindemann, Florian Krause',
        author_email='oliver@expyriment.org, florian@expyriment.org',
        license='MIT Licence',
        url=repository,
        packages=[PACKAGE_NAME],
        include_package_data=False,
        setup_requires=[],
        install_requires=install_requires,
        entry_points=entry_points,
        keywords = "", #ToDo
        classifiers=[ #ToDO
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Topic :: Scientific/Engineering"
        ],
        long_description=readme(),
        long_description_content_type='text/markdown'
    )
