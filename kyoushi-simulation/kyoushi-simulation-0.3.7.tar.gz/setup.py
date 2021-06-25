# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cr_kyoushi', 'cr_kyoushi.simulation']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'colorama>=0.4.4,<0.5.0',
 'livereload>=2.6.3,<3.0.0',
 'numpy>=1.19.5,<2.0.0',
 'pydantic>=1.8.1,<2.0.0',
 'ruamel.yaml>=0.16.12,<0.17.0',
 'structlog>=20.2.0,<21.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=3.1.0,<4.0.0',
                             'typing-extensions>=3.7.4,<4.0.0']}

entry_points = \
{'console_scripts': ['kyoushi-sim = kyoushi.simulation.cli:cli']}

setup_kwargs = {
    'name': 'kyoushi-simulation',
    'version': '0.3.7',
    'description': '',
    'long_description': '# AIT Cyber Range Kyoushi - Simulation\n\nThe Kyoushi Simulation package provides a development API and cli utilities for creating\nand running state machines. Developed state machines can be executed to automate the simulation\nof both attacker and normal user behavior in a Cyber Range. Thus facilitating Cyber Range\nexercises, IDS data set generation and other Cyber Range related tasks.\n',
    'author': 'Maximilian Frank',
    'author_email': 'maximilian.frank@ait.ac.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git-service.ait.ac.at/sct-cyberrange/tools/kyoushi/simulation',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
