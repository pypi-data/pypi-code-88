from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name="gfunction-auth",
    version="0.0.4",
    author="Andrew Dircks",
    author_email="abd93@cornell.edu",
    description="A lightweight package for makeing authorized requests to Google Cloud Functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrewdircks/gfunctions-auth",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    install_requires=['requests', 'google-auth','google-oauth'],
    packages=['gfunction_auth'],
    python_requires=">=3.7",
)