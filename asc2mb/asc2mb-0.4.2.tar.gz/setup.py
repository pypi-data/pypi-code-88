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
    'version': '0.4.2',
    'description': 'Manage your timetable by pasing the XML export from asc and format into two files suitable for upload into ManageBac',
    'long_description': "# aSc to ManageBac\n\n## Getting started\n\nRequires Python 3.6 or above. Install it.\n\nOpen the terminal or command line, and peform the following:\n\n```sh\npip install asc2mb\n```\n\nIf for some reason the `pip` command doesn't work, try the following:\n\n```\ncurl https://bootstrap.pypa.io/get-pip.py -o get-pip.py\npython3 get-pip.py\n```\n\nAfter `pip install` worked, it is now installed on your path, and the command `asc2mb` is not available. It takes three arguments, usage information can be found via typing the command with no arguments.\n\nIf there is some error with the arguments you supplied, such as cannot read the xml, or something else, it'll let you know.\n\n```ssh\nasc2mb path_to_xml path_to_classes_output_file path_to_timetable_output_file\n```\n\n\n\n",
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
