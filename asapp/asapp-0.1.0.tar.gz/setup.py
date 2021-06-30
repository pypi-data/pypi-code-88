# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asapp']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0', 'click>=8.0.1,<9.0.0']

entry_points = \
{'console_scripts': ['asapp = asapp.main:asapp']}

setup_kwargs = {
    'name': 'asapp',
    'version': '0.1.0',
    'description': 'Create desktop entries for running websites in app mode.',
    'long_description': None,
    'author': 'Blake Smith',
    'author_email': 'blakeinvictoria@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
