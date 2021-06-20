# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ayed']

package_data = \
{'': ['*']}

install_requires = \
['openpyxl>=3.0.7,<4.0.0', 'pandas>=1.2.4,<2.0.0', 'rich>=10.4.0,<11.0.0']

entry_points = \
{'console_scripts': ['ayed = ayed.tool:main']}

setup_kwargs = {
    'name': 'ayed',
    'version': '0.5.1',
    'description': 'AyED Tools',
    'long_description': '## AyED Tools\n### Instalación\n```zsh\nbocanada in ~/Dev/ayed/ayed on main ● λ $ pip install ayed\n```\nRequiere `python3.8^`*\n### Uso fn generator\n```zsh\n$ bocanada in ~/Dev/ayed/ayed on main ● λ $ ayed\n1. Coll fn generator\n2. Files generator\nOption [1/2]: $ 1\nOpen editor? [y/n] (y): $ n\nEnter path to a .cpp[,.hpp,.c,.h]: >> ../tests/structs/structs.cpp\n[14:25:10]                     Wrote /home/bocanada/Dev/ayed/output_files/20-06-21-1425.hpp            tool.py:68\n                                Wrote TtoDebug, TtoString, TfromString and newT for Equipo\n                                                      Done! Bye! 👋 \n```\n### Uso files generator\n```zsh\n$ bocanada in ~/Dev/ayed on main ● λ ayed\n1. Coll fn generator\n2. Files generator\nOption [1/2]: $ 2\nEnter path to a .xlsx file 👀 (AlgoritmosFiles.xlsx): $ AlgoritmosFiles.xlsx\nPor default, esto abrirá el excel y escribirá archivos en output_files/. Continuar? [y/n] (y): \n[14:29:48]                                     Found 3 structs 🙉                                 excel.py:53\n                                               Found 2 structs 🙉                                 excel.py:53\n                                             VUELOS.dat - 64 bytes\n                                          ┏━━━━━━━┳━━━━━┳━━━━━━━┳━━━━━━━┓\n                                          ┃ idVue ┃ cap ┃ idOri ┃ idDes ┃ \n                                          ┡━━━━━━━╇━━━━━╇━━━━━━━╇━━━━━━━┩\n                                          │   1   │ 10  │   1   │   4   │            \n                                          ├───────┼─────┼───────┼───────┤     \n                                          │   2   │ 15  │   2   │   1   │ \n                                          ├───────┼─────┼───────┼───────┤ \n                                          │   3   │ 12  │   4   │   3   │ \n                                          ├───────┼─────┼───────┼───────┤\n                                          │   4   │  5  │   3   │   2   │\n                                          └───────┴─────┴───────┴───────┘\n                                                   Done! Bye! 👋\n```\n',
    'author': 'Bocanada',
    'author_email': '24578415+Bocanada@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Bocanada/AyED-Tool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
