# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['speccify']

package_data = \
{'': ['*']}

install_requires = \
['djangorestframework',
 'djangorestframework-dataclasses',
 'drf-spectacular',
 'typing-extensions']

setup_kwargs = {
    'name': 'speccify',
    'version': '0.1.0',
    'description': 'Tie together `drf-spectacular` and `djangorestframework-dataclasses` for easy-to-use apis and openapi schemas.',
    'long_description': None,
    'author': 'Lyst Ltd.',
    'author_email': 'devs@lyst.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
