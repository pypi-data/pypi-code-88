# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['essencia_core',
 'essencia_core.db',
 'essencia_core.db.deta',
 'essencia_core.forms',
 'essencia_core.models',
 'essencia_core.utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0',
 'MarkupSafe>=2.0.1,<3.0.0',
 'bootstrap4>=0.1.0,<0.2.0',
 'deta>=0.8,<0.9',
 'starlette>=0.14.2,<0.15.0',
 'typesystem>=0.2.4,<0.3.0',
 'uvicorn>=0.14.0,<0.15.0']

setup_kwargs = {
    'name': 'essencia-core',
    'version': '0.1.51',
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
