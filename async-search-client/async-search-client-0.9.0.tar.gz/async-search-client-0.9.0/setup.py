# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_search_client']

package_data = \
{'': ['*']}

install_requires = \
['meilisearch-python-async>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'async-search-client',
    'version': '0.9.0',
    'description': 'async-search-client is now meilisearch-python-async',
    'long_description': '# Async Search Client\n\n⚠️ This project has been renamed to meilisearch-python-async and moved to the\n[meilisearch-python-async](https://github.com/sanders41/meilisearch-python-async) repository. All of\nthe functionality remains the same in meilisearch-python-async and development continues from where\nwhere this package left off. ⚠️\n',
    'author': 'Paul Sanders',
    'author_email': 'psanders1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sanders41/meilisearch-python-async',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
