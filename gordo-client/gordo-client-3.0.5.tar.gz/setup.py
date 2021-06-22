# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gordo_client', 'gordo_client.cli']

package_data = \
{'': ['*']}

install_requires = \
['cachetools>=4.0,<5.0',
 'click>=7.1.2,<8.0.0',
 'gordo-dataset>=2.6.4,<3.0.0',
 'influxdb>=5.3.0,<6.0.0',
 'numpy>=1.18,<2.0',
 'pandas>=1.0,<2.0',
 'pyarrow>=0.17.1,<0.18.0',
 'pydantic>=1.7.3,<2.0.0',
 'requests>=2.20,<3.0',
 'scikit-learn>=0.23,<1.0',
 'simplejson>=3.17.2,<4.0.0',
 'wrapt>=1.11,<2.0']

entry_points = \
{'console_scripts': ['gordo-client = gordo_client.cli.client:gordo_client']}

setup_kwargs = {
    'name': 'gordo-client',
    'version': '3.0.5',
    'description': 'Gordo client',
    'long_description': '# Gordo client\nClient for [Gordo](https://github.com/equinor/gordo) project.\n\n# Table of Contents\n* [Installation.](#Installation)\n* [Development Tools.](#Development-Tools)\n    * [Setup.](#Setup)\n        * [Setup Virtual Environment.](#Setup-Virtual-Environment)\n    * [Automated Tasks.](#Automated-Tasks)\n    \n# Installation\nIn order to install or uninstall this library run following commands.\n```bash\n# Install\npip install gordo-client\n\n# Uninstall\npip uninstall gordo-client\n```\nAfter installation client can be accessed as a library or by command line.\n```bash\nUsage: gordo-client [OPTIONS] COMMAND [ARGS]...\n\n  Entry sub-command for client related activities.\n\nOptions:\n  --version                   Show the version and exit.\n  --project TEXT              The project to target\n  --host TEXT                 The host the server is running on\n  --port INTEGER              Port the server is running on\n  --scheme TEXT               tcp/http/https\n  --batch-size INTEGER        How many samples to send\n  --parallelism INTEGER       Maximum asynchronous jobs to run\n  --metadata KEY_VALUE_PAR    Key-Value pair to be entered as metadata labels,\n                              may use this option multiple times. to be\n                              separated by a comma. ie: --metadata key,val\n                              --metadata some key,some value\n  --session-config SAFE_LOAD  Config json/yaml to set on the requests.Session\n                              object. Useful when needing to\n                              supplyauthentication parameters such as header\n                              keys. ie. --session-config {\'headers\': {\'API-\n                              KEY\': \'foo-bar\'}}\n  --help                      Show this message and exit.\n\nCommands:\n  download-model  Download the actual model from the target and write to an...\n  metadata        Get metadata from a given endpoint.\n  predict         Run some predictions against the target.\n```\n\n### Development Tools.\n\n#### Setup.\nWe use [invoke](http://www.pyinvoke.org/) and \n[poetry](https://python-poetry.org/) to speed up the development.\n\nYou need to install them only once.\n\nThe simplest way to get both is to install [poetry](https://python-poetry.org/)\nfirst, with the officially recommended way:\n```\ncurl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python\n```\nYou may need to run following command then:\n```\necho \'export PATH="$PATH:$HOME/.poetry/bin"\' >> $HOME/.zshrc\n```\n\n(Check out alternative instructions for `poetry` installation \n[here](https://python-poetry.org/docs/#installation))\n\nAfter that [poetry](https://python-poetry.org/) is able to automatically\nprovide you with `invoke` installed in the project virtual env.  So you can\ndo one of following [task](#Automated-Tasks):\n```\n# Run it directly\npoetry run inv [task]\n\n# Run it from the virtual environment\npoetry shell\ninv [task]\n\n# Have an alias (use custom name to avoid clashing with `inv` and `invoke`)\nalias invv=\'poetry run inv\'\ninvv [task]\n```\n\nAn alternative way to install all tools is using \n[pipx](https://pipxproject.github.io/pipx/):\n\n```\npython3.7 -m pip install pipx --user\npipx install poetry\npipx install invoke\n```\n##### Setup Virtual Environment.\nRun `poetry install` to install or re-install all dependencies.\n\nRun `poetry update` to update the locked dependencies to the most recent\nversion, honoring the constrains put inside `pyproject.toml`.\n\n\n#### Automated Tasks.\n[invoke](http://www.pyinvoke.org/) is used to run some common tasks.\nRun one of these from the root of the project.\n\n```\ninv fmt       # Apply automatic code formatting.\ninv check     # Run static checks.\ninv test      # Run tests.\n```\n\nThe tasks may be chained as following: `inv fmt check test`.\n\nThe tasks are defined in [tasks.py](./tasks.py) file.\nRun `inv -l` to see a list of all available tasks.\n',
    'author': 'Equinor ASA',
    'author_email': 'fg_gpl@equinor.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/equinor/gordo-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
