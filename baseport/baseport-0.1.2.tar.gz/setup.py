# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['baseport']

package_data = \
{'': ['*']}

install_requires = \
['basecampy3>=0.4.0,<0.5.0',
 'click>=8.0.1,<9.0.0',
 'html2text>=2020.1.16,<2021.0.0']

entry_points = \
{'console_scripts': ['baseport = baseport.cli:cli']}

setup_kwargs = {
    'name': 'baseport',
    'version': '0.1.2',
    'description': 'Export Basecamp 3 To-Dos into a CSV.',
    'long_description': "# Baseport\n\nBaseport is a small CLI tool to export your Basecamp to-dos into a CSV file. We\nconsidered migrating to Jira, and I needed a way to pull all our Basecamp to-dos\ninto it, so I've written a quick script and thought I'd share it.\n\n## Install\n\n`pip install baseport`\n\n## Usage\n\n```\n$ baseport --help\nUsage: baseport [OPTIONS] COMMAND [ARGS]...\n\n  Baseport exports Basecamp 3 to-do lists to CSVs.\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  projects  Project operations\n  todos     To-Do lists operations\n\n$ baseport todos --help\nUsage: baseport todos [OPTIONS] COMMAND [ARGS]...\n\n  To-Do lists operations\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  export  Export all todos in one or all lists into a CSV file\n  ls      List all available to-do lists in a project\n  show    List all todos in one or all lists in a project\n\n```\n\nTo export all of the to-dos in a single project, you'll use something like this:\n\n```\nbaseport todos export -p PROJECT_ID -o todos.csv\n```\n\n### Authentication\n\nBaseport uses [`basecampy3`](https://github.com/phistrom/basecampy3) to talk to\nBasecamp API. You'll need a `.conf` file with your OAuth app client_id and\nsecret, and OAuth token. Luckily, you can just run `bc3 configure` and it'll\nguide you through the setup proces.\n\n### Formatting and cleaning your CSV\n\nWe needed to do a bit of a company-specific cleanup (given that I needed to\nimport to-dos to Jira, and clean up our email addresses), so Baseport has\nformatter support. You can implement your own formatter and add it to\n`_format_todos()` function, and then just pass it in the terminal with\n`--formatter` option.\n\n## Contributing\n\nFeel free to open a PR with additional formatters or documentation on how to use\n`baseport` for other platform-specific exports.\n\nIf you found an issue, please do file it on this repo. I'll do my best to help\nyou out.\n\nBaseport is not going to be actively maintained or developed, it's a one-off\nquick tool I needed for myself, and it did it's job.\n",
    'author': 'Nate Gadzhi',
    'author_email': 'nate@respawn.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nategadzhi/baseport',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
