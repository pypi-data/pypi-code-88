import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gfunction-auth",
    version="0.0.2",
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
    packages=setuptools.find_packages(where="gfunction_auth"),
    python_requires=">=3.7",
)