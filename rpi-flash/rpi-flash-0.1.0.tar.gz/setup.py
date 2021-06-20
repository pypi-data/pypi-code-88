# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rpi_flash']

package_data = \
{'': ['*']}

install_requires = \
['humanize>=3.9.0,<4.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'typer>=0.3.2,<0.4.0']

setup_kwargs = {
    'name': 'rpi-flash',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Jono Hill',
    'author_email': 'jono@hillnz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
