# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lunchmoney']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.18.1,<0.19.0', 'pydantic>=1.8.2,<2.0.0']

setup_kwargs = {
    'name': 'lunchmoney',
    'version': '0.1.0',
    'description': 'Python client for the Lunch Money API.',
    'long_description': None,
    'author': 'Alan Velasco',
    'author_email': 'alanvelasco.a@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
