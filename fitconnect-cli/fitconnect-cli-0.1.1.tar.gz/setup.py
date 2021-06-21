# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['workspace']

package_data = \
{'': ['*'],
 'workspace': ['.git/*',
               '.git/hooks/*',
               '.git/info/*',
               '.git/logs/*',
               '.git/objects/01/*',
               '.git/objects/2a/*',
               '.git/objects/3e/*',
               '.git/objects/5a/*',
               '.git/objects/64/*',
               '.git/objects/79/*',
               '.git/objects/8e/*',
               '.git/objects/93/*',
               '.git/objects/94/*',
               '.git/objects/a3/*',
               '.git/objects/ae/*',
               '.git/objects/cf/*',
               '.git/objects/d3/*',
               '.git/objects/d7/*',
               '.git/objects/f5/*',
               '.git/objects/fb/*',
               '.git/refs/tags/*',
               '.github/workflows/*']}

install_requires = \
['PyInquirer>=1.0.3,<2.0.0',
 'PyJWT>=2.1.0,<3.0.0',
 'josepy>=1.8.0,<2.0.0',
 'pem>=21.2.0,<22.0.0',
 'pyOpenSSL>=20.0.1,<21.0.0',
 'python-json-config>=1.2.3,<2.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['fitconnect = main:main']}

setup_kwargs = {
    'name': 'fitconnect-cli',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Lilith Wittmann',
    'author_email': 'mail@lilithwittmann.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
