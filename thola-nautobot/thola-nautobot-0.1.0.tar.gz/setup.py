# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thola_nautobot', 'thola_nautobot.api', 'thola_nautobot.thola']

package_data = \
{'': ['*'], 'thola_nautobot': ['templates/thola_nautobot/*']}

install_requires = \
['nautobot>=1.0,<1.1', 'thola-client>=1.0.2,<2.0.0']

setup_kwargs = {
    'name': 'thola-nautobot',
    'version': '0.1.0',
    'description': 'Thola plugin for Nautobot',
    'long_description': None,
    'author': 'Thola Team',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
