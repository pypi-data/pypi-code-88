import pathlib
from setuptools import setup
import pkg_resources

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
# README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="profitmart",
    version="0.1.11",
    description="Profitmart APIs",
    # long_description=README,
    # long_description_content_type="text/markdown",
    # url="https://github.com/realpython/reader",
    author="Sumit Pratihar",
    author_email="timusp7@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["."],
    include_package_data=True,
    install_requires=["certifi","cffi","chardet","cryptography","idna","pycparser","requests","urllib3"],
    entry_points={
        "console_scripts": [
            "profitmart=profitmart.__main__:main",
        ]
    },
)