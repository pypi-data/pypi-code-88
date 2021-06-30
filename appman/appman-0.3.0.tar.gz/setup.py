# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['appman',
 'appman.data',
 'appman.data.formulas',
 'appman.data.packages',
 'appman.data.packages.apps',
 'appman.data.packages.backend',
 'appman.data.packages.backend.node',
 'appman.data.packages.backend.python',
 'appman.data.packages.drivers',
 'appman.data.packages.extensions',
 'appman.data.packages.extensions.vscode',
 'appman.data.packages.fonts',
 'appman.data.packages.provisioned',
 'appman.data.user']

package_data = \
{'': ['*']}

install_requires = \
['PyInquirer>=1.0.3,<2.0.0', 'click>=8.0.1,<9.0.0', 'pyyaml>=5.3.1,<6.0.0']

entry_points = \
{'console_scripts': ['appman = appman.cli:main']}

setup_kwargs = {
    'name': 'appman',
    'version': '0.3.0',
    'description': 'Cross-platform application management aggregator',
    'long_description': '# appman\n\nappman is cross-platform application management aggregator\n\n[![Build Status](https://travis-ci.com/basiliskus/appman.svg?branch=main)](https://travis-ci.com/basiliskus/appman)\n\n<p align="center"><img src="/docs/demo.gif?raw=true"/></p>\n\n## Requirements\n\n- Python 3.9\n\n## Installation\n\nYou can install appman from [PyPI](https://pypi.org/project/appman/):\n\n```bash\n> pip install appman\n```\n\n## How to use\n\n### Set up you user package list\n\n- Add a package to your user packages list\n\n    Using interactive mode:\n    ```console\n    $ appman add\n\n    [?] Select the package type: (Use arrow keys)\n    >app\n     font\n     driver\n     provisioned\n     backend\n     extension\n\n    [?] Select app packages to add: (<up>, <down> to move, <space> to select, <a> to toggle, <i> to invert)\n     ○ curl\n     ○ fzf\n    >● git\n     ○ jq\n     ○ python\n     ○ ...\n\n    Added git package\n    ```\n\n    or directly passing parameters:\n    ```console\n    $ appman add -pt app -id git\n    ```\n\n- Remove a previously added package\n\n    Using interactive mode:\n    ```console\n    $ appman add\n\n    [?] Select the package type: (Use arrow keys)\n    >app\n     font\n     driver\n     provisioned\n     backend\n     extension\n\n    [?] Select app packages to remove: (<up>, <down> to move, <space> to select, <a> to toggle, <i> to invert)\n     ○ 7zip\n     ○ curl\n    >● git\n     ○ ...\n\n    Removed git package\n    ```\n\n    Directly passing parameters:\n    ```console\n    $ appman remove -pt app -id git\n    ```\n\n- Show your user packages list\n\n    Using interactive mode:\n    ```console\n    $ appman list\n\n    [?] Select the package type: (Use arrow keys)\n    >app\n\n     • 7zip (cli, utils)\n     • curl (cli, utils)\n    ```\n\n    Directly passing parameters:\n    ```console\n    $ appman list -pt app\n    ```\n\n- Search all available packages to add\n\n    Using interactive mode:\n    ```console\n    $ appman search\n\n    [?] Select the package type: (Use arrow keys)\n    >app\n\n    7zip\n    ack\n    apache2\n    aria2\n    bottom\n    broot\n    cookiecutter\n    curl\n    ...\n    ```\n\n    Directly passing parameters:\n    ```console\n    $ appman search -pt app\n    ```\n\n### Install/Uninstall packages in your user packages list\n\nUsing interactive mode:\n```console\n$ appman install\n\n[?] Select the package type: (Use arrow keys)\n>app\n\nInstalling 7zip...\nInstalling ack...\n...\n```\n\nDirectly passing parameters:\n```console\n$ appman install -pt app -id 7zip\n```\n\n### Using labels\n\nAll packages have pre-defined labels (e.g. for apps: \'cli\' & \'gui\'), but you can also add your own labels by passing the --labels/-l parameter to the \'add\' command. \n\n```console\n$ appman add -pt app -id 7zip -l server\n```\n\nYou can also filter by labels when using the \'list\', \'search\', \'remove\', \'install\' or \'uninstall\' commands\n\n```console\n$ appman list -pt app -l server\n```\n\n## License\n\n© Basilio Bogado. Distributed under the [MIT License](LICENSE).\n',
    'author': 'Basilio Bogado',
    'author_email': '541149+basiliskus@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/basiliskus/appman',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
