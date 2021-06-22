from setuptools import setup, find_packages

import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="webstaterator",
    version="0.3.1",
    packages=find_packages(),
    install_requires=["jinja2 >= '2.11.2'"],
    author='Jon Keatley',
    keywords='website static web pages generator',
    description='A Python tool for generating static websites based on object models',
    url='https://gitlab.com/Jon.Keatley.Folio/webstaterator',
    project_urls={'Source Code':'https://gitlab.com/Jon.Keatley.Folio/webstaterator'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.5',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={'console_scripts':[
     'webstaterator = webstaterator.__main__:execute']},
)
