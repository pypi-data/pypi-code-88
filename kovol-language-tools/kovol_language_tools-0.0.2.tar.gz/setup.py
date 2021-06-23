import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="kovol_language_tools",
    version="0.0.2",
    description="Classes and functions for manipulating data in the Kovol langauge of Papua New Guinea.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/stevetasticsteve/kovol-language-tools",
    author="Steve Stanley",
    author_email="stevetasticsteve@gmail.com",
    license="GNU GPLv3 ",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["kovol_language_tools"],
    include_package_data=True,
    install_requires=["tabulate",],
)

