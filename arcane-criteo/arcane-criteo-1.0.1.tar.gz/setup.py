# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arcane', 'arcane.criteo']

package_data = \
{'': ['*']}

install_requires = \
['backoff>=1.10.0,<2.0.0', 'criteo-marketing-transition>=1.0.3,<2.0.0']

setup_kwargs = {
    'name': 'arcane-criteo',
    'version': '1.0.1',
    'description': 'A client to help us request Criteo API',
    'long_description': None,
    'author': 'Arcane',
    'author_email': 'product@arcane.run',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
