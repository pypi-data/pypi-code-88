import os
from importlib_metadata import version, PackageNotFoundError

# try fetching version, if it fails (usually when in dev), add default
try:
    BIOLIB_PACKAGE_VERSION = version('pybiolib')
except PackageNotFoundError:
    BIOLIB_PACKAGE_VERSION = '0.0.0'

IS_DEV = os.getenv('BIOLIB_DEV', '').upper() == 'TRUE'
