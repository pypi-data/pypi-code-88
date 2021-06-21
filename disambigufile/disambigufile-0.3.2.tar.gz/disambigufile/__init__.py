"""
Class with file-like interface to a file found in provided search path

Features
--------

* Search a path for a file that matches a pattern
* Search a path for a file inside directories that match a pattern
* Basic file-like interfaces:
    * DisFile(...).open()
    * with DisFile(...) as f: ...
* Get path from config file (if optini module installed)

Examples
--------

Simple usage:

.. code-block:: python

  from disambigufile import DisFile
  path = '/bin:/usr/bin:/usr/local/bin'
  try:
      print(DisFile('^ls', path=path))
  except Exception as e:
      print(f"unable to disambiguate file; exception: {e}")

Using a `with` statement to open the disambiguated file:

.. code-block:: python

  from disambigufile import DisFile
  path = 'path1:path2'
  try:
      with DisFile(r'^asdf', path=path) as f:
          print(f.read())
  except Exception as e:
      print(f"unable to disambiguate file; exception: {e}")

With more specific exception handling:

.. code-block:: python

  from disambigufile import DisFile
  import disambigufile
  path = '/bin:/usr/bin:/usr/local/bin'
  try:
      print(DisFile('^ls', path=path))
  except disambigufile.Error as e:
      # will only catch module-specific exceptions
      print(f"unable to disambiguate file; exception: {e}")

Match a file inside of a matched directory:

.. code-block:: python

  from disambigufile import DisFile
  # search for unique file matching ~/Datasets/*2019-08-19*/data*
  path='~/Datasets'
  try:
      hit = DisFile(
          pattern='2019-08-19',
          path=path,
          subpattern='^data',
      )
      print(hit)
  except disambigufile.Error as e:
      print(f"unable to disambiguate file; exception: {e}")

License
-------

* Free software: MIT license

Documentation
-------------

* https://disambigufile.readthedocs.io/

"""

__author__ = """Brendan Strejcek"""
__email__ = 'brendan@datagazing.com'
__version__ = '0.3.2'

from .disambigufile import DisFile # noqa F401
from .disambigufile import Error # noqa F401
from .disambigufile import NoMatchError # noqa F401
from .disambigufile import AmbiguousMatchError # noqa F401
