# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lmanage', 'lmanage.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'coloredlogger>=1.3.12,<2.0.0',
 'coloredlogs>=15.0,<16.0',
 'debugpy>=1.3.0,<2.0.0',
 'icecream>=2.1.0,<3.0.0',
 'ipython>=7.20.0,<8.0.0',
 'lookml>=3.0.3,<4.0.0',
 'pandas>=1.2.2,<2.0.0',
 'pynvim>=0.4.3,<0.5.0',
 'pytest-mock>=3.5.1,<4.0.0',
 'snoop>=0.3.0,<0.4.0',
 'sqlparse>=0.4.1,<0.5.0',
 'tabulate>=0.8.8,<0.9.0',
 'verboselogs>=1.7,<2.0']

entry_points = \
{'console_scripts': ['lmanage = lmanage.cli:lmanage']}

setup_kwargs = {
    'name': 'lmanage',
    'version': '0.1.4',
    'description': '',
    'long_description': None,
    'author': 'hselbie',
    'author_email': 'hselbie@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.9',
}


setup(**setup_kwargs)
