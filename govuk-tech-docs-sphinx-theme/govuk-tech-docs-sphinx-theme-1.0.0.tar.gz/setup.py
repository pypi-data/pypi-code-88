# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['govuk_tech_docs_sphinx_theme', 'govuk_tech_docs_sphinx_theme.components']

package_data = \
{'': ['*'],
 'govuk_tech_docs_sphinx_theme': ['static/*',
                                  'static/assets/govuk/assets/fonts/*',
                                  'static/assets/govuk/assets/images/*',
                                  'static/images/*',
                                  'static/javascripts/*',
                                  'static/javascripts/_govuk/*',
                                  'static/javascripts/_modules/*',
                                  'static/javascripts/_vendor/*',
                                  'static/stylesheets/*']}

install_requires = \
['Sphinx>=4.0.2,<5.0.0']

setup_kwargs = {
    'name': 'govuk-tech-docs-sphinx-theme',
    'version': '1.0.0',
    'description': 'A Sphinx theme to replicate the GOV.UK Tech Docs Template.',
    'long_description': '# GOV.UK Tech Docs Sphinx Theme\n\nA Sphinx theme to replicate the GOV.UK Tech Docs Template.\n\n```{warning}\n\nWhere this documentation refers to the root folder we mean where this README.md is located.\n\n```\n\n## Getting started\n\nThe source code for this Sphinx theme is available at\n[`https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme`][repository]. You\ncan use this for your own Sphinx documentation by following the steps below.\n\n### Install the package\n\nThe latest released version can be installed from the [Python Package Index\n(PyPI)][pypi]:\n\n```shell\npip install govuk-tech-docs-sphinx-theme\n```\n\n### Amend your Sphinx `conf.py` configuration file\n\nTo use this Sphinx theme, modify your Sphinx `conf.py` configuration file as follows:\n\n1. Add the theme in the list of `extensions`:\n   ```python\n   extensions = ["govuk_tech_docs_sphinx_theme"]\n   ```\n2. Make sure the `author`, and `project` variables reflect your organisation name, and\n   project\n3. Set `html_theme = "govuk_tech_docs_sphinx_theme"`\n4. Set the `html_context` dictionary as follows:\n   ```python\n   html_context = {\n       "github_url": None,                  # if using GitHub, set to the URL of your repository as a string\n       "gitlab_url": None,                  # if using GitLab, set to the URL of your repository as a string\n       "conf_py_path": "docs/",             # assuming your Sphinx folder is called `docs`\n       "version": "main",                   # assuming `main` is your repository\'s default branch\n       "accessibility": "accessibility.md"  # assuming your accessibility statement is at `docs/accessibility.md`\n   }\n   ```\n5. Set the `html_theme_options` dictionary as follows:\n   ```python\n   html_theme_options = {\n       "organisation": "",  # replace with your organisation\'s abbreviation (ideally) or name - long text may not look nice\n       "phase": ""          # replace with an Agile project phase - see https://www.gov.uk/service-manual/agile-delivery\n   }\n   ```\n\nNote, not all Sphinx configuration settings are currently supported by this theme —\n[feel free to contribute to support other settings](#contributing)!\n\n### Add an accessibility statement\n\n````{note} Accessibility issues with Sphinx autodoc extension\n\nWith the Sphinx autodoc extension, you may find headers do not fit the content that\nfollows. This [fails the WCAG 2.1 success criterion 2.4.6 Headings and\nLabels][wcag-2.1-2.4.6].\n\nTo resolve this, copy the entire `docs/_template` folder from this repository into\nyour Sphinx folder, and ensure your `conf.py` file contains:\n\n```python\ntemplates_path = ["_templates"]\n```\n\n````\n\nAll public sector bodies have to meet the [2018 accessibility\nregulations][govuk-accessibility] unless exempt.\n\nTo add an accessibility statement, create a blank Markdown file in the root of your\nSphinx folder called `accessibility.md`. This folder is the same location as your\nSphinx `conf.py` configuration file. Add the following header to your new Markdown file:\n\n```markdown\n---\norphan: true\n---\n# Accessibility statement\n```\n\nfollowed by your accesibility statement. [Guidance on how to write an accessibility\nstatement can be found on GOV.UK][govuk-example-accessibility].\n\nNext, in your Sphinx `conf.py` file, check that the `html_context` variable has this\nfile referenced, i.e.:\n\n```python\nhtml_context = {\n    ...,\n    "accessibility": "accessibility.md",\n    ...\n}\n```\n\n### Apply the theme\'s components\n\nThis theme should be compatible with most ReStructuredText syntax, and also includes\n[components from the GOV.UK Design System][govuk-design]. [See the example\ncomponents page for further details][docs-example-components-rest].\n\n[If you are using MyST to build Sphinx documentation using Markdown][myst], see\nthe [equivalent Markdown components page][docs-example-components-md].\n\n## Troubleshooting\n\nIf you have difficulties with this theme, [please raise an issue][repository-issues] or\n[contact us to report a problem][email].\n\n## Licence\n\nUnless stated otherwise, the codebase is released under the MIT License. This covers\nboth the codebase and any sample code in the documentation. [Additional third-party\ncomponent licences are stated in the `LICENSE`][license] file. The documentation is\n© Crown copyright and available under the terms of the Open Government 3.0 licence.\n\n## Contributing\n\n[If you want to help us build, and improve `govuk-tech-docs-sphinx-theme`, view our\ncontributing guidelines][contributing].\n\n## Acknowledgements\n\n[This project structure is based on the `govcookiecutter` template\nproject][govcookiecutter].\n\n[contributing]: ./docs/contributor_guide/CONTRIBUTING.md\n[docs-example-components-md]: ./docs/example_components/markdown.md\n[docs-example-components-rest]: ./docs/example_components/restructuredtext.rst\n[email]: mailto:gds-data-science@digital.cabinet-office.gov.uk\n[govcookiecutter]: https://github.com/ukgovdatascience/govcookiecutter\n[govuk-accessibility]: https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps\n[govuk-design]: https://design-system.service.gov.uk/\n[govuk-example-accessibility]: https://www.gov.uk/government/publications/sample-accessibility-statement/sample-accessibility-statement-for-a-fictional-public-sector-website\n[license]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme/blob/main/LICENSE\n[myst]: https://myst-parser.readthedocs.io/en/latest/\n[pypi]: https://pypi.org/project/govuk-tech-docs-sphinx-theme/\n[repository]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme\n[repository-issues]: https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme/issues/new\n[wcag-2.1-2.4.6]: https://www.w3.org/WAI/WCAG21/Understanding/headings-and-labels.html\n',
    'author': 'ukgovdatascience',
    'author_email': 'gds-data-science@digital.cabinet-office.gov.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ukgovdatascience/govuk-tech-docs-sphinx-theme',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
