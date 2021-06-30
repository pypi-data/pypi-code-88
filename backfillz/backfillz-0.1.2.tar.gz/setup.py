# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['backfillz', 'backfillz.example']

package_data = \
{'': ['*']}

install_requires = \
['importlib_metadata==3.4.0',
 'numpy==1.20.3',
 'plotly>=4.14.3,<5.0.0',
 'pystan==3.0.0',
 'scipy>=1.6.3,<2.0.0']

setup_kwargs = {
    'name': 'backfillz',
    'version': '0.1.2',
    'description': 'MCMC visualisations package developed at the University of Warwick and supported by The Alan Turing Institute.',
    'long_description': '<!-- badges: start -->\n\n[![Release build](https://github.com/WarwickCIM/backfillz-py/actions/workflows/build-publish.yml/badge.svg?branch=release)](https://github.com/WarwickCIM/backfillz-py/actions/workflows/build-publish.yml)\n[![Develop build](https://github.com/WarwickCIM/backfillz-py/actions/workflows/build-publish.yml/badge.svg?branch=develop)](https://github.com/WarwickCIM/backfillz-py/actions/workflows/build-publish.yml)\n[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n<!-- badges: end -->\n\n<img src="https://github.com/WarwickCIM/backfillz/raw/master/fig1.png" width=100% alt=""/>\n\n# New View of MCMC\n\nBackfillz-py provides new visual diagnostics for understanding MCMC (Markov Chain Monte Carlo) analyses and outputs. MCMC chains can defy a simple line graph. Unless the chain is very short (which isn’t often the case), plotting tens or hundreds of thousands of data points reveals very little other than a ‘trace plot’ where we only see the outermost points. Common plotting methods may only reveal when an MCMC really hasn’t worked, but not when it has.\nBackFillz-py slices and dices MCMC chains so increasingly parameter rich, complex analyses can be visualised meaningfully. What does ‘good mixing’ look like? Is a ‘hair caterpillar’ test verifiable? What does a density plot show and what does it hide?\n\n# Quick Start\n\nInstall from [PyPI](https://pypi.org/project/backfillz/).\n\nTODO - code example\n\n# Current prototype plots\n\nTODO\n\n# Acknowledgements\n\nWe are grateful for funding from the Alan Turing Institute within the ‘Tools, Practices and Systems’ theme. Initial user research was carried out by GJM on the ‘2020 Science’ programme (www.2020science.net/) funded by the EPSRC Cross-Discipline Interface Programme (grant number EP/I017909/1).\n',
    'author': 'James Tripp',
    'author_email': 'james.tripp@warwick.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/WarwickCIM/backfillz-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.0,<3.10',
}


setup(**setup_kwargs)
