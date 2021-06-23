# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clacks']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2.4,<4.0.0']

setup_kwargs = {
    'name': 'django-clacks',
    'version': '0.1.0',
    'description': 'The unseen, silent tribute to those we have lost.',
    'long_description': '',
    'author': 'David Cooke',
    'author_email': 'me@dave.lc',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
