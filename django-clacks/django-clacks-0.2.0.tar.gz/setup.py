# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clacks']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2.4,<4.0.0']

setup_kwargs = {
    'name': 'django-clacks',
    'version': '0.2.0',
    'description': 'The unseen, silent tribute to those we have lost.',
    'long_description': '# Django Clacks\nThe unseen, silent tribute to those we have lost.\n\n\n![python-versions](https://img.shields.io/pypi/pyversions/django-clacks) ![version](http://img.shields.io/pypi/v/django-clacks.svg?maxAge=3600) [![discord](https://img.shields.io/discord/577123238929498122)](https://discord.gg/mErKh58nWU)\n<hr>\n\n`django-clacks` contains boilerplate code for working with the nonstandard HTTP header `X-Clacks-Overhead`.\n\nYou can find out more about the `X-Clacks-Overhead` header here: https://xclacksoverhead.org/home/about\n\n\n## Installation\nDjango Clacks is on [PyPI](https://pypi.org/project/django-clacks/). Install it with `pip install django-clacks` or add it with your dependency manager.\n\n\n\n## Quickstart\nAdd `clacks.middleware.ClacksMiddleware` to your `MIDDLEWARE` setting:\n```py\nMIDDLEWARE = [\n    # ...\n    "clacks.middleware.ClacksMiddleware",\n    # ...\n]\n```\nBy default, all responses will now have a header `X-Clacks-Overhead`, with the content `GNU Terry Pratchett`. <br>\nYou can modify the names used with the `CLACKS_NAMES` setting. The following setting:\n```py\nCLACKS_NAMES = [\n    "Terry Pratchett",\n    "Joe Armstrong",\n]\n```\nWill result in an `X-Clacks-Overhead` header containing `GNU Terry Pratchett, Joe Armstrong`.\n',
    'author': 'David Cooke',
    'author_email': 'me@dave.lc',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
