# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['classyconf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'classyconf',
    'version': '0.5.1',
    'description': 'Extensible library for separation of settings from code.',
    'long_description': None,
    'author': 'Hernan Lozano',
    'author_email': 'hernantz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
