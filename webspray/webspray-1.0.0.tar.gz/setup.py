# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webspray', 'webspray.lib']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.3,<5.0.0',
 'lxml>=4.6.3,<5.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['webspray = webspray.webspray:go']}

setup_kwargs = {
    'name': 'webspray',
    'version': '1.0.0',
    'description': 'Fuzz for hidden proxies, vhosts, and URLs across many hosts',
    'long_description': None,
    'author': 'TheTechromancer',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/blacklanternsecurity/webspray',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
