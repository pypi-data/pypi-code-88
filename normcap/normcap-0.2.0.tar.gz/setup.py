# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['normcap', 'normcap.magics', 'normcap.resources']

package_data = \
{'': ['*'], 'normcap.resources': ['tessdata/.keep']}

install_requires = \
['PySide2>=5.15.2,<6.0.0',
 'importlib-metadata>=4.5.0,<5.0.0',
 'importlib-resources>=5.1.4,<6.0.0',
 'jeepney>=0.6.0,<0.7.0']

extras_require = \
{':sys_platform == "darwin"': ['tesserocr>=2.4.0,<3.0.0'],
 ':sys_platform == "linux"': ['tesserocr>=2.4.0,<3.0.0'],
 ':sys_platform == "win32"': ['tesserocr==2.4.0']}

entry_points = \
{'console_scripts': ['normcap = normcap.app:main']}

setup_kwargs = {
    'name': 'normcap',
    'version': '0.2.0',
    'description': 'OCR-powered screen-capture tool to capture information instead of images.',
    'long_description': '<!-- markdownlint-disable MD013 MD026 MD033 -->\n\n# NormCap\n\n**_OCR powered screen-capture tool to capture information instead of images._**\n\n[![Build passing](https://github.com/dynobo/normcap/workflows/Build/badge.svg)](https://github.com/dynobo/normcap/releases)\n[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)\n[![Code style: black](https://img.shields.io/badge/Code%20style-black-%23000000)](https://github.com/psf/black)\n[![Coverage Status](https://coveralls.io/repos/github/dynobo/normcap/badge.svg)](https://coveralls.io/github/dynobo/normcap)\n\n**Links:** [Repo](https://github.com/dynobo/normcap) |\n[PyPi](https://pypi.org/project/normcap) |\n[Releases](https://github.com/dynobo/normcap/releases) |\n[Changelog](https://github.com/dynobo/normcap/blob/main/CHANGELOG.md) |\n[FAQs](https://github.com/dynobo/normcap/blob/main/FAQ.md)\n\n**Content:** [Quickstart](#Quickstart) | [Python package](#Python-package) |\n[Usage](#Usage) | [Contribute](#Contribute) | [Credits](#Credits)\n\n[![Screencast](https://user-images.githubusercontent.com/11071876/123133596-3107d080-d450-11eb-8451-6dcebb7876ad.gif)](https://raw.githubusercontent.com/dynobo/normcap/main/assets/normcap.gif)\n\n## Quickstart\n\n**❱❱\n[Download & run a pre-build package for Linux, MacOS or Windows](https://github.com/dynobo/normcap/releases)\n❰❰**\n\nHints:\n\n- If you experience issues or have questions please look at the\n  [FAQs](https://github.com/dynobo/normcap/blob/main/FAQ.md) or\n  [open an issue](https://github.com/dynobo/normcap/issues).\n- On **Linux**, make the AppImage executable before running it:\n  ```\n  chmod +x NormCap-Linux.AppImage\n  ./NormCap-Linux.AppImage\n  ```\n- On **MacOS**, you have to allow the unsigned application on first start: "System\n  Preferences" → "Security & Privacy" → Tab "General" → "Open anyway". \\\n  Depending on\n  your OS, you might also need to allow NormCap to take screenshots.\n\n## Python package\n\nAs an _alternative_ to a pre-build package you can install the\n[NormCap Python package](https://pypi.org/project/normcap/):\n\n### On Linux\n\n```sh\n# Install dependencies (Ubuntu/Debian)\nsudo apt install tesseract-ocr tesseract-ocr-eng \\\n                 libtesseract-dev libleptonica-dev\n\n## Install dependencies (Arch)\nsudo pacman -S tesseract tesseract-data-eng leptonica\n\n## Install dependencies (Fedora)\nsudo dnf install tesseract tesseract-devel leptonica-devel\n\n# Install normcap\npip install normcap\n\n# Run\n./normcap\n```\n\n### On MacOS\n\n```sh\n# Install dependencies\nbrew install tesseract tesseract-lang\n\n# Install normcap\npip install normcap\n\n# Run\n./normcap\n```\n\n### On Windows\n\n1\\. Install "Tesseract **4.1**", e.g. by using the\n[installer provided by UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).\n\n2\\. Set the environment variable `TESSDATA_PREFIX` to Tesseract\'s data folder, e.g.:\n\n```cmd\nsetx TESSDATA_PREFIX "C:\\Program Files\\Tesseract-OCR\\tessdata"\n```\n\n3\\. Install [tesserocr](https://pypi.org/project/tesserocr/) using the\n[Windows specific wheel](https://github.com/simonflueckiger/tesserocr-windows_build) and\nNormCap afterwards:\n\n```bash\n# Install tesserocr package\npip install https://github.com/simonflueckiger/tesserocr-windows_build/releases/download/tesserocr-v2.4.0-tesseract-4.0.0/tesserocr-2.4.0-cp37-cp37m-win_amd64.whl\n\n# Install normcap\npip install normcap\n\n# Run\nnormcap\n```\n\n## Usage\n\n### General\n\n- Press `<esc>` key to abort a capture and quit the application.\n\n- Press `<space>` key while selecting a region with the mouse (left mouse button has to\n  be hold down) to switch between the two capture modes:\n\n  - **★ (parse):** Try to auto-detect the type of text using [magics](#Magics) and\n    format the text accordingly, then copy\n  - **☰ (raw):** Copy detected text line by line, without further modification\n\n### Command line options\n\nNormCap has no settings, just a set of command line arguments:\n\n```plain\n(normcap)dynobo@cioran:~$ normcap --help\nusage: normcap [-h] [-l LANGUAGE] [-c COLOR] [-n] [-t] [-v] [-V]\n\nOCR-powered screen-capture tool to capture information instead of images.\n\noptional arguments:\n  -h, --help                  show this help message and exit\n  -l LANGUAGE, --language LANGUAGE\n                              set language(s) for text recognition, e.g.\n                              eng+deu (default: eng)\n  -c COLOR, --color COLOR     set primary color for UI (default: #FF2E88)\n  -n, --no-notifications      disable notifications shown after ocr detection\n                              (default: False)\n  -t, --tray                  keep running in system tray - experimental\n                              (default: False)\n  -v, --verbose               print debug information to console (default:\n                              False)\n  -V, --very-verbose          print more debug information to console\n                              (default: False)\n```\n\n### Magics\n\n"Magics" are like add-ons providing automated functionality to intelligently detect and\nformat the captured input.\n\nFirst, every "magic" calculates a "**score**" to determine the likelihood of being\nresponsible for this type of text. Second, the "magic" which achieved the highest\n"score" takes the necessary actions to **"transform"** the input text according to its\ntype.\n\nCurrently implemented Magics:\n\n| Magic           | Score                                                | Transform                                                                            |\n| --------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------ |\n| **Single\xa0line** | Only single line is detected                         | Trim unnecessary whitespace                                                          |\n| **Multi\xa0line**  | Multi lines, but single Paragraph                    | Separated by line breaks and trim each lined                                         |\n| **Paragraph**   | Multiple blocks of lines or multiple paragraphs      | Join every paragraph into a single line, separate different paragraphs by empty line |\n| **E-Mail**      | Number of chars in email addresses vs. overall chars | Transform to a comma-separated list of email addresses                               |\n| **URL**         | Number of chars in URLs vs. overall chars            | Transform to line-break separated URLs                                               |\n\n## Why "NormCap"?\n\nSee [XKCD](https://xkcd.com):\n\n[![Comic](https://imgs.xkcd.com/comics/norm_normal_file_format.png)](https://xkcd.com/2116/)\n\n## Contribute\n\n### Setup Environment\n\nPrerequisites are **Python >=3.7.1**, **Poetry**, **Tesseract** (incl. **language\ndata**).\n\n```sh\n# Clone repository\ngit clone https://github.com/dynobo/normcap.git\n\n# Change into project directory\ncd normcap\n\n# Create virtual env and install dependencies\npoetry install\n\n# Register pre-commit hook\npoetry run pre-commit install\n\n# Run NormCap in virtual env\npoetry run python -m normcap\n```\n\n## Credits\n\nThis project uses the following non-standard libraries:\n\n- [pyside2](https://pypi.org/project/PySide2/) _- bindings for Qt UI Framework_\n- [tesserocr](https://pypi.org/project/tesserocr/) _- wrapper for tesseract\'s API_\n- [jeepney](https://pypi.org/project/jeepney/) _- DBUS client_\n\nPackaging is done with:\n\n- [briefcase](https://pypi.org/project/briefcase/) _- converting Python projects into_\n  _standalone apps_\n\nAnd it depends on external software\n\n- [tesseract](https://github.com/tesseract-ocr/tesseract) - _OCR engine_\n\nThanks to the maintainers of those nice libraries!\n\n## Certification\n\n![WOMM](https://raw.githubusercontent.com/dynobo/lmdiag/master/badge.png)\n',
    'author': 'dynobo',
    'author_email': 'dynobo@mailbox.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dynobo/normcap',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
