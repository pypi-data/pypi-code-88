# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pwcheck', 'pwcheck.tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pwcheck',
    'version': '0.1.0',
    'description': 'Python Password Checker',
    'long_description': None,
    'author': 'Itotutona',
    'author_email': 'itotutona.github@evta.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
