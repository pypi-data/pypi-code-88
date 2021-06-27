# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['acquisition_extractor', 'acquisition_extractor.statute_parts']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'arrow>=1.1.0,<2.0.0',
 'beautifulsoup4>=4.9.3,<5.0.0',
 'html5lib>=1.1,<2.0']

setup_kwargs = {
    'name': 'acquisition-extractor',
    'version': '0.3.0',
    'description': 'Parse statute, decision data from a specified location',
    'long_description': None,
    'author': 'Marcelino G. Veloso III',
    'author_email': 'testmarcelino@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.1,<4.0.0',
}


setup(**setup_kwargs)
