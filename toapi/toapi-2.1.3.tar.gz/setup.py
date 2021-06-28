# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['toapi']

package_data = \
{'': ['*']}

install_requires = \
['cchardet>=2.1.7,<3.0.0',
 'click>=8.0.1,<9.0.0',
 'colorama>=0.4.4,<0.5.0',
 'cssselect>=1.1.0,<2.0.0',
 'flask>=2.0.1,<3.0.0',
 'htmlfetcher>=0.0.6,<0.0.7',
 'htmlparsing>=0.1.5,<0.2.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['toapi = toapi.cli:cli']}

setup_kwargs = {
    'name': 'toapi',
    'version': '2.1.3',
    'description': 'Every web site provides APIs.',
    'long_description': None,
    'author': 'Elliot Gao',
    'author_email': 'gaojiuli@gmail.com',
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
