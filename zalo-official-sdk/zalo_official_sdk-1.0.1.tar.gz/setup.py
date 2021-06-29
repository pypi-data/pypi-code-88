# Copyright 2021
import os
import sys
from setuptools import setup, find_packages

this_dir = os.path.dirname(__file__)
readme_filename = os.path.join(this_dir, 'README.md')

PACKAGE_NAME = 'zalo_official_sdk'
PACKAGE_VERSION = '1.0.1'
PACKAGE_AUTHOR = 'Hieutt39'
PACKAGE_AUTHOR_EMAIL = ''
PACKAGE_URL = 'https://github.com/hieutt39/python-zalo-official-sdk'
# PACKAGE_DOWNLOAD_URL = 'https://github.com/hieutt39/python-zalo-official-sdk/tarball/' + PACKAGE_VERSION
PACKAGES = find_packages()

PACKAGE_DATA = {
    'zalo_official': ['*.crt'],
    'zalo_official.test': ['*.jpg']
}
PACKAGE_LICENSE = 'LICENSE'
PACKAGE_DESCRIPTION = 'Zalo Official SDK'
if sys.version_info < (3, 6):
    sys.exit("Python versions less than 3.6 are not supported")
# with open(readme_filename) as f:
#     PACKAGE_LONG_DESCRIPTION = f.read()

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    author=PACKAGE_AUTHOR,
    author_email=PACKAGE_AUTHOR_EMAIL,
    url=PACKAGE_URL,
    # download_url=PACKAGE_DOWNLOAD_URL,
    packages=PACKAGES,
    package_data=PACKAGE_DATA,
    license="GPL-2.0 License",
    description=PACKAGE_DESCRIPTION,
    # long_description=PACKAGE_LONG_DESCRIPTION,
    keywords=['zalo', 'sdk'],
    classifiers=[],
    python_requires=">=3.6",
)
