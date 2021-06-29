# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['velogames']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.3,<5.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['velogames = velogames.cli:main']}

setup_kwargs = {
    'name': 'velogames',
    'version': '0.1.1',
    'description': 'Small tool for scraping Velogames data',
    'long_description': '# Velogames data scraper\n\nParses data from [velogames.com](https://www.velogames.com/) and outputs it into\na CSV file for further processing.\n\nPossible output commands:\n\n- ``teams``:  Parse all teams in a league\n- ``riders``: Parse all selected riders in the league\n- ``scores``: Parse scores for all different events in the league\n',
    'author': 'Ossi Rajuvaara',
    'author_email': 'ossi@robocorp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/osrjv/velogames',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
