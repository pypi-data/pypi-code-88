# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['textfile']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'textfile',
    'version': '0.1.1',
    'description': 'Functions that enables us to write out or read from with text file in shorter syntax.',
    'long_description': '\nFunctions that enables us to write out or read from with text file in shorter syntax\nthan using only standard library.\n\nInstall\n-------\n\n::\n\n    pip install textfile\n\n\nUsage\n-----\n\nCreate file and write text to it::\n\n    >>> import textfile\n    >>> textfile.write("a.txt", "any string value")\n\nRead text from file::\n\n    >>> import textfile\n    >>> textfile.read("a.txt")\n    "any string value"\n\nThe benefit to use textfile\n---------------------------\n\nBy using ``textfile``, it is possible to shorten your program on a specific situation.\n\nIf you often write code like::\n\n    with open("somefile.txt") as f:\n        f.write("any string value")\n\nYou can rewrite those codes to::\n\n    textfile.write("somefile.txt", "any string value")\n\nAnd other functions in ``textfile`` library are made of the same consept.\n\nWhat situation does textfile fits?\n----------------------------------\n\nAPI that is simple to use, is less flexibility.\nIt means that, it is not recommended to use in such a programs that is required speed or strictness.\n\nBut I think that it will not be a matter in almost all situations of our programming.\n\nI courage you to use ``textfile`` as much as possible you can.\nIf you do so, increase the readability of your code and suppress the bug.\n\nIs this document written in strange English?\n--------------------------------------------\nKenjimaru, the author of this document, I am Japanese and am not familiar to English.\n\nSo, if you read this document, and find anything to fix, feel free to contact me,\nand I will appreciate.\n\n',
    'author': 'kenjimaru',
    'author_email': 'kendimaru2@gmail.com',
    'maintainer': 'kenjimaru',
    'maintainer_email': 'kendimaru2@gmail.com',
    'url': 'https://github.com/kendimaru/textfile',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
