# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['team_the_chef_filler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'team-the-chef-filler',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'kohkubo',
    'author_email': 'kohkubo@student.42tokyo.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
