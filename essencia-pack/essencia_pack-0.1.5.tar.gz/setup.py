# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['essencia_pack',
 'essencia_pack.core',
 'essencia_pack.core.auth',
 'essencia_pack.core.db',
 'essencia_pack.core.middleware',
 'essencia_pack.core.models',
 'essencia_pack.deta_api',
 'essencia_pack.deta_api.async_api',
 'essencia_pack.deta_api.sync_api',
 'essencia_pack.models']

package_data = \
{'': ['*'], 'essencia_pack': ['static/*']}

install_requires = \
['Jinja2>=2.11.3,<3.0.0',
 'PyYAML>=5.4.1,<6.0.0',
 'SQLAlchemy==1.3.9',
 'aiofiles>=0.6.0,<0.7.0',
 'aiosqlite>=0.17.0,<0.18.0',
 'apispec>=4.4.0,<5.0.0',
 'databases>=0.4.3,<0.5.0',
 'deta>=0.7,<0.8',
 'flama>=0.16.0,<0.17.0',
 'graphene>=2.1.8,<3.0.0',
 'httpx>=0.17.1,<0.18.0',
 'itsdangerous>=1.1.0,<2.0.0',
 'orm>=0.1.5,<0.2.0',
 'pydantic>=1.8.1,<2.0.0',
 'python-dotenv>=0.17.0,<0.18.0',
 'python-forge>=18.6.0,<19.0.0',
 'python-multipart>=0.0.5,<0.0.6',
 'requests>=2.25.1,<3.0.0',
 'starlette>=0.14.2,<0.15.0',
 'uvicorn>=0.13.4,<0.14.0']

setup_kwargs = {
    'name': 'essencia-pack',
    'version': '0.1.5',
    'description': '',
    'long_description': None,
    'author': 'arantesdv',
    'author_email': 'arantesdv@me.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
