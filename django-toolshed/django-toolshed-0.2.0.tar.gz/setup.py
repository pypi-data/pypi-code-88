# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_toolshed', 'django_toolshed.management.commands']

package_data = \
{'': ['*'],
 'django_toolshed': ['static/django_toolshed/css/*',
                     'static/django_toolshed/images/*',
                     'static/django_toolshed/js/*',
                     'templates/django_toolshed/*']}

install_requires = \
['Django>=3.1,<4.0',
 'django-click>=2.2.0,<3.0.0',
 'ipython_genutils>=0.2.0,<0.3.0',
 'iterfzf>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'django-toolshed',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Dani Hodovic',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
