# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thlink_backend_test_lib']

package_data = \
{'': ['*']}

install_requires = \
['aws-lambda-powertools>=1.16.1,<2.0.0',
 'pytest>=6.2.4,<7.0.0',
 'thlink-backend-app-lib>=0.6.0,<0.7.0',
 'thlink-backend-db-lib>=0.4.0,<0.5.0',
 'thlink-backend-notification-lib>=0.5.0,<0.6.0',
 'thlink-backend-object-storage-lib>=0.2.1,<0.3.0']

entry_points = \
{'pytest11': ['thlink_backend_test_lib = thlink_backend_test_lib']}

setup_kwargs = {
    'name': 'thlink-backend-test-lib',
    'version': '0.2.4',
    'description': 'pytest mock fixtures',
    'long_description': None,
    'author': 'thlink',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
