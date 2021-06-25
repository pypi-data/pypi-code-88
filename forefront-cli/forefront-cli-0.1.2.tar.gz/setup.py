# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['forefront_cli',
 'forefront_cli.config',
 'forefront_cli.deploy',
 'forefront_cli.init',
 'forefront_cli.logout',
 'forefront_cli.projects',
 'forefront_cli.versions']

package_data = \
{'': ['*']}

install_requires = \
['PyInquirer>=1.0.3,<2.0.0',
 'click>=8.0.1,<9.0.0',
 'halo>=0.0.31,<0.0.32',
 'prettytable>=2.1.0,<3.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['ff = forefront_cli.main:cli']}

setup_kwargs = {
    'name': 'forefront-cli',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'Mike',
    'author_email': 'michaelrturck@gmail.com',
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
