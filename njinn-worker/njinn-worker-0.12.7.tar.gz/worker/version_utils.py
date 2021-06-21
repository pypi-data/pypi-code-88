"""
We use get_worker_version both in our code and in setup.py,
so we can't put it in a file with external dependencies.
"""
import os

BASE_REQUIREMENTS = [
    "requests >=2.25, <2.26",
    "PyJWT ==1.7.1",
    "requests-jwt ==0.5.3",
    "backoff ==1.10.0",
    # explicit cryptography dependencies to be in sync with base packs
    "cryptography ==3.4.7",
]


def get_worker_version() -> str:
    """
    Gets the worker version
    """
    version_file = open(os.path.join(os.path.dirname(__file__), "VERSION"))
    return version_file.read().strip()

