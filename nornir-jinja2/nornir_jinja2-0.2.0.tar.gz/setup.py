# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nornir_jinja2', 'nornir_jinja2.plugins', 'nornir_jinja2.plugins.tasks']

package_data = \
{'': ['*']}

install_requires = \
['jinja2>=2.11.2,<4', 'nornir>=3,<4']

setup_kwargs = {
    'name': 'nornir-jinja2',
    'version': '0.2.0',
    'description': 'Jinja2 plugins for nornir',
    'long_description': None,
    'author': 'David Barroso',
    'author_email': 'dbarrosop@dravetech.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
