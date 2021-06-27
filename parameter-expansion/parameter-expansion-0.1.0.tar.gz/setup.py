# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['parameter_expansion']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'parameter-expansion',
    'version': '0.1.0',
    'description': 'POSIX parameter expansion in Python',
    'long_description': "# POSIX Parameter Expansion\n\nThis is an experiment to create a Python library to enable\n[POSIX parameter expansion][1] from a string.\n\n## Obvious Test Cases\n\n```python\n    >>> from pe import expand\n    >>> foo = 'abc/123-def.ghi'\n    >>> # Bland Expansion\n    >>> expand('abc $foo abc')\n    'abc abc/123-def.ghi abc'\n    >>> expand('abc${foo}abc')\n    'abcabc/123-def.ghiabc'\n    >>>\n    >>> # Default Value Expansion\n    >>> expand('-${foo:-bar}-')\n    '-abc/123-def.ghi-'\n    >>> expand('-${bar:-bar}-')\n    '-bar-'\n```\n\n### Default Value Expansion\n\n```python\n    >>> foo = 'abc/123-def.ghi'\n    >>> expand('abc $foo abc')\n    'abc abc/123-def.ghi abc'\n    >>> expand('abc${foo}abc')\n    'abcabc/123-def.ghiabc'\n```\n\n\n[1]: http://pubs.opengroup.org/onlinepubs/009695399/utilities/xcu_chap02.html#tag_02_06_02\n",
    'author': 'Michael A. Smith',
    'author_email': 'michael@smith-li.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
