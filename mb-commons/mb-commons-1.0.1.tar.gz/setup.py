import codecs
import os
import re

import setuptools


def find_version(*file_paths):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *file_paths), "r") as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name="mb-commons",
    version=find_version("mb_commons/__init__.py"),
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "requests==2.25.1",
        "PySocks==1.7.1",
        "sorcery==0.2.1",
        "pydash==5.0.1",
        "wrapt==1.12.1",
        "python-dateutil==2.8.1",
        "pymongo==3.11.4",
        "pydantic==1.8.2",
    ],
    extras_require={
        "dev": [
            "pytest==6.2.4",
            "python-dotenv==0.18.0",
            "pre-commit==2.13.0",
            "pytest-xdist==2.3.0",
            "wheel==0.36.2",
            "twine==3.4.1",
        ],
    },
)
