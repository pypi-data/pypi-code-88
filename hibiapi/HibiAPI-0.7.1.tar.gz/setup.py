# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hibiapi',
 'hibiapi.api',
 'hibiapi.api.bilibili',
 'hibiapi.api.bilibili.api',
 'hibiapi.api.netease',
 'hibiapi.api.pixiv',
 'hibiapi.api.sauce',
 'hibiapi.api.tieba',
 'hibiapi.app',
 'hibiapi.app.routes',
 'hibiapi.app.routes.bilibili',
 'hibiapi.utils']

package_data = \
{'': ['*'], 'hibiapi': ['configs/*']}

install_requires = \
['aiocache[redis]>=0.11.1,<0.12.0',
 'aiofiles>=0.7.0,<0.8.0',
 'click>=8.0.1,<9.0.0',
 'confuse>=1.4.0,<2.0.0',
 'fastapi>=0.63.0,<0.64.0',
 'httpx[http2]>=0.17.1,<0.18.0',
 'loguru>=0.5.3,<0.6.0',
 'pycryptodomex>=3.10.1,<4.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'python-dotenv>=0.17,<0.19',
 'python-multipart>=0.0.5,<0.0.6',
 'qrcode[pil]>=6.1,<7.0',
 'sentry-sdk>=1.1.0,<2.0.0',
 'uvicorn>=0.14.0,<0.15.0']

entry_points = \
{'console_scripts': ['hibiapi = hibiapi.__main__:main']}

setup_kwargs = {
    'name': 'hibiapi',
    'version': '0.7.1',
    'description': 'An alternative implement of Imjad API',
    'long_description': None,
    'author': 'mixmoe',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
