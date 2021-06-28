# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dfa_identify']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=20.3.0,<21.0.0',
 'bidict>=0.21.2,<0.22.0',
 'dfa>=2.1.2,<3.0.0',
 'funcy>=1.15,<2.0',
 'networkx>=2.5.1,<3.0.0',
 'python-sat>=0.1.7-alpha.2,<0.2.0']

setup_kwargs = {
    'name': 'dfa-identify',
    'version': '0.1.2',
    'description': 'Python library for identifying (learning) DFAs (automata) from labeled examples.',
    'long_description': None,
    'author': 'Marcell Vazquez-Chanlatte',
    'author_email': 'mvc@linux.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
