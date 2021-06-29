# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['models']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'django-vehicle-models',
    'version': '0.1.1',
    'description': 'models for storing in DB',
    'long_description': None,
    'author': 'Lamarmora',
    'author_email': 'scheduleanevent@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
