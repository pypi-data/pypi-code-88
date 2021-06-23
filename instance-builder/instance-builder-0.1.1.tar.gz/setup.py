# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['instance_builder']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'instance-builder',
    'version': '0.1.1',
    'description': 'Instance builder library for Python inspired by Lombok',
    'long_description': None,
    'author': 'Shuntaro Shimizu',
    'author_email': 'ut.s.shimizu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
