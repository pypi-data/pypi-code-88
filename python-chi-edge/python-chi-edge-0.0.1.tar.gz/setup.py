# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chi_edge', 'chi_edge.ansible']

package_data = \
{'': ['*'],
 'chi_edge.ansible': ['roles/common/files/*',
                      'roles/common/handlers/*',
                      'roles/common/tasks/*',
                      'roles/docker/meta/*',
                      'roles/docker/tasks/*',
                      'roles/docker/templates/*',
                      'roles/nano/tasks/*',
                      'roles/nano/templates/*',
                      'roles/wireguard/files/*',
                      'roles/wireguard/tasks/*']}

install_requires = \
['ansible-runner>=1.4.7,<2.0.0', 'ansible>=4.0.0,<5.0.0', 'click>=8.0.1,<9.0.0']

setup_kwargs = {
    'name': 'python-chi-edge',
    'version': '0.0.1',
    'description': 'Manage edge devices for use with the CHI@Edge IoT/Edge testbed.',
    'long_description': None,
    'author': 'Chameleon Project',
    'author_email': 'contact@chameleoncloud.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
