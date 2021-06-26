# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tgl2rdm', 'tgl2rdm.cli', 'tgl2rdm.extract']

package_data = \
{'': ['*']}

install_requires = \
['petl>=1.7.4,<2.0.0',
 'schema>=0.7.4,<0.8.0',
 'toml>=0.10.2,<0.11.0',
 'typer[all]>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['t2m = tgl2rdm.__main__:app']}

setup_kwargs = {
    'name': 'tgl2rdm',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'BANO.notIT',
    'author_email': 'bano.notit@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
