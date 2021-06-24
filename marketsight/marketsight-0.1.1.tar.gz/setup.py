"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import sys

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

# Get the version number from the VERSION file
version_dict = {}
with open("./marketsight/__version__.py") as version_file:
    exec(version_file.read(), version_dict)  # pylint: disable=W0122

version = version_dict.get("__version__")

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.


setup(
    name="marketsight",  # Required
    version=version,  # Required
    description=("Python bindings for the MarketSight API"),  # Required
    long_description=long_description,
    url="https://marketsight.readthedocs.io/en/latest",  # Optional
    author="MarketSight, LLC",  # Optional
    author_email="support@marketsight.com",  # Optional
    license="MIT",
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 1 - Planning",
        # Indicate who your project is intended for
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=False,
    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords="marketsight cross-tab xtab statistical analysis analytics",  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(exclude=["bravado", "dpath", "validator-collection", "simplejson"]),  # Required
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        "validator-collection>=1.5.0",
        "simplejson>=3.0",
        "bravado>=10.6.0",
        "dpath>=2.0.1"
    ],
    # List additional groups of dependencies here (ENV.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={  # Optional
        "dev": [
            "check-manifest",
            "sphinx",
            "sphinx-rtd-theme",
            "sphinx-tabs",
            "readme-renderer",
            "restview",
            "python-dotenv",
        ],
        "test": [
            "coverage",
            "pytest",
            "pytest-benchmark",
            "pytest-cov",
            "tox",
            "codecov",
            "python-dotenv",
        ],
    },
    python_requires=">=3.0, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",

    include_package_data=True,
    project_urls={  # Optional
        "Documentation": "https://marketsight.readthedocs.io/en/latest",
        "Say Thanks!": "https://saythanks.io/to/marketsight",
        "Bug Reports": "https://github.com/dynata/msight-csl/issues",
        "Source": "https://github.com/dynata/msight-csl/",
    },
)
