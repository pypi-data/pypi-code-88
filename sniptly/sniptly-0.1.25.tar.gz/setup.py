# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sniptly']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'click>=7.1.2,<8.0.0',
 'jstyleson>=0.0.2,<0.0.3',
 'rich>=10.3.0,<11.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['sniptly = sniptly.cli:index']}

setup_kwargs = {
    'name': 'sniptly',
    'version': '0.1.25',
    'description': 'Build code snippets for vscode',
    'long_description': '# Sniptly\n\nA Python command line tool for managing [user defined code snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets) in code for [vscode](https://code.visualstudio.com/).\n\nSniptly makes it possible to mantain code snippets in code and build the json representation vscode uses for code snippets when needed. Maintaining snippets in code is more convenient and allows one to benefit from code formatters or, for larger code snippet libraries, to have unit tests for the snippets.\n\nSniptly is at experimental stage for now. It is tested to some extent with Python. In principle, it *should* work with other languages as well.\n\n# Installation\n\nTo install the latest release on PYPI run\n\n```\npip install sniptly\n```\n# Usage\n\n- Create configuration file by running `snitply create-config`\n- Edit the newly created `sniptly.toml` configuration file by adding the languages you wish to create code snippets for. By default the configuration specifies to look for python and javascript files.\n- **NOTE**: Sniptly tries to figure out the folder where vscode keeps user snippets. Verify that the `vscode_snippets_dir` configuration has the correct value.\n- Optional steps with first time usage\n    - Run `sniptly create-sample` to create a sample file named `python_sniptly_snippets.py` with sniptly comments. See [the file contents](#sample) to understand how comments are used to turn code fragments to user defined code snippets in vscode.\n    - Run `sniptly build --source python_sniptly_snippets.py` to build the code snippet and to add the snippet to your existing vscode snippets.\n    - Add sniptly code snippet template by running `sniptly add-snippet-template --lang [language, for example: python]`. Code from which to generate code snippets is commented with special comments. By adding the template as a code snippet it\'s easy to turn existing code fragments to vscode snippets.\n- Start adding sniptly comments for the code fragments you want to turn into vscode snippets\n- Run `sniptly build --source [file or folder]` to build code snippets from the specified file or folder for the languages you have enabled in `sniptly.toml`\n\n# Syntax for marking code fragments for snippet creation\n\nThe start sequence will specify where the snippet starts. The following lines specify name, prefix and description that will be used in the vscode\'s json representation for user defined code snippets. The end sequence ends the snippet.\n\nSyntax can be modified via `sniptly.toml`. The `{}` in `start_sequence` and `stop_sequence` will be replaced by the value set in `comment_character`.\n\n See the sample file contents below to see how code fragments can be marked for snippet creation.\n\n<a id="sample"></a>\n# Example of Python code fragment marked for snippet creation\n\n```python\n# -->\n# name: [my awesome snippet]\n# prefix: [prefix for my awesome snippet]\n# description: [snippet description]\nimport json\ndata = {"foo": "bar"}\ndata_as_json = json.dumps(data, indent=2)\nwith open("file.json", "w") as f:\n    f.write(data_as_json)\n# <--\n```',
    'author': 'jjaakko',
    'author_email': 'devjaakko@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jjaakko/sniptly',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
