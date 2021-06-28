# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bits', 'bits.mhl']

package_data = \
{'': ['*']}

install_requires = \
['netaddr']

setup_kwargs = {
    'name': 'bits-mhl',
    'version': '1.20.7',
    'description': 'BITS MHL',
    'long_description': '# bits-mhl\nBITS MHL Python Library\n',
    'author': 'Lukas Karlsson',
    'author_email': 'karlsson@broadinstitute.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/broadinstitute/bits-mhl.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
