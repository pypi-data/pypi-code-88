# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['git_identity']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.18,<4.0.0',
 'argcomplete>=1.12.3,<2.0.0',
 'dataclasses-json>=0.5.4,<0.6.0',
 'jsonschema>=3.2.0,<4.0.0',
 'xdg>=5.1.0,<6.0.0']

entry_points = \
{'console_scripts': ['git-identity = git_identity:main']}

setup_kwargs = {
    'name': 'git-identity',
    'version': '1.0.0',
    'description': 'Quickly set user.name and user.email for a repository, based on a config file',
    'long_description': '# `git-identity`\n## Installation\nRecommended installation is with [`pipx`](https://pypi.org/project/pipx):\n```bash\npipx install git-identity\n```\n### Autocompletion\nAutocompletion is done with [`argcomplete`](https://pypi.org/project/argcomplete/). \nInstall, and add the following to your shell\'s startup scripts:\n```bash\neval "$(register-python-argcomplete git-identity)"\n```\n## Configuration\nThis project will look for `git-identity.json` in the XDG config folder (typically `$HOME/.config/`).\n```json\n{\n    "identities" : {\n        "alias": {\n            "name": "Alex Ample",\n            "email": "alexample@example.com"\n        }\n    }\n}\n```\n`alias` is what is used when invoking the command.\n## Usage\nAfter installation, you [may use this as a git subcommand](https://github.com/git/git/blob/670b81a890388c60b7032a4f5b879f2ece8c4558/Documentation/howto/new-command.txt) (though argcomplete only works when you invoke it as `git-identity`)\n```bash\ngit identity <alias>\n```\n',
    'author': 'Aatif Syed',
    'author_email': 'aatifsyedyp@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aatifsyed/git-identity',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
