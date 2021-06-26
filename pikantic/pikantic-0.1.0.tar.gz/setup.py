# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pikantic']

package_data = \
{'': ['*']}

install_requires = \
['aio-pika>=6.8.0,<7.0.0', 'pika>=1.2.0,<2.0.0']

setup_kwargs = {
    'name': 'pikantic',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Tom',
    'author_email': 'tomgrin10@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
