import os
import re

from semantic_version import Version
from setuptools import setup


def get_version():
    VERSIONFILE = os.path.join("gdaps", "__init__.py")
    lines = open(VERSIONFILE, "rt").readlines()
    for line in lines:
        match = re.search("^__version__ ?= ?['\"]([^'\"]*)['\"].*$", line, re.M)
        if match:
            return match.group(1)
    raise RuntimeError("No __version__ attribute found in %s." % (VERSIONFILE,))


version = get_version()
try:
    Version(version)
    setup(version=version)
except ValueError:
    raise TypeError(
        f"Version '{version}' in CHANGELOG file is not a semantic version number."
    )
