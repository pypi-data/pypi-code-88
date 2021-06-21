# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['antsichaut']

package_data = \
{'': ['*']}

install_requires = \
['ConfigArgParse>=1.4.1,<2.0.0', 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['antsichaut = antsichaut.antsichaut:main']}

setup_kwargs = {
    'name': 'antsichaut',
    'version': '0.1.2',
    'description': 'antsichaut automates ansible changelog generation from GitHub Pull Requests',
    'long_description': '# Antsichaut\n\nThis is a very rough first try at automating the parts\nof creating a `changelog.yaml` used by antsibull-changelog.\n\nYou define a Github repository and a Github release. Then the script\nsearches all pull requests since the release and adds them to the `changelog.yaml`.\n\nThe PR\'s get categorized into the changelog-sections based on labels and\naccording to this configuration (currently hardcoded):\n\n```\ngroup_config = [\n  {"title": "major_changes", "labels": ["major", "breaking"]},\n  {"title": "minor_changes", "labels": ["minor", "enhancement"]},\n  {"title": "breaking_changes", "labels": ["major", "breaking"]},\n  {"title": "deprecated_features", "labels": ["deprecated"]},\n  {"title": "removed_features", "labels": ["removed"]},\n  {"title": "security_fixes", "labels": ["security"]},\n  {"title": "bugfixes", "labels": ["bug", "bugfix"]},\n]\n```\n\nThis means for example that PR\'s with the label `major` get categorized\ninto the `major_changes` section of the changelog.\n\nPR\'s that do not have one of the above labels get categorized into the\n`trivial` section.\n\n## Installation\n\nInstall the requirements:\n\n```\npip install -r requirements.txt\n```\n\n\n## Usage\n\nYou need a minimal `changelog.yml` created by antsibull-changelog:\n\n```\nantsibull-changelog release --version 1.17.0\n```\n\nThen define the version and the github repository you want to fetch the PRs from.\nEither via arguments or via environment variables:\n\n```\n> python3 antsi_change_pr_getter.py --github_token 123456789012345678901234567890abcdefabcd --since_version 1.17.0 --to_version 1.18.0 --github_repository=T-Systems-MMS/ansible-collection-icinga-director\n```\n\n```\nexport SINCE_VERSION=1.17.0  # (or `latest`)\nexport TO_VERSION=1.18.0     # optional. if unset, defaults to current date\nexport GITHUB_REPOSITORY=T-Systems-MMS/ansible-collection-icinga-director\n```\n\n## Acknowledgements and Kudos\n\nThis script was initially forked from https://github.com/saadmk11/changelog-ci/\nand modified to suit my needs. Thank you, @saadmk11!\n\n## License\n\nThe code in this project is released under the MIT License.\n',
    'author': 'Sebastian Gumprich',
    'author_email': 'sebastian.gumprich@t-systems.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rndmh3ro/antsichaut',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
