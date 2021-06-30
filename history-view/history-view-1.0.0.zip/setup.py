from setuptools import setup, find_packages
import os
from io import open

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="history-view",
    version="1.0.0",
    description="A tiny python application that abstracts viewing/interacting with your console history.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/semick-dev/history-view",
    author="semick-dev",
    author_email="sbeddall@gmail.com",
    license="MIT License",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(exclude=["tests"]),
    install_requires=["jinja2", "pyperclip"],
    project_urls={
        "Bug Reports": "https://github.com/semick-dev/history-view/issues",
        "Source": "https://github.com/semick-dev/history-view",
    },
    entry_points={"console_scripts": ["hv=hv:console_entry"]},
)
