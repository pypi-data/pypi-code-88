# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['revjson']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'revjson',
    'version': '0.1.0',
    'description': 'A Python library for intuitive JSON handling',
    'long_description': None,
    'author': 'reeve0930',
    'author_email': 'reeve0930@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
