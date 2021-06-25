# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nemosyne']

package_data = \
{'': ['*']}

install_requires = \
['CacheControl==0.12.6',
 'appdirs==1.4.3',
 'boto3==1.17.96',
 'botocore==1.20.96',
 'certifi==2019.11.28',
 'chardet==3.0.4',
 'click==7.1.2',
 'colorama==0.4.3',
 'contextlib2==0.6.0',
 'distlib==0.3.0',
 'distro==1.4.0',
 'html5lib==1.0.1',
 'idna==2.8',
 'ipaddr==2.2.0',
 'jmespath==0.10.0',
 'lockfile==0.12.2',
 'msgpack==0.6.2',
 'packaging==20.3',
 'pep517==0.8.2',
 'progress==1.5',
 'pyparsing==2.4.6',
 'python-dateutil==2.8.1',
 'python-dotenv==0.17.1',
 'pytoml==0.1.21',
 'requests==2.22.0',
 'retrying==1.3.3',
 's3transfer==0.4.2',
 'six==1.14.0',
 'typer==0.3.2',
 'urllib3==1.25.8',
 'webencodings==0.5.1']

entry_points = \
{'console_scripts': ['nemosyne = nemosyne.main:app']}

setup_kwargs = {
    'name': 'nemosyne',
    'version': '0.0.1',
    'description': 'nemosyne (aka [Mnemosyne](https://en.wikipedia.org/wiki/Mnemosyne)) is an S3 command-line manager.WIP',
    'long_description': 'nemosyne (aka [Mnemosyne](https://en.wikipedia.org/wiki/Mnemosyne)) is an S3 command-line manager.\n',
    'author': 'Ali Tavallaie',
    'author_email': 'a.tavallaie@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
