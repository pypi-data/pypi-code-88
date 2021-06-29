# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nork',
 'nork.cli',
 'nork.commands',
 'nork.core',
 'nork.framework',
 'nork.framework.commands',
 'nork.framework.routing',
 'nork.framework.server']

package_data = \
{'': ['*']}

install_requires = \
['fnc>=0.5.2,<0.6.0', 'toml>=0.10.2,<0.11.0', 'typer[all]>=0.3.2,<0.4.0']

extras_require = \
{'framework': ['fastapi[all]>=0.65.2,<0.66.0']}

entry_points = \
{'console_scripts': ['nork = nork.cli:app']}

setup_kwargs = {
    'name': 'nork',
    'version': '0.1.12',
    'description': 'CLI for open source PaaS and framework.',
    'long_description': '# NOR/K\nCLI for open source PaaS and framework.\n\n## Installation\nInstallation is automated with the following command:\n\n```bash\n/bin/bash -c "$(curl -fsSL https://nork.link/CLI-install)"\n```\n',
    'author': 'NORK',
    'author_email': 'support@nork.sh',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://nork.sh',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
