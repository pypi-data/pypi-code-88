# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyruler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyruler',
    'version': '0.9.0',
    'description': 'Simple and powerful rule engine to generate complex data validations on an easy way',
    'long_description': None,
    'author': 'Eduardo Aguilar',
    'author_email': 'dante.aguilar41@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
