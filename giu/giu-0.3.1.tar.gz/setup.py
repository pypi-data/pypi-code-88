# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['giu']

package_data = \
{'': ['*']}

install_requires = \
['atoml>=1.0.1,<2.0.0',
 'click>=8.0.1,<9.0.0',
 'halo>=0.0.31,<0.0.32',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['giu = giu.cli:giu']}

setup_kwargs = {
    'name': 'giu',
    'version': '0.3.1',
    'description': 'Gandi LiveDNS Updater - commnand line tool to keep your dynamic ip up to date',
    'long_description': "# GIU\nGandi LiveDNS Updater - Command line tool to keep your dynamic ip up to date.\n\n[![yriveiro](https://circleci.com/gh/yriveiro/giu.svg?style=svg)](https://circleci.com/gh/yriveiro/giu)\n\n[![Downloads/Week](https://static.pepy.tech/personalized-badge/giu?period=week&units=international_system&left_color=black&right_color=orange&left_text=Downloads/Week)](https://pepy.tech/project/giu) [![Downloadsi/Month](https://static.pepy.tech/personalized-badge/giu?period=month&units=international_system&left_color=black&right_color=orange&left_text=Downloads/Month)](https://pepy.tech/project/giu) [![Downloads](https://static.pepy.tech/personalized-badge/giu?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/giu)\n\n## Prequisites\n\n* A valid key fro Gandi LiveDNS API. Use https://account.gandi.net/en/users/USER/security\n(`USER` is your Gandi user account).\n* Python 3.\n\n## Installation\n\nThe recommended way to install this package is through [pip](https://pip.pypa.io/en/stable/).\n\n```shell\npip install --user giu\n```\n\n## Usage\n\nTo use `giu` you need to create a `config.toml` file to hold the minimal set of\nconfigurations.\n\n```toml\n[api]\nurl = 'https://dns.api.gandi.net/v5/livedns'\nkey = 'YOUR_KEY'\n\n[dns]\ndomain = 'example.com'\nrecords = [\n    {'type' = 'A', 'name' = '@', 'ttl' = 18000},\n]\n\n[resolver]\nproviders = [\n    'http://ipecho.net/plain',\n    'https://ifconfig.me/ip',\n    'http://www.mon-ip.fr'\n]\n```\n\n### One shot\nIn this example the config file was created on `$HOME/.giu/example.com.toml`.\n\n```shell\ngiu sync --conf $HOME/.giu/example.com.toml\n```\n\n### Cronjob\nIn this example the config file was created on `$HOME/.giu/example.com.toml`.\n\n```shell\n$ crontab -e\n* */2 * * * giu sync --conf $HOME/.giu/example.com.toml\n```\n\n### Docker\nIn this example the config is mounted as part of a config folder.\n\n```shell\ndocker run -it --rm -v config-folder:/tmp/ yriveiro/giu:latest giu sync --config /tmp/config.toml\n```\n\n## Improvements\n\nSome improvements that I have ff the top of my head:\n\n* `put` command to create entries like CNAMES and so on.\n* `delete` command to delete entries\n* `backup` command to do backups\n* ~~Docker Image to run giu with docker compose or as a Cronjob on Kubernetes.~~\n",
    'author': 'Yago Riveiro',
    'author_email': 'yago.riveiro@gmail.com',
    'maintainer': 'Yago Riveiro',
    'maintainer_email': 'yago.riveiro@gmail.com',
    'url': 'https://github.com/yriveiro/giu',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
