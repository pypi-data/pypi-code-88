# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mailersend']

package_data = \
{'': ['*']}

install_requires = \
['pre-commit>=2.12.1,<3.0.0', 'requests>=2.25.0,<3.0.0']

setup_kwargs = {
    'name': 'mailersend',
    'version': '0.1.1',
    'description': 'The official MailerSend Python SDK',
    'long_description': None,
    'author': 'Alex Orfanos',
    'author_email': 'alexandros@mailerlite.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
