# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['garages_burgos']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.0.0,<4.0.0', 'bs4>=0.0.1,<0.0.2', 'lxml>=4.6.3,<5.0.0']

setup_kwargs = {
    'name': 'garages-burgos',
    'version': '1.1.0',
    'description': 'Asynchronous Python client for getting garage occupancy in Burgos',
    'long_description': '# Python API fetching garage occupancy in Burgos\n\nRetrieve the status of the Public Parkings in Burgos, Spain.\n\n## Acknowledgements\n\n- Inspired by\n  [Garages Amsterdam](https://github.com/klaasnicolaas/garages_amsterdam)\n\n## Authors\n\n- [@ricveal](https://www.github.com/ricveal)\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'ricveal',
    'author_email': 'ricveal@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ricveal/garages_burgos',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
