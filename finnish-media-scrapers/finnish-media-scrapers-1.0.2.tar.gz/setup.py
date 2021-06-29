# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['finnish_media_scrapers', 'finnish_media_scrapers.scripts']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.2.0,<22.0.0', 'beautifulsoup4>=4.9.3,<5.0.0', 'lxml>=4.6.3,<5.0.0']

setup_kwargs = {
    'name': 'finnish-media-scrapers',
    'version': '1.0.2',
    'description': 'Scrapers for extracting articles from Finnish journalistic media websites.',
    'long_description': None,
    'author': 'Human Sciences - Computing Interaction Research Group',
    'author_email': 'eetu.makela@helsinki.fi',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
