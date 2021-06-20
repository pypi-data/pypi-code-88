# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['skjold', 'skjold.sources']

package_data = \
{'': ['*']}

install_requires = \
['click>=7,<9',
 'poetry-semver>=0.1.0,<0.2.0',
 'pyyaml>=5.3,<6.0',
 'toml>=0.10.0']

entry_points = \
{'console_scripts': ['skjold = skjold.cli:cli']}

setup_kwargs = {
    'name': 'skjold',
    'version': '0.3.0',
    'description': 'Security audit Python project dependencies against security advisory databases.',
    'long_description': '![](https://img.shields.io/pypi/v/skjold?color=black&label=PyPI&style=flat-square)\n![](https://img.shields.io/github/workflow/status/twu/skjold/Python%20Package/master?color=black&label=Tests&style=flat-square)\n![](https://img.shields.io/pypi/status/skjold?color=black&style=flat-square)\n![](https://img.shields.io/pypi/pyversions/skjold?color=black&logo=python&logoColor=white&style=flat-square)\n![](https://img.shields.io/pypi/l/skjold?color=black&label=License&style=flat-square)\n![](https://img.shields.io/pypi/dm/skjold?color=black&label=Downloads&style=flat-square)\n[![](https://api.codeclimate.com/v1/badges/9f756df1ff145e6004a7/maintainability)](https://codeclimate.com/github/twu/skjold/maintainability)\n[![Test Coverage](https://api.codeclimate.com/v1/badges/9f756df1ff145e6004a7/test_coverage)](https://codeclimate.com/github/twu/skjold/test_coverage)\n\n```\n        .         .    .      Skjold /skjɔl/\n    ,-. | , . ,-. |  ,-|\n    `-. |<  | | | |  | |      Security audit python project dependencies\n    `-\' \' ` | `-\' `\' `-´      against several security advisory databases.\n           `\'\n```\n\n## Introduction\nIt currently supports fetching advisories from the following sources:\n\n| Source | Name | Notes |\n| ------:|:----:|:------|\n| [GitHub Advisory Database](https://github.com/advisories) | `github` | |\n| [PyUP.io safety-db](https://github.com/pyupio/safety-db) | `pyup` | |\n| [GitLab gemnasium-db](https://gitlab.com/gitlab-org/security-products/gemnasium-db) | `gemnasium` | |\n| [PYPA Advisory Database](https://github.com/pypa/advisory-db) | `pypa` | **Experimental!** Only supports `ECOSYSTEM` and `SEMVER`! |\n| [OSV.dev Database](https://osv.dev) | `osv` | **Experimental!** Only supports `ECOSYSTEM` and `SEMVER`!<br/> Sends package information to [OSV.dev](https://osv.dev) API. |\n\n\nNo source is enabled by default! Individual sources can be enabled by setting `sources` list (see [Configuration](#configuration)). There is (currently) no de-duplication meaning that using all of them could result in _a lot_ of duplicates.\n\n## Motivation\nSkjold was initially created for myself to replace `safety`. ~Which appears to no longer receive monthly updates (see [pyupio/safety-db #2282](https://github.com/pyupio/safety-db/issues/2282))~. I wanted something I can run locally and use for my local or private projects/scripts.\n\nI currently also use it during CI builds and before deploying/publishing containers or packages.\n\n## Installation\n`skjold` can be installed from either [PyPI](https://pypi.org/project/skjold/) or directly from [Github](https://github.com/twu/skjold) using `pip`:\n\n```sh\npip install skjold                                        # Install from PyPI\npip install git+https://github.com/twu/skjold.git@vX.X.X  # Install from Github\n```\n\nThis should provide a script named `skjold` that can then be invoked. See [Usage](#usage).\n\n## Usage\n```sh\n$ pip list --format=freeze | skjold -v audit --sources gemnasium -\n```\n\nWhen running `audit` one can either provide a path to a _frozen_ `requirements.txt`, a `poetry.lock` or a `Pipfile.lock` file. Alternatively, dependencies can also be passed in via `stdin`  (formatted as `package==version`).\n\n`skjold` will maintain a local cache (under `cache_dir`) that will expire automatically after `cache_expires` has passed. The `cache_dir` and `cache_expires` can be adjusted by setting them in  `tools.skjold` section of the projects `pyproject.toml` (see [Configuration](#configuration) for more details). The `cache_dir`will be created automatically, and by default unless otherwise specified will be located under `$HOME/.skjold/cache`.\n\nFor further options please read `skjold --help` and/or `skjold audit --help`.\n\n### Examples\n\nAll examples involving `github` assume that `SKJOLD_GITHUB_API_TOKEN` is already set (see [Github](#github)).\n\n```sh\n# Using pip list. Checking against GitHub only.\n$ pip list --format=freeze | skjold audit -s github -\n\n# Be verbose. Read directly from supported formats.\n$ skjold -v audit requirements.txt\n$ skjold -v audit poetry.lock\n$ skjold -v audit Pipenv.lock\n\n# Using poetry.\n$ poetry export -f requirements.txt | skjold audit -s github -s gemnasium -s pyup -\n\n# Using poetry, format output as json and pass it on to jq for additional filtering.\n$ poetry export -f requirements.txt | skjold audit -o json -s github - | jq \'.[0]\'\n\n# Using Pipenv, checking against Github\n$ pipenv run pip list --format=freeze | skjold audit -s github -\n\n# Checking a single package via stdin against Github and format findings as json.\n$ echo "urllib3==1.23" | skjold audit -o json -r -s github -\n[\n  {\n    "severity": "HIGH",\n    "name": "urllib3",\n    "version": "1.23",\n    "versions": "<1.24.2",\n    "source": "github",\n    "summary": "High severity vulnerability that affects urllib3",\n    "references": [\n      "https://nvd.nist.gov/vuln/detail/CVE-2019-11324"\n    ],\n    "url": "https://github.com/advisories/GHSA-mh33-7rrq-662w"\n  }\n]\n\n# Checking a single package via stdin against Gemnasium and report findings (`-o cli`).\n$ echo "urllib3==1.23" | skjold audit -o cli -r -s gemnasium -\n\nurllib3==1.23 (<=1.24.2) via gemnasium\n\nCRLF injection. In the urllib3 library for Python, CRLF injection is possible\nif the attacker controls the request parameter.\nhttps://nvd.nist.gov/vuln/detail/CVE-2019-11236\n--\n\nurllib3==1.23 (<1.24.2) via gemnasium\n\nWeak Authentication Caused By Improper Certificate Validation. The urllib3\nlibrary for Python mishandles certain cases where the desired set of CA\ncertificates is different from the OS store of CA certificates, which results\nin SSL connections succeeding in situations where a verification failure is the\ncorrect outcome. This is related to use of the `ssl_context`, `ca_certs`, or\n`ca_certs_dir` argument.\nhttps://nvd.nist.gov/vuln/detail/CVE-2019-11324\n--\n\nurllib3==1.23 (<1.25.9) via gemnasium\n\nInjection Vulnerability. urllib3 allows CRLF injection if the attacker controls\nthe HTTP request method, as demonstrated by inserting `CR` and `LF` control\ncharacters in the first argument of `putrequest()`. NOTE: this is similar to\nCVE-2020-26116.\nhttps://nvd.nist.gov/vuln/detail/CVE-2020-26137\n--\n\n# Ignore PYSEC-2020-148 finding from PyPA source until a certain date with a specific reason.\n$ skjold ignore urllib3 PYSEC-2020-148 --reason "Very good reason." --expires "2021-01-01T00:00:00+00:00"\nIgnore urllib3 in PYSEC-2020-148 until 2021-01-01 00:00:00+00:00?\nVery good reason.\n--\nAdd to \'.skjoldignore\'? [y/N]: y\n\n# Ignore PYSEC-2020-148 finding from PyPA source for 7 days with "No immediate remediation." reason.\n$ skjold ignore urllib3 PYSEC-2020-148\nIgnore urllib3 in PYSEC-2020-148 until ...?\nNo immediate remediation.\n--\nAdd to \'.skjoldignore\'? [y/N]: y\n\n# Audit `poetry.lock` using a custom `.skjoldignore` file location via `ENV`...\n$ SKJOLD_IGNORE_FILE=<path-to-file> skjold audit -s pyup poetry.lock\n\n# ... or using -i/--ignore-file\n$ skjold audit -s pyup -i <path-to-file> poetry.lock\n```\n\n### Configuration\n\n`skjold` can read its configuration from the `tools.skjold` section of a projects  `pyproject.toml`. Arguments specified via the command-line should take precedence over any configured or default value.\n\n```toml\n[tool.skjold]\nsources = ["github", "pyup", "gemnasium"]  # Sources to check against.\nreport_only = true                         # Report only, always exit with zero.\nreport_format = \'json\'                     # Output findings as `json`. Default is \'cli\'.\ncache_dir = \'.skjold_cache\'                # Cache location (default: `~/.skjold/cache`).\ncache_expires = 86400                      # Cache max. age.\nignore_file = \'.skjoldignore\'              # Ignorefile location (default `.skjoldignore`).\nverbose = true                             # Be verbose.\n```\n\nTo take a look at the current configuration / defaults run:\n```shell\n$ skjold config\nsources: [\'pyup\', \'github\', \'gemnasium\']\nreport_only: True\nreport_format: json\nverbose: False\ncache_dir: .skjold_cache\ncache_expires: 86400\nignore_file = \'.skjoldignore\'\n```\n\n#### Github\n\nFor the `github` source to work you\'ll need to provide a Github API Token via an `ENV` variable named `SKJOLD_GITHUB_API_TOKEN`. You can [create a new Github Access Token here](https://github.com/settings/tokens). You *do not* have to give it *any* permissions as it is only required to query the [GitHub GraphQL API v4](https://developer.github.com/v4/) API.\n\n### Version Control Integration\nTo use `skjold` with the excellent [pre-commit](https://pre-commit.com/) framework add the following to the projects `.pre-commit-config.yaml` after [installation](https://pre-commit.com/#install).\n\n```yaml\nrepos:\n  - repo: https://github.com/twu/skjold\n    rev: vX.X.X\n    hooks:\n    - id: skjold\n      verbose: true  # Important if used with `report_only`, see below.\n```\n\nAfter running `pre-commit install` the hook should be good to go. To configure `skjold` in this scenario I recommend adding the entire configuration to the projects `pyproject.toml` instead of manipulating the hook `args`. See this projects [pyproject.toml](./pyproject.toml) for an example.\n\n> **Important!**: When using `skjold` as a `pre-commit`-hook it only gets triggered if you want to commit changed dependency files (e.g. `Pipenv.lock`, `poetry.lock`, `requirements.txt`,...).\n> It will not continuously check your dependencies on _every_ commit!\n\nYou could run `pre-commit run skjold --all-files` manually in your workflow/scripts or run `skjold` manually.\nIf you have a better solution please let me know!\n\n> **Important!**: If you use `report_only` in any way make sure that you add `verbose: true` to your hook configuration\notherwise `pre-commit` won\'t show you any output since the hook is always returning with a zero exit code due\nto `report_only` being set!\n\n## Contributing\nPull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n',
    'author': 'Thomas Wurmitzer',
    'author_email': 't.wurmitzer+github@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/twu/skjold',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
