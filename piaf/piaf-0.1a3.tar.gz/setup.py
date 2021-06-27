# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['piaf', 'piaf.comm', 'piaf.examples']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'piaf',
    'version': '0.1a3',
    'description': 'A FIPA-compliant Agent Platform written in python.',
    'long_description': '# Python Intelligent Agent Framework (piaf)\n\n![pipeline status](https://gitlab.com/ornythorinque/piaf/badges/master/pipeline.svg)\n![coverage report](https://gitlab.com/ornythorinque/piaf/badges/master/coverage.svg?job=test)\n\n\nThe aim of piaf is to provide a FIPA-compliant agent framework using Python. It uses **asyncio** to power agents.\n\n**For now, this work is experimental and subject to changes.**\n\n## Documentation\nThe full documentation (both user and API) is available here: https://ornythorinque.gitlab.io/piaf\nIt will teach you how to install and run your own agents.\n\n## Author(s)\n* ornythorinque (pierredubaillay@outlook.fr)\n',
    'author': 'Pierre DUBAILLAY',
    'author_email': 'pierredubaillay@outlook.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/ornythorinque/piaf',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
