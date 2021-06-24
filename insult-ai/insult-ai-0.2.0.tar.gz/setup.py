# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['insult_ai']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0', 'detoxify>=0.2.2,<0.3.0', 'pandas>=1.2.5,<2.0.0']

entry_points = \
{'console_scripts': ['insult-ai = insult_ai.console:insult_me']}

setup_kwargs = {
    'name': 'insult-ai',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Richard Brooker',
    'author_email': 'richard@anghami.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
