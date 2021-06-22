# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['latex2mathml']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['l2m = latex2mathml.converter:main',
                     'latex2mathml = latex2mathml.converter:main']}

setup_kwargs = {
    'name': 'latex2mathml',
    'version': '3.56.0',
    'description': 'Pure Python library for LaTeX to MathML conversion',
    'long_description': '# latex2mathml\n\nPure Python library for LaTeX to MathML conversion\n\n<table>\n    <tr>\n        <td>License</td>\n        <td><img src=\'https://img.shields.io/pypi/l/latex2mathml.svg\' alt="License"></td>\n        <td>Version</td>\n        <td><img src=\'https://img.shields.io/pypi/v/latex2mathml.svg\' alt="Version"></td>\n    </tr>\n    <tr>\n        <td>Travis CI</td>\n        <td><img src=\'https://www.travis-ci.com/roniemartinez/latex2mathml.svg?branch=master\' alt="Travis CI"></td>\n        <td>Coverage</td>\n        <td><img src=\'https://codecov.io/gh/roniemartinez/latex2mathml/branch/master/graph/badge.svg\' alt="CodeCov"></td>\n    </tr>\n    <tr>\n        <td>Supported versions</td>\n        <td><img src=\'https://img.shields.io/pypi/pyversions/latex2mathml.svg\' alt="Python Versions"></td>\n        <td>Wheel</td>\n        <td><img src=\'https://img.shields.io/pypi/wheel/latex2mathml.svg\' alt="Wheel"></td>\n    </tr>\n    <tr>\n        <td>Status</td>\n        <td><img src=\'https://img.shields.io/pypi/status/latex2mathml.svg\' alt="Status"></td>\n        <td>Downloads</td>\n        <td><img src=\'https://img.shields.io/pypi/dm/latex2mathml.svg\' alt="Downloads"></td>\n    </tr>\n</table>\n\n## Support\nIf you like `latex2mathml` or if it is useful to you, show your support by buying me a coffee.\n\n<a href="https://www.buymeacoffee.com/roniemartinez" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>\n\n## Installation\n\n```bash\npip install latex2mathml\n```\n\n## Usage\n\n### Python\n\n```python\nimport latex2mathml.converter\n\nlatex_input = "<your_latex_string>"\nmathml_output = latex2mathml.converter.convert(latex_input)\n```\n\n### Command-line\n\n```shell\n% latex2mathml -h\nusage: l2m [-h] [-V] [-b] [-t TEXT | -f FILE]\n\nPure Python library for LaTeX to MathML conversion\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -V, --version         Show version\n  -b, --block           Display block\n\nrequired arguments:\n  -t TEXT, --text TEXT  Text\n  -f FILE, --file FILE  File\n```\n\n## References\n### LaTeX\n\n- https://en.wikibooks.org/wiki/LaTeX/Mathematics\n- http://artofproblemsolving.com/wiki/index.php?title=Main_Page\n- http://milde.users.sourceforge.net/LUCR/Math/\n- https://math-linux.com/latex-26/faq/latex-faq/article/latex-derivatives-limits-sums-products-and-integrals\n- https://www.tutorialspoint.com/tex_commands\n- https://www.giss.nasa.gov/tools/latex/ltx-86.html\n- https://ftp.gwdg.de/pub/ctan/info/l2tabu/english/l2tabuen.pdf\n\n### MathML\n\n- http://www.xmlmind.com/tutorials/MathML/\n\n\n## Author\n- [Ronie Martinez](mailto:ronmarti18@gmail.com)\n',
    'author': 'Ronie Martinez',
    'author_email': 'ronmarti18@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/roniemartinez/latex2mathml',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4',
}


setup(**setup_kwargs)
