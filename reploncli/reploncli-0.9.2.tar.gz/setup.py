# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reploncli']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'reploncli',
    'version': '0.9.2',
    'description': 'REPL extension to CLI apps',
    'long_description': '# REPL on CLI\n\nREPL extension to CLI apps\n\n### Example\n\n```python\nimport sys\nfrom reploncli import reploncli\n\nimport my_cli_function, show_help\n\n# turn on REPL mode if the first command line argument is \'repl\'\nlets_start_in_repl_mode = (sys.argv[1:] or [\'\'])[0] == "repl"\n\nreploncli(my_cli_function, lets_start_in_repl_mode, show_help, ">>> ")\n```\n\n### reploncli()\n\nSignature:\n```python\ndef reploncli(cli_function, repl_mode=None, help=None, prompt=""):\n    ...\n```\n\nIf `repl_mode is True` then REPL mode starts.\n\n### Wrap your CLI entry point\n\nCreate `cli_function` by wrapping your CLI entry point that accepts one optional argument with `args` to use as a replacement for `sys.argv` if given.  \nOtherwise process `sys.argv` as normal.\n\n### Shell commands\n\nIf an input in REPL mode starts with `.` then it\'s run by `os.system()` after removing that dot.\n',
    'author': 'silkyanteater',
    'author_email': 'cyclopesrufus@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/silkyanteater/reploncli',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
