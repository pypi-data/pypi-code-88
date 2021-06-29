# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twisp']

package_data = \
{'': ['*']}

install_requires = \
['tika>=1.24,<2.0']

entry_points = \
{'console_scripts': ['twisp = twisp:main']}

setup_kwargs = {
    'name': 'twisp',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Tzeng Yuxio',
    'author_email': 'tzengyuxio@gmail.com',
    'maintainer': 'Tzeng Yuxio',
    'maintainer_email': 'tzengyuxio@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
