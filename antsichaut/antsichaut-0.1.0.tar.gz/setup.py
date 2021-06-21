# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['antsichaut']

package_data = \
{'': ['*']}

install_requires = \
['ConfigArgParse>=1.4.1,<2.0.0']

entry_points = \
{'console_scripts': ['antsichaut = antsichaut.antsichaut:main']}

setup_kwargs = {
    'name': 'antsichaut',
    'version': '0.1.0',
    'description': 'antsichaut automates ansible changelog generation from GitHub Pull Requests',
    'long_description': None,
    'author': 'Sebastian Gumprich',
    'author_email': 'sebastian.gumprich@t-systems.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
