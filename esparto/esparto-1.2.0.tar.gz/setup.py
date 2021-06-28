# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['esparto']

package_data = \
{'': ['*'], 'esparto': ['resources/css/*', 'resources/jinja/*']}

install_requires = \
['Pillow>=7.0.0,<9', 'jinja2>=2.10.1,<4.0.0', 'markdown>=3.1,<4.0']

extras_require = \
{':python_version < "3.7"': ['dataclasses'],
 'extras': ['beautifulsoup4>=4.7', 'weasyprint>=51']}

setup_kwargs = {
    'name': 'esparto',
    'version': '1.2.0',
    'description': 'Simple HTML and PDF document generator for Python.',
    'long_description': 'esparto\n=======\n\n[![image](https://img.shields.io/pypi/v/esparto.svg)](https://pypi.python.org/pypi/esparto)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/esparto.svg)](https://pypi.python.org/pypi/esparto/)\n[![Build Status](https://travis-ci.com/domvwt/esparto.svg?branch=main)](https://travis-ci.com/domvwt/esparto)\n[![codecov](https://codecov.io/gh/domvwt/esparto/branch/main/graph/badge.svg?token=35J8NZCUYC)](https://codecov.io/gh/domvwt/esparto)\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=domvwt_esparto&metric=alert_status)](https://sonarcloud.io/dashboard?id=domvwt_esparto)\n\n\n## Introduction\n`esparto` is a simple HTML and PDF document generator for Python.\nThe library takes a fully Pythonic approach to defining documents,\nallowing iterative building and modification of the page and its contents.\n\n\n### Example Use Cases\n* Automated MI reporting\n* Collating and sharing data visualisations\n* ML model performance and evaluation documents\n* Designing simple web pages\n\n\n## Main Features\n* Lightweight API\n* Jupyter Notebook support\n* Output self-contained HTML and PDF files\n* Responsive layout from [Bootstrap](https://getbootstrap.com/)\n* No CSS or HTML required\n* Implicit conversion for:\n    * Markdown\n    * Images\n    * Pandas DataFrames\n    * Matplotlib\n    * Bokeh\n    * Plotly\n\n\n## Installation\n`esparto` is available from PyPI:\n```bash\npip install esparto\n```\n\nIf PDF output is required, `weasyprint` must also be installed:\n```bash\npip install weasyprint\n```\n\n\n## Dependencies\n*   [python](https://python.org/) >= 3.6\n*   [jinja2](https://palletsprojects.com/p/jinja/)\n*   [markdown](https://python-markdown.github.io/)\n*   [Pillow](https://python-pillow.org/)\n*   [weasyprint](https://weasyprint.org/) _(optional - for PDF output)_\n\n\n## License\n[MIT](https://opensource.org/licenses/MIT)\n\n\n## Documentation\nFull documentation and examples are available at [domvwt.github.io/esparto/](https://domvwt.github.io/esparto/).\n\n\n## Basic Usage\n```python\nimport esparto as es\n\n# Instantiating a Page\npage = es.Page(title="Research")\n\n# Page layout hierarchy:\n# Page -> Section -> Row -> Column -> Content\n\n# Add or update content\n# Keys are used as titles\npage["Introduction"]["Part One"]["Item A"] = "./text/content.md"\npage["Introduction"]["Part One"]["Item B"] = "./pictures/image1.jpg"\n\n# Add content without a title\npage["Introduction"]["Part One"][""] = "Hello, Wolrd!"\n\n# Replace child at index - useful if no title given\npage["Introduction"]["Part One"][-1] = "Hello, World!"\n\n# Set content and return input object\n# Useful in Jupyter Notebook as it will be displayed in cell output\npage["Methodology"]["Part One"]["Item A"] << "dolor sit amet"\n# >>> "dolor sit amet"\n\n# Set content and return new layout\npage["Methodology"]["Part Two"]["Item B"] >> "foobar"\n# >>> {\'Item B\': [\'Markdown\']}\n\n# Show document structure\npage.tree()\n# >>> {\'Research\': [{\'Introduction\': [{\'Part One\': [{\'Item A\': [\'Markdown\']},\n#                                                   {\'Item B\': [\'Image\']}]}]},\n#                   {\'Methodology\': [{\'Part One\': [{\'Item A\': [\'Markdown\']}]},\n#                                    {\'Part Two\': [{\'Item A\': [\'Markdown\']}]}]}]}\n\n# Remove content\ndel page["Methodology"]["Part One"]["Item A"]\ndel page.methodology.part_two.item_b\n\n# Access existing content as an attribute\npage.introduction.part_one.item_a = "./pictures/image2.jpg"\npage.introduction.part_one.tree()\n# >>> {\'Part One\': [{\'Item A\': [\'Image\']},\n#                   {\'Item B\': [\'Image\']},\n#                   {\'Column 2\': [\'Markdown\']}]}\n\n# Save the document\npage.save_html("my-page.html")\npage.save_pdf("my-page.pdf")\n```\n\n\n## Example Output\nIris Report - [HTML](https://domvwt.github.io/esparto/examples/iris-report.html) |\n[PDF](https://domvwt.github.io/esparto/examples/iris-report.pdf)\n\nBokeh and Plotly - [HTML](https://domvwt.github.io/esparto/examples/interactive-plots.html) |\n[PDF](https://domvwt.github.io/esparto/examples/interactive-plots.pdf)\n\n<br>\n\n<img width=600  src="https://github.com/domvwt/esparto/blob/fdc0e787c0bc013d16667773e82e21c647b71d91/docs/images/iris-report-compressed.png?raw=true"\nalt="example page" style="border-radius:0.5%;">\n',
    'author': 'Dominic Thorn',
    'author_email': 'dominic.thorn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://domvwt.github.io/esparto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
