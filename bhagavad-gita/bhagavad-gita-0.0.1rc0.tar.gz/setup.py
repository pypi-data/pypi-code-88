# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bhagavad_gita']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'bhagavad-gita',
    'version': '0.0.1rc0',
    'description': '',
    'long_description': None,
    'author': 'aahnik',
    'author_email': 'daw@aahnik.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
