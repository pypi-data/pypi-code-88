# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['puchipuchi_filler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'puchipuchi-filler',
    'version': '0.1.2',
    'description': 'nothing',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
