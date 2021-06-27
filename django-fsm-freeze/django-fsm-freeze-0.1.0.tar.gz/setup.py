# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_fsm_freeze']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2.4,<4.0.0',
 'black>=21.6b0,<22.0',
 'django-dirtyfields>=1.7.0,<2.0.0',
 'django-fsm>=2.7.1,<3.0.0',
 'flake8>=3.9.2,<4.0.0',
 'isort>=5.9.1,<6.0.0',
 'pytest-django>=4.4.0,<5.0.0',
 'pytest>=6.2.4,<7.0.0']

setup_kwargs = {
    'name': 'django-fsm-freeze',
    'version': '0.1.0',
    'description': 'Django FSM data freeze support',
    'long_description': None,
    'author': 'mingtung',
    'author_email': 'mingtung.hong@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ming-tung/django-fsm-freeze',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
