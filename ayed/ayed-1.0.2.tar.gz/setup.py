# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ayed']

package_data = \
{'': ['*']}

install_requires = \
['openpyxl>=3.0.7,<4.0.0',
 'pandas>=1.2.4,<2.0.0',
 'rich>=10.4.0,<11.0.0',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['ayed = ayed.tool:app']}

setup_kwargs = {
    'name': 'ayed',
    'version': '1.0.2',
    'description': 'AyED Tools',
    'long_description': '# `AyED Tools`\n\n**Usage**:\n\n```console\n$ ayed [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `coll`: Crea las funciones newT, TToString, etc. Para un struct T.\n* `files`: Crea archivos .dat con los datos de un excel.\n\n## `ayed coll`\n\nCrea las funciones newT, TToString, TFromString, TToDebug para un struct T.\n\nPor default, abre un editor - $VISUAL o NOTEPAD en Win, $EDITOR o vi/vim/nvim/nano en Linux - en el que podrán escribir sus structs\n\nSi ya tienen un archivo y no quieren que se abra el editor, pueden usar\n-p o --path [PATH], siendo [PATH] el nombre del archivo.\n\n**Usage**:\n\n```console\n$ ayed coll [OPTIONS]\n```\n\n**Options**:\n\n* `-p, --path FILE`: La dirección del archivo .cpp[,.hpp,.c,.h] que contiene a los structs\n* `--help`: Show this message and exit.\n\n## `ayed files`\n\nPor default, abre el excel `AlgoritmosFiles.xlsx` en la carpeta en la que\nestén y lee todas sus solapas.\n\nSi el excel está en otro lugar, pueden especificar la dirección del archivo.xlsx\ndespués del nombre del programa,\nej: \n```console\n$ ayed files home/bocanada/Documents/AlgoritmosFiles.xlsx.\n```\nCon -s o --sheet [SHEET] pueden especificar una solapa, siendo [SHEET] la solapa.\n\nSi utilizan --no-read, el programa no leerá los archivos para mostrarlos.\n\n**Usage**:\n\n```console\n$ ayed files [OPTIONS] [PATH]\n```\n\n**Arguments**:\n\n* `[PATH]`: La dirección del .xlsx  [default: AlgoritmosFiles.xlsx]\n\n**Options**:\n\n* `-s, --sheet TEXT`: El nombre de la solapa/sheet\n* `--read / --no-read`: Lee las estructuras guardadas en el .dat  [default: True]\n* `--help`: Show this message and exit.\n',
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
