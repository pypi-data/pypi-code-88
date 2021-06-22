# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['replacy_issue_boundary']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=1.7.0,<2.0.0']}

setup_kwargs = {
    'name': 'replacy-issue-boundary',
    'version': '0.2.9',
    'description': 'A replaCy component to fix issue boundary, fix signle or double space at start, extend to next word if facing casing issue.',
    'long_description': '# replaCy Issue Boundary\n\nA replaCy component to fix issue boundary:\n* fix signle or double space at start.\n* fix double comma.\n* fix comma at start\n* fix parenthesis space.\n* fix first letter is a lower case.\n* extend to next word if facing casing issue.\n\n## Warning\n\nAdd after joiner to work\n\n## Install\n\n`poetry add replacy_issue_boundary`\n\nor\n\n`pip install replacy_issue_boundary`\n\n## Usage\n\n```python\nimport en_core_web_sm\nfrom replacy import ReplaceMatcher\nfrom replacy.db import load_json\nfrom replacy_issue_boundary import IssueBoundary\nfrom spacy.util import filter_spans\n\n\nnlp = en_core_web_sm.load()\nreplaCy = ReplaceMatcher(nlp, load_json(\'path to match dict(s)\'))\nissue_boundary = IssueBoundary()\nreplaCy.add_pipe(name="span_filter", component=filter_spans, before="joiner")\nreplaCy.add_pipe(issue_boundary, name="article_agreer", after="joiner")\n```\n\n## Developing\n\nThe CI/CD in this project is great. GitHub Actions run linting and tests on any PR. If you merge into master, [release-drafter](https://github.com/marketplace/actions/release-drafter) drafts a new release based on PR commits and tags (e.g. if the PR is tagged `feature` and `minor` it will create a minor version bump with the changes labeled as Features).\n\nI can\'t figure out the automatic versioning bit... leaving it in a broken state for now :/\n',
    'author': 'Sam Havens',
    'author_email': 'sam.havens@qordoba.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Qordobacode/replacy_issue_boundary',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
