# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sofascore']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sofascore',
    'version': '1.0.0',
    'description': '',
    'long_description': None,
    'author': 'shimst3r',
    'author_email': 'shimst3r@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
