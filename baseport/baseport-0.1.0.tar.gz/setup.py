# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['baseport']

package_data = \
{'': ['*']}

install_requires = \
['basecampy3>=0.4.0,<0.5.0',
 'click>=8.0.1,<9.0.0',
 'html2text>=2020.1.16,<2021.0.0']

entry_points = \
{'console_scripts': ['baseport = baseport.cli:cli']}

setup_kwargs = {
    'name': 'baseport',
    'version': '0.1.0',
    'description': 'Export Basecamp 3 To-Dos into a CSV.',
    'long_description': None,
    'author': 'Nate Gadzhi',
    'author_email': 'nate@respawn.io',
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
