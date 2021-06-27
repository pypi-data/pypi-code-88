#! /usr/bin/env python
from setuptools import find_packages

DESCRIPTION = "Easy data transformation across Python analytics libraries"
LONG_DESCRIPTION = """\
Transformer/xfmr creates a unified interface for transforming data structures
between common forms used in core Python data anlytics libraries like pandas,
scikit-learn, NumPy, SciPy, and Vaex.

xfmr provides:
- Single API and data object that can easily output and keep track of multiple
  data structure formats so that data can be easily passed between different
  analytics libraries
- Methods for transforming data using any one of a number of diffeent libraries
  on the same data object
  
All xfmr wheels distributed on PyPI are BSD 3-clause licensed.
"""

DISTNAME = "xfmr"
MAINTAINER = "Charles Kelley"
MAINTAINER_EMAIL = "cksisu@gmail.com"
URL = "https://xfmr.readthedocs.io.org"
LICENSE = "BSD (3-clause)"
DOWNLOAD_URL = "https://github.com/cksisu/xfmr"
VERSION = "0.0.1.dev0"
PYTHON_REQUIRES = ">=3.7"

INSTALL_REQUIRES = ["scikit-learn>=0.21.0"]

EXTRAS_REQUIRE = {"all": ["vaex>=4.0.0"]}

CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9"]


if __name__ == "__main__":

    from setuptools import setup

    import sys
    if sys.version_info[:2] < (3, 7):
        raise RuntimeError("preso requires python >= {0}.".format(PYTHON_REQUIRES))

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        package_dir={"": "xfmr"},
        packages=find_packages(where="xfmr"),
        classifiers=CLASSIFIERS)

