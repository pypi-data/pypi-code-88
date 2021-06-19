"""
Simple convenience function to extract docstring

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

Features
--------

* No dependencies

Limitations
-----------

* Embedded backslash-n newlines are treated as actual newlines
* Relies on various pseudo-internals: locals(), exec()

"""

__author__ = """Brendan Strejcek"""
__email__ = 'brendan@datagazing.com'
__version__ = '0.1.0'

from .gleandoc import docstring, main # noqa F401
