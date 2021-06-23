# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['trial_hello']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['trial-hello = trial-hello.console:main']}

setup_kwargs = {
    'name': 'trial-hello',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Bhuwan Bhatt',
    'author_email': 'bhattbhuwan13@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
