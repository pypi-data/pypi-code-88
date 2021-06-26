# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pynfogen', 'pynfogen.cli']

package_data = \
{'': ['*'], 'pynfogen': ['art/*', 'templates/*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'click>=8.0.0,<9.0.0',
 'dunamai>=1.5.5,<2.0.0',
 'pycountry>=20.7.3,<21.0.0',
 'pyd2v>=1.3.0,<2.0.0',
 'pymediainfo>=5.1.0,<6.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['nfo = pynfogen.cli:cli']}

setup_kwargs = {
    'name': 'pynfogen',
    'version': '0.4.2',
    'description': 'Scriptable MediaInfo-fed NFO Generator for Movies and TV',
    'long_description': '# pynfogen\n\nScriptable MediaInfo-fed NFO Generator for Movies and TV.\n\n## Installation\n\n    pip install --user pynfogen\n\n### Or, Install from Source\n\n#### Requirements\n\n1. [pip], v19.0 or newer\n2. [poetry], latest recommended\n\n#### Steps\n\n1. `poetry config virtualenvs.in-project true` (optional, but recommended)\n2. `poetry install`\n3. You now have a `.venv` folder in your project root directory. Python and dependencies are installed here.\n4. To use the venv, follow [Poetry Docs: Using your virtual environment]\n\nNote: Step 1 is recommended as it creates the virtual environment in one unified location per-project instead of\nhidden away somewhere in Poetry\'s Cache directory.\n\n  [pip]: <https://pip.pypa.io/en/stable/installing>\n  [poetry]: <https://python-poetry.org/docs>\n  [Poetry Docs: Using your virtual environment]: <https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment>\n\n## Usage\n\n### Introduction\n\nUsing pynfogen is fairly simple. You have a configuration file ([config.yml](config.yml)) which holds external\ninformation about the file(s) you are feeding to the output NFO, including templates and artwork.\n\nWhen generating an NFO (by running [pynfogen.py](pynfogen.py)) it reads the primary input file for mediainfo (metadata)\nusing pymediainfo and use that information in the output NFO wherever the template asks.\n\n- Artwork files ([/art](/art)): Should only contain artwork that goes around the template contents.\n  Generally no scripting should be made.\n- Template files ([/templates](/templates)): These are the main scriptable files. You can make templates for specific\n  scenarios like TV, Movies, Episodes, etc. If you are changing a template often, consider putting the changes as a new\n  template instead, or perhaps as part of the artwork.\n\n### Copyright Agreement for included Artwork and Template files\n\nThere\'s already example template files and artwork files for you to look at.\nHowever, the Artwork files are copyright to whomever committed them where-as the templates are not copyright.\nThe copyrighted files may not be used, even under the conditions of the License, except for viewing as examples.\nNo derivative work is permitted based on their general concept.\nSimply remember that artwork files are themselves pieces of Art, and should be treated as such.\n\n### Text-encoding\n\nTraditional NFOs expect to use the codepage 437 (cp437) "ascii" text-encoding.\npynfogen generally doesn\'t care what you use, but may not respect you\'re choice correctly in the NFO output.\nIt has not been set up for specific text-encoding choice and generally speaking UTF-8 is expected.\n\n### Scripting\n\nThe scripting system used by pynfogen is by no means ideal. It is however, consistent.\nIt\'s mostly a mix of python\'s normal new-style string formatting, with custom formatters.\nIt also uses a PHP-like `<?{x:y}..?>` custom syntax for if statements.\n\n#### If statement\n\nFor example the following will check if the `{note}` variable (python new-style formatting) is a truthy value,\nand only if so, print it:\n\n    # note = "Hello World!"\n    <?{note:true}Has note: {note}?>\n    # returns: `Has note: Hello World!`\n\n    # note = ""  # or None, 0, False, 1==2, e.t.c\n    <?{note:true}Has note: {note}?>\n    # returns: ``\n\nIt\'s obvious this is in no way good syntax for `if` statements (no `else` or `elif` support either), but it works.\n\nIt uses `1` and `0` in the `<?{here}?...>` section to determine if it should print or not.\nEssentially speaking any time the If statement is used, you should be using the [Boolean custom formatter](#boolean).\n\n#### Custom Formatting\n\nThe following custom additional formatting to pythons new-style formatting is available:\n\n##### Chaining\n\nExample: `{var:bbimg:layout,2x2x0}`\n\nUsing `:` you can chain formatter results from left to right, passing previous value as it goes on.\nThe previous value does not necessarily need to be used.\n\nFor less confusion, since `:` is already used as standard in new-string formatting, look at the above example as\n`{(var:bbimg):(layout,2x2x0)}`\n\n##### Boolean\n\nExample: `{var:true}` or `{var:!false}`.  \nType-hint: func(var: Any) -> Fixed\\[1, 0]\n\nReturns `1` if `var` is a truthy value, otherwise `0`.\n\nThere\'s also `{var:false}` and `{var:!true}` which is the flip-reverse of the above result.\n\n##### BBCode Image Links\n\nExample: `{var:bbimg}`  \nType-hint: bbimg(var: Union\\[List\\[dict], dict]) -> Union\\[List\\[str], str]  \nEach dictionary: e.g. `{url: \'https://url/to/image/page\', src: \'https://url/to/image/src.png\'}`\n\nEvery dictionary is converted to BBCode `[IMG]` wrapped in `[URL]`. For example:\n`[URL=https://url/to/image/page][IMG]https://url/to/image/src.png[/IMG][/URL]`\n\nReturns a list of converted bbcode strings, or a single string if only one dictionary was provided.\n\n##### Layout\n\nExample: `{var:layout,3x2x1}`  \nType-hint: layout(var: Union\\[List\\[Any], Any], width: int, height: int, spacing: int) -> str\n\nLays out items in a grid-like layout, spacing out items using spaces (or new lines) as specified.\nNew-lines are used when spacing vertically.\n\n##### Wrapping\n\nExample: `{var:>>2x68}`  \nType-hint: wrap(var: Any, indent: int, wrap: int)\n\nText-wrap to a specific length. Each subsequent new-line caused by the wrapping can be intended (or not if 0).\n\n##### Centering\n\nExample: `{var:^>70x68}`  \nType-hint: center(var: Any, centering: int, wrap: int)\n\nCenters and also Text-wraps (while also centering wraps) to a specific width.\n',
    'author': 'PHOENiX',
    'author_email': 'rlaphoenix@pm.me',
    'maintainer': 'PHOENiX',
    'maintainer_email': 'rlaphoenix@pm.me',
    'url': 'https://github.com/rlaphoenix/pynfogen',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
