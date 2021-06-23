# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asc2mb']

package_data = \
{'': ['*']}

install_requires = \
['click==8.0']

entry_points = \
{'console_scripts': ['asc2mb = asc2mb.asc2mb:main']}

setup_kwargs = {
    'name': 'asc2mb',
    'version': '0.4.3',
    'description': 'Manage your timetable by pasing the XML export from asc and format into two files suitable for upload into ManageBac',
    'long_description': '# aSc to ManageBac\n\n## Getting started\n\nRequires Python 3.6 or above. Install Python at [python.org](https://www.python.org). Installing Python also installs a package manager (called `pip`) that can install the command `asc2mb` into your command line enviornment.\n\nAfter instally Python, open the terminal or command line or PowerShell, and peform the following:\n\n```sh\npip install asc2mb\n```\n\nIf for some reason the `pip` command doesn\'t work, you can manually install it by following [the relevant instructions](https://pip.pypa.io/en/stable/installing/) for your system.\n\n### Upgrade\n\nShould you need to update to the latest version, you can do:\n\n```\npip install --upgrade asc2mb\n```\n\nAfter `pip install` worked, it is now installed on your path, and the command `asc2mb` is now available. \n\nThe command takes three required arguments, and there are additional options as well. The three required arguments tell the program where the xml file is located, and where to save the two csv files. \n\nThe options depend on your school\'s needs. For example, the class id is how ManageBac knows which class you are referring to, so that program helps you derive the class ID based on information contains in the xml file. It\'s up to you to ensure there are classes that have those IDs in managebac, but the program does produce a csv so that they can be uploaded in bulk.\n\nBy default, class id uses the pattern `{class_.short}_{division.name}`, which means "the short name of the class" plus an underscore, plus the name of the division. At the time of publication, having a different pattern is only possible by contacting the author (or, if you\'re a keen developer, add a pull request).\n\nIf you run the program without any options, it\'ll prompt you to enter them.\n\n```ssh\nasc2mb path_to_xml path_to_classes_output_file path_to_timetable_output_file\n```\n\n\n\n\n\n\n',
    'author': 'Adam Morris',
    'author_email': 'adam.morris@fariaedu.com',
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
