# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyjsonedit']

package_data = \
{'': ['*']}

install_requires = \
['coverage==5.5', 'pylint==2.8.2', 'pytest==6.2.4']

entry_points = \
{'console_scripts': ['pyjsonedit-mask = pyjsonedit.cli:run_mask',
                     'pyjsonedit-modify = pyjsonedit.cli:run_modify']}

setup_kwargs = {
    'name': 'pyjsonedit',
    'version': '1.0.4',
    'description': 'Edit parts of json strings & files while keeping the orginal, inconsistent formating',
    'long_description': '# pyJsonEdit\n\n[![PyPi version](https://badge.fury.io/py/pyjsonedit.svg)](https://pypi.org/project/pyjsonedit/)\n[![license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)]()\n[![tests](https://github.com/UrbanskiDawid/pyJsonEditor/actions/workflows/tests.yaml/badge.svg)](https://github.com/UrbanskiDawid/pyJsonEditor/actions/workflows/tests.yaml)\n\n[![](https://forthebadge.com/images/badges/made-with-python.svg)]()\n[![](https://forthebadge.com/images/badges/powered-by-coffee.svg)]()\n[![](https://forthebadge.com/images/badges/uses-badges.svg)]()\n\n\nEdit parts of inconsistently formatted json.\n\nIt\'s just a bit slower that doing this by hand!\n\n# matcher\n\nNow you can easly select **nodes** in json tree\n\nsyntax:\n\nselector | action | node type | comments\n---------|--------|-------|-------\n  *| select **all** items in current node| - |\n [n] | select **n-th** item of curent node| array|\n {n} | select **n-th** item of curent node| object|\n key | select node chilld **by name**| object|\n"key"| select node chilld **by name**| object|\n \\>  | mark current node as seleced |-|\n a=b | check if current node has child \'a\' with value \'b\' |object|\n| :before | add text before selected node| -| must at end of pattern\n| :after | add text after selected node  | -| must at end of pattern\n\nexample 1: \n\n```\nkey > [0]\n```\n\nthis pattern will match one element by:\n\n1. selecting "key" element in root node (assuring that is an object)\n2. select first element in it (assumintg its an array) \n\nexample 2: \n\n```\nname > *\n```\n\nthis pattern will match multiple elements by:\n\n1. selecting "name" element in root node (assuring that is an object)\n2. select all element in it \n\n## how to install\n\n```bash\npip install --upgrade pyjsonedit\n```\n\n## python module\n\n```python\nimport pyjsonedit\n```\n## comand line - mark\n\n```sh\n$ pyjsonedit-mask --help\n```\n\n```\nUsage: pyjsonedit-mask [OPTIONS] PATTERN [JSONS]...\n\n  Select and mask parts of json\n\nOptions:\n  --symbol TEXT\n  -i, --insert   save changes to file\n  --help         Show this message and exit.\n```\n\nexample:\n```\npyjsonedit-mask "pass" "{\'pass\':123}"\n{\'pass\':XXX}\n```\n## comand line - modify\n\n```sh\n$ pyjsonedit-modify --help\n```\n```\nUsage: pyjsonedit-modify [OPTIONS] PATTERN TEMPLATE [JSONS]...\n\n  select and modify parts of json\n\nOptions:\n  -i, --insert  save changes to file\n  --help        Show this message and exit.\n```\n\nexample 1: simple string\n```\npyjsonedit-modify "pass" \'P@$W&$d\' "{\'pass\':123}"\n{\'pass\':P@$W&$d}\n```\n\nexample 2: python code:\n\nfile **/home/dave/somefile.py**\n```python\n#!/usr/bin/python3\ndef modify(node,ctx):\n   return "\'<"+str(1)+">\'"\n```\nnode - matched node\n\nctx - context in witch node was matched: file_name & match_nr\n\n```bash\npyjsonedit-modify "*" /home/dave/somefile.py "{\'a\':1}"\n{\'a\':\'<1>\'}\n```\n\n## example: mask multiple nodes\n```\n$ pyjsonedit-mask **"quiz > * > q1 >*"** DOC/example.json\n```\n\n```\n{\n    "quiz": {\n        "sport": {\n            "q1": {\n                "question": XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX,\n                "options": XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX,\n                "answer": XXXXXXXXXXXXXXX\n            }\n        },\n        "maths": {\n            "q1": {\n                "question": XXXXXXXXXXX,\n                "options": XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX,\n                "answer": XXXX\n            },\n            "q2": {\n                "question": "12 - 8 = ?",\n                "options": [\n                    "1",\n                    "2",\n                    "3",\n                    "4"\n                ],\n                "answer": "4"\n            }\n        }\n    }\n}\n```\n\n## example: mask selected nodes\n\n```python\n$ import pyjsonedit\n$ pyjsonedit.string_match_mark("{\'pass\':123}","pass")\n{\'pass\':XXX}\n```\n\n[![string_match_mark](https://github.com/UrbanskiDawid/pyJsonEditor/raw/master/DOC/mask_pass.gif)]()\n\n\n## project stats\n\n[![string_match_mark](https://github.com/UrbanskiDawid/pyJsonEditor/raw/master/DOC/stats_boilerplate.png)]()',
    'author': 'Dawid Urbanski',
    'author_email': 'kontakt@dawidurbanski.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/UrbanskiDawid/pyJsonEditor',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
