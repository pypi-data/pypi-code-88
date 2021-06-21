# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linechart']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.1.0,<2.0.0',
 'empyrical>=0.5.5,<0.6.0',
 'linefolio>=1.5.0,<2.0.0',
 'matplotlib>=3.4.2,<4.0.0',
 'pandas>=1.2.4,<2.0.0',
 'quantrocket-client>=2.6.0,<3.0.0',
 'scipy>=1.7.0,<2.0.0',
 'seaborn>=0.11.1,<0.12.0']

setup_kwargs = {
    'name': 'linechart',
    'version': '1.7.0',
    'description': 'Backtest performance analysis and charting for MoonLine.',
    'long_description': None,
    'author': 'Tim Wedde',
    'author_email': 'timwedde@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
