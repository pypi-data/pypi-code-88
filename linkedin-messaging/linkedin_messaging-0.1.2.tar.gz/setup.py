# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linkedin_messaging']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0',
 'beautifulsoup4>=4.9.3,<5.0.0',
 'dataclasses-json>=0.5.4,<0.6.0']

setup_kwargs = {
    'name': 'linkedin-messaging',
    'version': '0.1.2',
    'description': 'An unofficial API for interacting with LinkedIn Messaging',
    'long_description': '# LinkedIn Messaging API\n\n[![Python](https://github.com/sumnerevans/linkedin-messaging-api/actions/workflows/python.yaml/badge.svg)](https://github.com/sumnerevans/linkedin-messaging-api/actions/workflows/python.yaml)\n[![Matrix Chat](https://img.shields.io/matrix/linkedin-matrix:nevarro.space?server_fqdn=matrix.nevarro.space)](https://matrix.to/#/#linkedin-matrix:nevarro.space?via=nevarro.space&via=sumnerevans.com)\n\nAn unofficial API for interacting with LinkedIn Messaging.\n\nBuilt using [aiohttp](https://docs.aiohttp.org/en/stable/).\n\n## Documentation\n\nSee [`examples` directory](./examples).\n\n## Credits\n\nAuthentication technique from [@everping](https://github.com/everping) in the\n[Linkedin-Authentication-Challenge](https://github.com/everping/Linkedin-Authentication-Challenge). Used with permission.\n',
    'author': 'Sumner Evans',
    'author_email': 'inquiries@sumnerevans.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sumnerevans/linkedin-messaging-api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
