# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pcmd']

package_data = \
{'': ['*']}

install_requires = \
['Distance>=0.1.3,<0.2.0', 'PyYAML>=5.4.1,<6.0.0', 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['pcmd = pcmd.main:app']}

setup_kwargs = {
    'name': 'pcmd',
    'version': '2.2.0',
    'description': 'A super simple terminal command shortener.',
    'long_description': "## About\nDuring daily development, it can be frustrating,\n\n- to type long commands when you start up the terminal for the day (or when your terminal shuts down due to unknown reasons!) or,\n- to type a set of terminal commands repeatedly to do configuration, checks, and so on.\n\n> For these problems...\n\n***pcmd*** comes in handy :thumbsup:  \nIt's main features are\n\n- It helps to execute commands with a user-define name. \n- It helps to execute multiple commands with just a single user-defined name.\n\nA single config file ...\n\n... and your ready to go !\n\nTrust me, it is better than bash aliases!\n## ><=> pcmd \n- [Documentation](https://j0fin.github.io/pcmd/)\n- [Source Code](https://github.com/j0fiN/pcmd)",
    'author': 'Jofin',
    'author_email': 'jofinfab@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/j0fiN/pcmd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
