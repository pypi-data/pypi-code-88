# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pywhat']

package_data = \
{'': ['*'], 'pywhat': ['Data/*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'name_that_hash>=1.7.0,<2.0.0', 'rich>=9.9,<11.0']

entry_points = \
{'console_scripts': ['pywhat = pywhat.what:main', 'what = pywhat.what:main']}

setup_kwargs = {
    'name': 'pywhat',
    'version': '3.1.0',
    'description': 'What is that thing?',
    'long_description': '<p align=\'center\'>\n<img src=\'images_for_README/logo.png\'>\n<p align="center">➡️ <a href="http://discord.skerritt.blog">Discord</a> ⬅️<br>\n<i>The easiest way to identify anything</i><br>\n<code>pip3 install pywhat && pywhat --help</code>\n</p>\n\n<p align="center">\n  <a href="http://discord.skerritt.blog"><img alt="Discord" src="https://img.shields.io/discord/754001738184392704"></a> <a href="https://pypi.org/project/pywhat/"><img alt="PyPI - Downloads" src="https://pepy.tech/badge/pywhat/month"></a>  <a href="https://twitter.com/bee_sec_san"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/bee_sec_san?style=social"></a> <a href="https://pypi.org/project/pywhat/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pywhat"></a> <a href="https://pypi.org/project/pywhat/"><img alt="PyPI" src="https://img.shields.io/pypi/v/pywhat"></a>\n</p>\n<hr>\n\n# 🤔 `What` is this?\n\n![](images_for_README/main_demo.gif)\n\nImagine this: You come across some mysterious text 🧙\u200d♂️ `5f4dcc3b5aa765d61d8327deb882cf99` and you wonder what it is. What do you do?\n\nWell, with `what` all you have to do is ask `what "5f4dcc3b5aa765d61d8327deb882cf99"` and `what` will tell you!\n\n`what`\'s job is to **identify _what_ something is.** Whether it be a file or text! Or even the hex of a file! What about text _within_ files? We have that too! `what` is recursive, it will identify **everything** in text and more! \n\n# ⚙ Use Cases\n\n## 🦠 Wannacry\n\n![](images_for_README/Screenshot%202021-05-09%20162158.png)\n\nYou come across a new piece of malware called WantToCry. You think back to Wannacry and remember it was stopped because a researcher found a kill-switch in the code.\n\nWhen a domain, hardcoded into Wannacry, was registered the virus would stop.\n\nYou use `What` to identify all the domains in the malware, and use a domain registrar API to register all the domains. If Wannacry happens again, you can stop it in minutes - not weeks.\n\n## 🦈 Faster Analysis of Pcap files\n\n![](images_for_README/pcap_demo.gif)\n\nSay you have a `.pcap` file from a network attack. `What` can identify this and quickly find you:\n* All hashes\n* Credit card numbers\n* Cryptocurrency addresses\n* Social Security Numbers\n* and much more.\n\nWith `what`, you can identify the important things in the pcap in seconds, not minutes.\n\n## 🌌 Anything\n\nAnytime you have a file and you want to find structured data in it that\'s useful, `What` is for you.\n\nOr if you come across some piece of text and you don\'t know what it is, `What` will tell you.\n\n**File Opening** You can pass in a file path by `what \'this/is/a/file/path\'`. `What` is smart enough to figure out it\'s a file!\n\nWhat about a whole **directory**? `What` can handle that too! It will **recursively** search for files and output everything you need!\n\n**Filtration** You can filter output by using `what --rarity 0.2:0.8 --include_tags tag1,tag2 TEXT`. Use `what --help` to get more information.\n\n**Sorting** You can sort the output by using `what -k rarity --reverse TEXT`. Use `what --help` to get more information.\n\n# 🍕 API\n\nPyWhat has an API! Click here [https://github.com/bee-san/pyWhat/wiki/API](https://github.com/bee-san/pyWhat/wiki/API) to read about it.\n\n# 👾 Contributing\n\n`what` not only thrives on contributors, but can\'t exist without them! If you want to add a new regex to check for things, you can read our documentation [here](https://github.com/bee-san/what/wiki/Adding-your-own-Regex)\n\nWe ask contributors to join the Discord for quicker discussions, but it\'s not needed:\n<img alt="Discord" src="https://img.shields.io/discord/754001738184392704">\n',
    'author': 'Bee',
    'author_email': 'github@skerritt.blog',
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
