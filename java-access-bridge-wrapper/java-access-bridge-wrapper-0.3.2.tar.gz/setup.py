# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['JABWrapper']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'java-access-bridge-wrapper',
    'version': '0.3.2',
    'description': 'Python wrapper for the Windows Java Access Bridge',
    'long_description': '\nPython wrapper around the Java Access Bridge / Windows Access Bridge.\n\n# Prerequisites\n\n* 64-bit Windows\n* Java >= 8 (https://docs.aws.amazon.com/corretto/latest/corretto-8-ug/downloads-list.html)\n* Python >= 3.7 (https://www.python.org/downloads/release/python-375/)\n* Install poetry: https://python-poetry.org/docs/\n\n# Test\n\nEnable the Java Access Bridge in windows\n\n* `C:\\path\\to\\java\\bin\\jabswitch -enable`.\n\nRun test script against simple Swing application\n\n* set environment variable `set RC_JAVA_ACCESS_BRIDGE_DLL=C:\\Program Files\\Java\\jre1.8.0_261\\bin\\WindowsAccessBridge-64.dll`\n* `poetry run python tests\\test.py`\n\n# Packaging\n\n* poetry build\n* poetry publish\n\n# TODO:\n\n* Support for 32-bit Java Access Bridge version\n* Add rest of the parsing functions\n* Better API to the ContextNode component\n\n',
    'author': 'Robocorp',
    'author_email': 'support@robocorp.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/robocorp/java-access-bridge-wrapper.git',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
