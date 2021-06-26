"""
Simple singleton to share variables across modules

Features
--------

* Use the basic module namespace functionality

Examples
--------

.. code-block:: python

  import monist
  dispatch = eval(monist.dispatch())

  # set singleton value
  monist.thing = 1

  # access singleton value with fallback
  # if monist.thing exists, return it, otherwise return some_default
  asdf = dispatch('thing', some_default)

Importing monist as another name works also:

.. code-block:: python

  import monist as stage
  stage.something = 2

Limitations
-----------

* Almost certainly not thread-safe, appropriate for concurrency, etc.

License
-------

* Free software: MIT license

Documentation
-------------

* https://monist.readthedocs.io/
"""

__author__ = """Brendan Strejcek"""
__email__ = 'brendan@datagazing.com'
__version__ = '0.1.0'

from .monist import dispatch # noqa F401
