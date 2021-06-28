"""
Module that securely calculates the inverse of a secret-shared matrix using the MPyC framework.
"""

# Explicit re-export of all functionalities, such that they can be imported properly. Following
# https://www.python.org/dev/peps/pep-0484/#stub-files and
# https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-no-implicit-reexport
from .matrix_inverse import matrix_inverse as matrix_inverse

__version__ = "0.3.1"
