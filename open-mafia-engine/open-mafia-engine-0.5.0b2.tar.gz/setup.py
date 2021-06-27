# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['open_mafia_engine',
 'open_mafia_engine.api',
 'open_mafia_engine.builders',
 'open_mafia_engine.built_in',
 'open_mafia_engine.commands',
 'open_mafia_engine.core',
 'open_mafia_engine.examples',
 'open_mafia_engine.test',
 'open_mafia_engine.util']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=1.6.0,<2.0.0',
 'fuzzywuzzy>=0.18.0,<0.19.0',
 'makefun>=1.11.3,<2.0.0',
 'sortedcontainers>=2.3.0,<3.0.0',
 'typer>=0.3.2,<0.4.0']

extras_require = \
{'dev': ['pytest>=6.2.4,<7.0.0', 'flake8>=3.9.2,<4.0.0', 'mypy>=0.800,<0.801'],
 'docs': ['pygments>=2.9.0,<2.10.0',
          'mkdocs>=1.1.2,<2.0.0',
          'mkdocs-material>=7.1.8,<8.0.0',
          'mkdocstrings>=0.15.2,<0.16.0'],
 'examples': ['prompt-toolkit>=3.0.19,<4.0.0', 'pygments>=2.9.0,<2.10.0'],
 'pygments': ['pygments>=2.9.0,<2.10.0'],
 'recommended': ['prompt-toolkit>=3.0.19,<4.0.0',
                 'pygments>=2.9.0,<2.10.0',
                 'pytest>=6.2.4,<7.0.0'],
 'test': ['pytest>=6.2.4,<7.0.0']}

entry_points = \
{'console_scripts': ['mafia-cli = open_mafia_engine.examples.cli:main']}

setup_kwargs = {
    'name': 'open-mafia-engine',
    'version': '0.5.0b2',
    'description': 'Open Mafia Engine - a framework for mafia/werewolf games.',
    'long_description': '# Open Mafia Engine\n\n[![PyPI version](https://badge.fury.io/py/open-mafia-engine.svg)](https://badge.fury.io/py/open-mafia-engine)\n[![Stable Release](https://img.shields.io/github/release/open-mafia/open_mafia_engine.svg)](https://github.com/open-mafia/open_mafia_engine/releases)\n[![Docs](https://readthedocs.org/projects/open-mafia-engine/badge/?version=latest)](https://open-mafia-engine.readthedocs.io/en/latest/)\n\n[![Test Python package "open_mafia_engine"](https://github.com/open-mafia/open_mafia_engine/actions/workflows/python-testing.yml/badge.svg)](https://github.com/open-mafia/open_mafia_engine/actions/workflows/python-testing.yml)\n\nThe Open Mafia Engine is a flexible, open-source game engine for Mafia-like games.\n\nSee the [Wikipedia article](https://en.wikipedia.org/wiki/Mafia_%28party_game%29)\nfor information on what Mafia/Werewolf is.\n\nThe Open Mafia Engine actually allows a much broader type of game to be played,\nwith custom roles and very intricate "setups". Most of these custom roles come\nfrom either "real-life" games or online forums such as\n[MafiaScum](https://wiki.mafiascum.net/index.php?title=Main_Page) and\n[Bay12Games Mafia Subforum](http://www.bay12forums.com/smf/index.php?board=20.0).\n\n## Features\n\n- Event-based architecture, which allows for very complex interactions.\n- Many built-in abilities, victory conditions, etc.\n  (Not "many" yet, but we\'re working on it!)\n- Games are defined declaratively or using an parametrized GameBuilder.\n- Open source & extensible.\n\n## Installing\n\nInstall the latest stable version, with recommended dependencies, via pip:\n\n`pip install open_mafia_engine[recommended]`\n\nSee the [dev docs](docs/development/installing_dev.md) to install for local\ndevelopment (using Poetry).\n\n## Getting started\n\nThis example starts a 5-player "test" mafia game (1 mafioso vs 4 townies):\n\n```python\nimport open_mafia_engine.api as mafia\n\nbuilder = mafia.GameBuilder.load("test")\nplayers = [\'Alice\', \'Bob\', \'Charlie\', \'Dave\', \'Eddie\']\ngame = builder.build(players)\n```\n\n## Example Application\n\nThis repository includes an example text-based Mafia app, runnable like:\n\n```bash\nmafia-cli\n# or\npython -m open_mafia_engine.example.cli\n```\n\nThis is what the UI looks like:\n\n![Example CLI Application](docs/examples/ExampleMafiaCLI.gif)\n',
    'author': 'Open Mafia Team',
    'author_email': 'openmafiateam@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://open-mafia-engine.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
