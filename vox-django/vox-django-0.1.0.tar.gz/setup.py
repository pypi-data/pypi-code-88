# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vox_django',
 'vox_django.healthcheck',
 'vox_django.management',
 'vox_django.management.commands']

package_data = \
{'': ['*']}

install_requires = \
['django',
 'django-cors-headers',
 'django-health-check',
 'django-rest-witchcraft',
 'django-sorcery',
 'djangorestframework>=3.11,<3.12',
 'drf-yasg',
 'pycryptodome',
 'python-dotenv',
 'sqlalchemy-easy-profile>=1.2.0,<2.0.0',
 'sqlalchemy-pagination',
 'sqlalchemy-schemadisplay',
 'sqlalchemy==1.3.21']

setup_kwargs = {
    'name': 'vox-django',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Jhonatan Teixeira',
    'author_email': 'jhonatan.teixeira@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
