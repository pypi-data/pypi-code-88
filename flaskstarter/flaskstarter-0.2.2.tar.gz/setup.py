# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flaskstarter', 'flaskstarter.tools']

package_data = \
{'': ['*'], 'flaskstarter': ['templates/*']}

install_requires = \
['Jinja2==3.0.1', 'MarkupSafe==2.0.1', 'click==8.0.1']

entry_points = \
{'console_scripts': ['flaskstarter = flaskstarter.flaskstart_cli:flaskstarter']}

setup_kwargs = {
    'name': 'flaskstarter',
    'version': '0.2.2',
    'description': 'A Flask project start-up CLI to create a modular ready projects.',
    'long_description': "# flaskstarter\nA Flask project start-up CLI to create modular ready projects.\n\nFlaskstarter assumes you know about Flask microframework and its mechanics in a begginer level. It can be really helpfull if you are still using monolithic aproach, and needs to start using a modular architecture.\n\nIt also assumes you are using Python 3.6+.\n\nTo install flaskstarter use the usual:\n\n`pip install flaskstarter --require-hashes`\n\nTo see its help:\n\n`flaskstarter --help`\n\nTo start a project:\n\n`flaskstarter init project_name`\n\nTo see init's help:\n\n`flaskstarter init --help`\n\nNow, after project creation, you can enter on its directory and make full use of manage.py, a script with a CLI that may help you to automate some tasks inside project tree.\n\nBy now you can create a blueprint structure by typing the bellow on project root:\n\n`$ python manage.py create-blueprint [blueprint_name]`\n\nAfter that, remember to go onto app init file to register the blueprint on it. There is an EXTENSIONS variable where you can list all the plugins to autoimport. It uses factory design.\n\nTo run your app you can use the bellow on project root:\n\n`$ python manage.py runserver`\n\nAsk manage.py for runserver help to see its options.\n\n## What the project does for you\n\nIt creates project tree, a functional virtualenv on .venv, the init and routes files with a helloworld example and a manage.py script to run the project with the virtual enviroment created and attach blueprints to it. It now installs the requirements on project's .venv on POSIX systems. Feel free to change to poetry and pyproject.toml pattern.\n\nA word of warning: when commiting and pushing your project to versioning servers, remember to put instance folder into .gitignore, if not yet. And then remember to place it into deploy destination.\n\n## What the project does not do for you\n\nIt does not autoconfigure plugins on settings.toml yet. It doesn't force you to use pip, poetry or any other tool but flask and dynaconf on the Flask project created.\n\n## Future\n\nAdd more power to manage.py. Maybe autoconfigure plugins and blueprints on settings.toml.",
    'author': 'Felipe Bastos Nunes',
    'author_email': 'felipe.bastosn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/felipebastos/flaskstart',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
