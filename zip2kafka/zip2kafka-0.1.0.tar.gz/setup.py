# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zip2kafka']

package_data = \
{'': ['*']}

install_requires = \
['confluent-kafka>=1.7.0,<2.0.0', 'loguru>=0.5.3,<0.6.0', 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['zip2kafka = zip2kafka.main:app']}

setup_kwargs = {
    'name': 'zip2kafka',
    'version': '0.1.0',
    'description': 'Package a zip and push it to kafka (and back!)',
    'long_description': None,
    'author': 'Dmitri Gvozdev',
    'author_email': 'dmitrigvozdev94@gmail.com',
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
