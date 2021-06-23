# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['scholar_network']

package_data = \
{'': ['*']}

install_requires = \
['selenium>=3.141.0,<4.0.0']

setup_kwargs = {
    'name': 'scholar-network',
    'version': '0.1.9',
    'description': 'Graph Network Analysis for scraping Google Scholar authors.',
    'long_description': '# Welcome to Scholar Network\n\nThis package is intended for people wanting to scrape Google Scholar\nto build graph networks of Google Scholar authors and identify network\nconnections as opportunities for collaboration.\n\n## Features\n\n1. Selenium based web scraping\n2. Poetry based dependency management\n3. Basic Graph algorithms and metrics\n',
    'author': 'Nick Anthony',
    'author_email': 'nanthony007@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
