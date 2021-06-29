# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['x690']

package_data = \
{'': ['*']}

install_requires = \
['t61codec>=1.0.1,<2.0.0']

extras_require = \
{':python_version < "3.7"': ['dataclasses>=0.7,<0.8'],
 ':python_version < "3.8"': ['importlib-metadata>=3.3.0,<4.0.0']}

setup_kwargs = {
    'name': 'x690',
    'version': '0.5.0a6',
    'description': 'Pure Python X.690 implementation',
    'long_description': 'Pure Python `X.690`_ implementation\n===================================\n\n.. image:: https://github.com/exhuma/x690/workflows/Testing/badge.svg?branch=main\n    :alt: Code Style\n\n.. image:: https://github.com/exhuma/x690/workflows/Build%20&%20Publish%20Docs/badge.svg?branch=main\n    :alt: Build & Publish Docs\n\n.. _X.690: https://www.itu.int/rec/recommendation.asp?lang=en&parent=T-REC-X.690-201508-I\n\n\nThis module contains a pure Python implementation of the "x690" standard for\nBER encoding/decoding. Other encodings are currently unsupported but\npull-requests are welcome.\n\n\nSupporting New Types\n--------------------\n\nSome applications may need to support types which are not defined in the X.690\nstandard. This is supported by this library but the types must be defined and\nregistered.\n\nTo register a type, simply subclass ``x690.types.Type``. This will take care of\nthe registration. Make sure that your new type is imported before using it.\n\nNew types should define the following 3 class-variables:\n\n**TYPECLASS**\n    A value from ``x690.util.TypeClass``\n**NATURE**\n    A value from ``x690.util.TypeNature``\n**TAG**\n    A numerical identifier for the type\n\nRefer to the x690 standard for more details on these values. As a general\nrule-of-thumb you can assume that the class is either "context" or\n"application" (it might be good to keep the "universal" class reserved for\nx690). The nature should be "primitive" for simple values and "constructed" for\ncomposed types. The tag is free to choose as long as you don\'t overlap with an\nexisting type.\n\nTo convert raw-bytes into a Python object, override ``x690.Type.decode_raw``\nand conversely also ``x690.Type.encode_raw``. Refer to the docstrings for more\ndetails.\n\n\nReverse Engineering Bytes\n-------------------------\n\nAll types defined in the ``x690`` library provide a ``.pretty()`` method which\nreturns a prettyfied string.\n\nIf you are confronted with a bytes-object encoded using X.690 but don\'t have\nany documentation, you can write the following loop::\n\n    from x690 import decode\n\n    data = open("mydatafile.bin", "rb").read()\n\n    value, nxt = decode(data)\n    print(value.pretty())\n\n    while nxt < len(data):\n        value, nxt = decode(data, nxt)\n        print(value.pretty())\n\nThis should get you started.\n\nIf the data contain non-standard types, they will get detected as "UnknownType"\nand will print out the type-class, nature and tag in the pretty-printed block.\n\nThis will allow you to define your own subclass of ``x690.types.Type`` using\nthose values. Override ``decode(...)`` in that class to handle the unknown\ntype.\n\n\nExamples\n========\n\nEncoding to bytes\n-----------------\n\nEncoding to bytes can be done by simply calling the Python builting ``bytes()``\non instances from ``x690.types``:\n\nEncoding of a single value\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n.. code:: python\n\n    >>> import x690.types as t\n    >>> myvalue = t.Integer(12)\n    >>> asbytes = bytes(myvalue)\n    >>> repr(asbytes)\n    b\'\\x02\\x01\\x0c\'\n\nEncoding of a composite value using Sequence\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n.. code:: python\n\n    >>> import x690.types as t\n    >>> myvalue = t.Sequence(\n    ...     t.Integer(12),\n    ...     t.Integer(12),\n    ...     t.Integer(12),\n    ... )\n    >>> asbytes = bytes(myvalue)\n    >>> repr(asbytes)\n    b\'0\\t\\x02\\x01\\x0c\\x02\\x01\\x0c\\x02\\x01\\x0c\'\n\n\nDecoding from bytes\n~~~~~~~~~~~~~~~~~~~\n\nDecode bytes by calling ``x690.types.decode`` on your byte data. This will\nreturn a tuple where the first value contains the decoded object, and the\nsecond one will contain any remaining bytes which were not decoded.\n\n.. code:: python\n\n    >>> import x690\n    >>> data = b\'0\\t\\x02\\x01\\x0c\\x02\\x01\\x0c\\x02\\x01\\x0c\'\n    >>> decoded, nxt = x690.decode(data)\n    >>> decoded\n    Sequence(Integer(12), Integer(12), Integer(12))\n    >>> nxt\n    11\n\n\nType-Hinting & Enforcing\n~~~~~~~~~~~~~~~~~~~~~~~~\n\n**New in 0.3.0**\n\nWhen decoding bytes, it is possible to specify an expcted type which does two\nthings: Firstly, it tells tools like ``mypy`` what the return type will be and\nsecondly, it runs an internal type-check which *ensures* that the returned\nvalue is of the expected type. ``x690.exc.UnexpectedType`` is raised otherwise.\n\nThis does of course only work if you know the type in advance.\n\n.. code:: python\n\n    >>> import x690\n    >>> import x690.types as t\n    >>> data = b\'0\\t\\x02\\x01\\x0c\\x02\\x01\\x0c\\x02\\x01\\x0c\'\n    >>> decoded, nxt = x690.decode(data, enforce_type=t.Sequence)\n    >>> decoded\n    Sequence(Integer(12), Integer(12), Integer(12))\n    >>> nxt\n    11\n\n\nStrict Decoding\n~~~~~~~~~~~~~~~\n\n**New in 0.3.0**\n\nWhen decoding using ``decode`` and you don\'t expect any remaining bytes, use\n``strict=True`` which will raise ``x690.exc.IncompleteDecoding`` if there\'s any\nremaining data.\n\n.. code:: python\n\n    >>> import x690\n    >>> data = b\'0\\t\\x02\\x01\\x0c\\x02\\x01\\x0c\\x02\\x01\\x0cjunk-bytes\'\n    >>> decoded, nxt = x690.decode(data, strict=True)\n    Traceback (most recent call last):\n      ...\n    x690.exc.IncompleteDecoding: Strict decoding still had 10 remaining bytes!\n',
    'author': 'Michel Albert',
    'author_email': 'michel@albert.lu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://exhuma.github.io/x690/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
