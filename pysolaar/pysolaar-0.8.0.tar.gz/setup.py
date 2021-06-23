# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysolaar', 'pysolaar.utils']

package_data = \
{'': ['*']}

install_requires = \
['pysolr>=3.9.0,<4.0.0', 'solrq>=1.1.1,<2.0.0']

setup_kwargs = {
    'name': 'pysolaar',
    'version': '0.8.0',
    'description': '',
    'long_description': None,
    'author': 'Richard Hadden',
    'author_email': 'richard.hadden@oeaw.ac.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4',
}


setup(**setup_kwargs)
