# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sortdir']

package_data = \
{'': ['*']}

install_requires = \
['watchdog>=2.1.2,<3.0.0']

entry_points = \
{'console_scripts': ['sortdir = sortdir:__main__']}

setup_kwargs = {
    'name': 'sortdir',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Yevhen Shymotiuk',
    'author_email': 'yevhenshymotiuk@gmail.com',
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
