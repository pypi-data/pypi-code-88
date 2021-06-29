# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['thankyou']
setup_kwargs = {
    'name': 'thankyou',
    'version': '0.0.1',
    'description': 'Python module to print Thank You in every known language.',
    'long_description': '# thanks\nPython module to print "Thanks/Thank you" in every known language.  \nInstall it, import it and use it with \n```python\nfrom thankyou import give_thanks\nthanks = give_thanks()\n```\n',
    'author': 'Mario Hernandez',
    'author_email': 'mariofix@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mariofix/thankyou',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
