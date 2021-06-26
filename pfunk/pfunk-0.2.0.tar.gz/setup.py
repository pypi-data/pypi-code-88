# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pfunk', 'pfunk.contrib', 'pfunk.contrib.auth', 'pfunk.tests', 'pfunk.utils']

package_data = \
{'': ['*']}

install_requires = \
['envs>=1.3,<2.0',
 'faunadb>=4.0.1,<5.0.0',
 'jinja2==3.0.1',
 'pip>=21.0.1,<22.0.0',
 'pytz>=2021.1,<2022.0',
 'requests>=2.23.0,<3.0.0',
 'valley>=1.5.6,<2.0.0']

setup_kwargs = {
    'name': 'pfunk',
    'version': '0.2.0',
    'description': 'A Python library created make building FaunaDB GraphQL schemas and authentication code easier.',
    'long_description': None,
    'author': 'Brian Jinwright',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
