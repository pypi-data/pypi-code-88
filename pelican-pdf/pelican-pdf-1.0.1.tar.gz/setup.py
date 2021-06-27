# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican', 'pelican.plugins.pdf']

package_data = \
{'': ['*'], 'pelican.plugins.pdf': ['test_data/*']}

install_requires = \
['pelican>=4.5', 'rst2pdf>=0.98', 'xhtml2pdf>=0.2.5']

extras_require = \
{'markdown': ['markdown>=3.2.2']}

setup_kwargs = {
    'name': 'pelican-pdf',
    'version': '1.0.1',
    'description': 'PDF Generator is a Pelican plugin that exports articles and pages as PDF files during site generation',
    'long_description': 'PDF Generator: A Plugin for Pelican\n===================================\n\n[![Build Status](https://img.shields.io/github/workflow/status/pelican-plugins/pdf/build)](https://github.com/pelican-plugins/pdf/actions)\n[![PyPI Version](https://img.shields.io/pypi/v/pelican-pdf)](https://pypi.org/project/pelican-pdf/)\n![License](https://img.shields.io/pypi/l/pelican-pdf?color=blue)\n\nThe PDF Generator plugin automatically exports articles and pages as PDF files as part of the site generation process.\nPDFs are saved to: `output/pdf/`\n\nInstallation\n------------\n\nThis plugin can be installed via:\n\n    python -m pip install pelican-pdf\n\nUsage\n-----\n\nTo customize the PDF output, you can use the following settings in your Pelican configuration file:\n\n\tPDF_STYLE = ""\n\tPDF_STYLE_PATH = ""\n\n`PDF_STYLE_PATH` defines a new path where *rst2pdf* will look for style sheets, while `PDF_STYLE` specifies the style you want to use.\nFor a description of the available styles, please read the [rst2pdf documentation](http://rst2pdf.ralsina.me/handbook.html#styles).\n\nContributors\n------------\n\nContributors include: Dominik Wombacher, Justin Mayer, Kyle Mahan, Renato Cunha, dpetzel, and Lucas Cimon\n\nContributing\n------------\n\nContributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].\n\nTo start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.\n\n[existing issues]: https://github.com/pelican-plugins/pdf/issues\n[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html\n\nLicense\n-------\n\nThis project is licensed under the AGPL 3.0 license.\n',
    'author': 'Pelican Dev Team',
    'author_email': 'authors@getpelican.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pelican-plugins/pdf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
