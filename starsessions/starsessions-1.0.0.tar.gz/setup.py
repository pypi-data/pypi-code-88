# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starsessions']

package_data = \
{'': ['*']}

install_requires = \
['itsdangerous>=2.0.1,<3.0.0', 'starlette>=0.15.0,<0.16.0']

setup_kwargs = {
    'name': 'starsessions',
    'version': '1.0.0',
    'description': 'Pluggable session support for Starlette.',
    'long_description': None,
    'author': 'alex.oleshkevich',
    'author_email': 'alex.oleshkevich@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
