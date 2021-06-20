# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ayed']

package_data = \
{'': ['*']}

install_requires = \
['openpyxl>=3.0.7,<4.0.0', 'pandas>=1.2.4,<2.0.0', 'rich>=10.4.0,<11.0.0']

entry_points = \
{'console_scripts': ['ayed = ayed.tool:main']}

setup_kwargs = {
    'name': 'ayed',
    'version': '0.5.0',
    'description': '',
    'long_description': None,
    'author': 'Bocanada',
    'author_email': '24578415+Bocanada@users.noreply.github.com',
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
