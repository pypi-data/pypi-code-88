# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['playwrighting', 'playwrighting.navigation']

package_data = \
{'': ['*']}

install_requires = \
['12factor-configclasses>=0.4,<0.5',
 'anyio>=3.1.0,<4.0.0',
 'asyncclick>=8.0.1,<9.0.0',
 'beautifulsoup4>=4.9,<5.0',
 'html5lib>=1.1,<2.0',
 'lxml>=4.6.3,<5.0.0',
 'more-itertools>=8.7,<9.0',
 'pandas>=1.2.4,<2.0.0',
 'playwright>=1.11,<2.0',
 'python-dotenv>=0.15,<0.16',
 'rich>=10.2.2,<11.0.0',
 'selectolax>=0.2,<0.3',
 'tabulate>=0.8.9,<0.9.0']

entry_points = \
{'console_scripts': ['pying = playwrighting.pying:cli']}

setup_kwargs = {
    'name': 'playwrighting',
    'version': '0.6.1',
    'description': 'Get your ING account data',
    'long_description': '# PlaywrightING\n\nGet your ING bank account data.\n\nThis works for ING ES (Spain), for another country page you will have to change some values in constants.py and some \nand selectors.py.\n\n## Install\n\n    pip install playwrighting\n\n## Commands\n\nTo inspect all CLI commands use:\n\n    pying\n\n### Init\n\nThis command will initialize the app, scraping your bank data from your account and creating an internal file \nthat will have your global position (cards, accounts and transactions).\n\n    pying init\n\n### Update\n\nThis command will try to update your account info, if there are some changes.\nYou can force the update with parameter --force.\n\n    pying update [--force]\n\n\n### Download\n\nFiles (csv) with your accounts transactions will be downloaded in the specified download_path or supplied parameter \n--download path.\n\n    pying download [--download_path PATH]\n\n### Show\n\n    pying show\n\n\n## Build\n\n    poetry build',
    'author': 'Pablo Cabezas',
    'author_email': 'headsrooms@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
