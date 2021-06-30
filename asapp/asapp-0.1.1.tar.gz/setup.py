# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asapp']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0', 'click>=8.0.1,<9.0.0']

entry_points = \
{'console_scripts': ['asapp = asapp.main:asapp']}

setup_kwargs = {
    'name': 'asapp',
    'version': '0.1.1',
    'description': 'Create desktop entries for running websites in app mode.',
    'long_description': "# asapp\n\nOpen websites in Chromium's app mode.\n\n## Motivation\n\nI use several GSuite apps such as Google Sheets and Google Docs, but there are not suitible \nlinux clients available for these apps. Running them in [app](https://superuser.com/questions/33548/starting-google-chrome-in-application-mode) mode using the `--app` CLI option\nis a good substitute for this. \n\n## Installation\n\n### PyPi\n\n```shell script\npip install asapp\n```\n\n### Git Clone\n\n```shell script\ngit clone https://github.com/BlakeASmith/as_app.git\npip install . \n```\n\n## Usage\n\n### Open Websites\n\nLaunch a website in it's own window, without any borders or browser options. \n\n```shell script\nasapp open https://duckduckgo.com\n```\n\n### Create a Desktop Entry\n\n```shell script\nasapp shortcut --name DuckDuckGo https://duckduckgo.com\n```\n\nThis will add a `.desktop` file to the `~/.local/share/applications/` folder, causing\n`DuckDuckGo` to appear in your app launcher of choice!\n",
    'author': 'Blake Smith',
    'author_email': 'blakeinvictoria@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
