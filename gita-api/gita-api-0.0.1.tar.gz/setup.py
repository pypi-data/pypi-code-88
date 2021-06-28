# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gita_api',
 'gita_api.api',
 'gita_api.api.api_v2',
 'gita_api.api.api_v2.endpoints',
 'gita_api.db',
 'gita_api.models',
 'gita_api.schemas']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.19,<2.0.0',
 'fastapi>=0.65.2,<0.66.0',
 'graphene-elastic>=0.7,<0.8',
 'graphene-sqlalchemy-filter>=1.12.2,<2.0.0',
 'graphene-sqlalchemy>=2.3.0,<3.0.0',
 'psycopg2-pgevents>=0.2.2,<0.3.0',
 'python-dotenv>=0.18.0,<0.19.0',
 'pytz>=2021.1,<2022.0',
 'uvicorn>=0.14.0,<0.15.0']

setup_kwargs = {
    'name': 'gita-api',
    'version': '0.0.1',
    'description': 'Bhagavad Gita API allows any developer to use content from Bhagavad Gita in their applications.',
    'long_description': None,
    'author': 'The Gita Initiative',
    'author_email': 'contact@bhagavadgita.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
