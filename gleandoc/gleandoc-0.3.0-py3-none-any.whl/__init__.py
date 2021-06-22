"""
Convenience functions to extract docstring and write README

* Intent: store one copy of top-level docstring in <package>/__init__.py
* Allows generation of top level gitub README based on the package docstring

Features
--------

* Determine package name from current directory
* Extract docstring using Python semantics and standards
* No dependencies outside standard library
* Uses abstract syntax tree parsing for relative __init__.py files

Examples
--------

Print the first line of a docstring:

.. code-block:: python

  >>> import gleandoc
  >>> docstring = gleandoc.docstring('re')
  >>> docstring.splitlines()[0]
  'Support for regular expressions (RE).'
  >>>

Do the same thing from the command line:

.. code-block:: console

  $ gleandoc re | head -1
  Support for regular expressions (RE).
  $

Interpolate template README.rst.fstr and write results to README.rst,
replacing {__doc__} with extracted docstring based on the name of the
current directory:

.. code-block:: console

  $ gleandoc README.rst.fstr README.rst
  gleandoc: WARNING: replacing README.rst
  gleandoc: INFO: wrote README.rst
  $

The -h option at the command line will show supported options:

.. code-block:: console

  $ gleandoc -h
  Usage: gleandoc [-h] [NAME]
  Extract docstring from module [NAME]

    -h, --help            show this help message and exit

  - If unspecified, NAME defaults to the basename of the current directory
  - This is designed for use in build systems to construct README files

  Alternative two argument usage: gleandoc TEMPLATE README
  Interpolate docstring into TEMPLATE and write results to README

  - In this mode, always derives NAME from basename of current directory
  - Template uses style similar to f-string
  - Supported variables which will be interpolated include: {__doc__}
  - For literal (single) braces, use double braces: {{ or }}

Limitations
-----------

* Embedded backslash-n newlines are treated as actual newlines
* Relies on various pseudo-internals: locals(), exec()

"""

__author__ = """Brendan Strejcek"""
__email__ = 'brendan@datagazing.com'
__version__ = '0.3.0'

from .gleandoc import docstring, main # noqa F401
