from dataclasses import dataclass


SETUP = \
'''from setuptools import find_packages, setup

pkgs = find_packages(where="src")

# manpy: start
# Do not edit lines between manpy quotes, use .manpy/config.ini

setup_kwds = dict(
    name="{PKG_NAME}",
    version="{PKG_VER}",
    author="{PKG_AUTH}",
    author_email="{PKG_EMAIL}",
    package_dir={"": "src"},
    packages=pkgs,
    description="{PKG_SHORT_DESC}",
    long_description="{PKG_LONG_DESC}",
    url="{PKG_URL}",
    zip_safe=False
)

# 
# manpy: end

setup(**setup_kwds)'''


CONDA_ENV = \
'''name: {CONDA_NAME}
channels:
{CONDA_CHANNELS}
dependencies: {CONDA_DEPS}

'''

VERSION = \
'''# manpy: start
# Do not edit lines between manpy quotes, use .manpy/config.ini

__version__ = "{PKG_VER}"

# 
# manpy: end
'''


def default_values_pkg(pkg_name: str) -> dict:
    DEFAULT_VALUES = dict(pkg_ver='0.0.1',
                          pkg_author='MY_NAME',
                          pkg_email='MY_EMAIL',
                          conda_name=pkg_name,
                          conda_channels='anaconda',
                          conda_deps='python')
    return DEFAULT_VALUES