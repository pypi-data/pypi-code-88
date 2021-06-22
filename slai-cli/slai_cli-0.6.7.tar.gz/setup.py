# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slai_cli',
 'slai_cli.init',
 'slai_cli.model',
 'slai_cli.model.templates',
 'slai_cli.modules',
 'slai_cli.profile']

package_data = \
{'': ['*'], 'slai_cli.init': ['templates/*']}

install_requires = \
['Columnar>=1.3.1,<2.0.0',
 'Flask-Cors>=3.0.9,<4.0.0',
 'Flask>=1.1.2,<2.0.0',
 'GitPython>=3.1.11,<4.0.0',
 'Jinja2>=2.11.2,<3.0.0',
 'PyDrive>=1.3.1,<2.0.0',
 'boto3>=1.16.44,<2.0.0',
 'celery==5.0.2',
 'click>=7.1.2,<8.0.0',
 'dill>=0.3.3,<0.4.0',
 'docker>=5.0.0,<6.0.0',
 'python-dotenv>=0.15.0,<0.16.0',
 'redis>=3.5.3,<4.0.0',
 'shtab>=1.3.4,<2.0.0',
 'slai==0.1.40']

entry_points = \
{'console_scripts': ['slai = slai_cli:main.main']}

setup_kwargs = {
    'name': 'slai-cli',
    'version': '0.6.7',
    'description': '',
    'long_description': None,
    'author': 'slai',
    'author_email': 'luke@slai.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
