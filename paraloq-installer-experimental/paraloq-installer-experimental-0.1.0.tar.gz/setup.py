# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['paraloq', 'paraloq.installer']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.17.14,<2.0.0',
 'click>=8.0.1,<9.0.0',
 'pydantic>=1.8.1,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'rich>=10.1.0,<11.0.0',
 'typing-extensions>=3.10.0,<4.0.0']

extras_require = \
{':platform_system == "Windows"': ['pywin32>=300,<301']}

entry_points = \
{'console_scripts': ['pq = paraloq.installer.cli:paraloq']}

setup_kwargs = {
    'name': 'paraloq-installer-experimental',
    'version': '0.1.0',
    'description': 'Facilitates installing paraloq software.',
    'long_description': '# Paraloq\n\nThis is the core package for the paraloq software products. For more information, please refere\nto the docs on GitHub.\n',
    'author': 'Maximilian Arrich',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
