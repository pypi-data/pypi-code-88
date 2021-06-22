# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aura',
 'aura.analyzers',
 'aura.analyzers.python',
 'aura.analyzers.python.taint',
 'aura.data',
 'aura.output',
 'aura.uri_handlers',
 'tests',
 'tests.files',
 'tests.files.diffs.1_a',
 'tests.files.diffs.1_b',
 'tests.files.import_tester.mypackage',
 'tests.files.import_tester.mypackage.sub1',
 'tests.files.import_tester.mypackage.sub2',
 'tests.files.pyt_examples',
 'tests.files.pyt_examples.sql']

package_data = \
{'': ['*'],
 'tests.files': ['malformed_xmls/*', 'mirror/*', 'templates/*'],
 'tests.files.pyt_examples': ['templates/*']}

install_requires = \
['click>=8.0,<8.1',
 'colorama>=0.4.4,<0.5.0',
 'jinja2>=3.0,<3.1',
 'packaging>=20.9,<20.10',
 'prettyprinter>=0.18.0,<0.19.0',
 'python-magic>=0.4.24,<0.5.0',
 'python-tlsh>=3.17.0,<3.18.0',
 'pytz>=2021.1,<2021.2',
 'requests>=2.25.1,<2.26.0',
 'ruamel.yaml>=0.17.7,<0.18.0',
 'tqdm>=4.61,<4.62']

extras_require = \
{'full': ['jsonschema>=3.2,<3.3',
          'GitPython>=3.1,<3.2',
          'defusedxml>=0.7,<0.8',
          'tomlkit>=0.7,<0.8',
          'yara-python>=4.0.5,<4.1.0',
          'networkx>=2.5,<2.6',
          'python-rapidjson>=1.0,<1.1']}

entry_points = \
{'aura.analyzers': ['archive = aura.analyzers.archive:archive_analyzer',
                    'crypto_gen_key = '
                    'aura.analyzers.python.crypto:CryptoGenKey',
                    'data_finder = aura.analyzers.data_finder:DataFinder',
                    'file_analyzer = aura.analyzers.fs_struct:analyze',
                    'jinja = aura.analyzers.python.jinja:JinjaAnalyzer',
                    'misc = aura.analyzers.python.misc:MiscAnalyzer',
                    'pypirc = aura.analyzers.pypirc:analyze',
                    'pyproject_toml = '
                    'aura.analyzers.pyproject:analyze_pyproject',
                    'req_analyzer = '
                    'aura.analyzers.requirements_analyzer:analyze_requirements_file',
                    'secrets = aura.analyzers.python.secrets:SecretsAnalyzer',
                    'setup_py = aura.analyzers.setup:SetupPy',
                    'sqli = aura.analyzers.python.sqli:SQLi',
                    'stats = aura.analyzers.stats:analyze',
                    'string_finder = aura.analyzers.data_finder:StringFinder',
                    'taint_analysis = '
                    'aura.analyzers.python.taint.base:TaintDetection',
                    'wheel = aura.analyzers.wheel:analyze_wheel',
                    'xml = aura.analyzers.xml:analyze',
                    'yara = aura.analyzers.yara_scan:analyze'],
 'aura.ast_visitors': ['ast_pattern_matching = '
                       'aura.analyzers.python.pattern_matching_visitor:ASTPatternMatcherVisitor',
                       'convert = aura.analyzers.python.convert_ast:ASTVisitor',
                       'readonly = '
                       'aura.analyzers.python.readonly:ReadOnlyAnalyzer',
                       'rewrite = aura.analyzers.python.rewrite_ast:ASTRewrite',
                       'taint_analysis = '
                       'aura.analyzers.python.taint.visitor:TaintAnalysis'],
 'aura.diff_hooks': ['diff_archive = aura.analyzers.archive:diff_archive'],
 'aura.diff_output_handlers': ['json = aura.output.json:JSONDiffOutput',
                               'sqlite = aura.output.sqlite:SQLiteDiffOutput',
                               'text = aura.output.text:TextDiffOutput'],
 'aura.info_output_handlers': ['text = aura.output.text:TextInfoOutput'],
 'aura.input_hooks': ['package_enrichment = '
                      'aura.analyzers.package_enrichment:analyze',
                      'typosquatting = aura.analyzers.typosquatting:analyze'],
 'aura.output_handlers': ['gitlab-sast = aura.output.gitlab:GitlabSASTOutput',
                          'json = aura.output.json:JSONScanOutput',
                          'sarif = aura.output.sarif:SARIFOutput',
                          'sqlite = aura.output.sqlite:SQLiteScanOutput',
                          'text = aura.output.text:TextScanOutput'],
 'aura.typosquatting_output_handlers': ['json = '
                                        'aura.output.json:JSONTyposquattingOutput',
                                        'text = '
                                        'aura.output.text:TextTyposquattingOutput'],
 'aura.uri_handlers': ['git = aura.uri_handlers.git:GitRepoHandler',
                       'local = aura.uri_handlers.local:LocalFileHandler',
                       'mirror = aura.uri_handlers.mirror:MirrorHandler',
                       'pypi = aura.uri_handlers.pypi:PyPiHandler'],
 'console_scripts': ['apip = aura.apip:main', 'aura = aura.cli:main']}

setup_kwargs = {
    'name': 'aura-security',
    'version': '2.1',
    'description': 'Security auditing and static analysis for python',
    'long_description': '.. image:: files/logo/logotype.png\n   :target: https://aura.sourcecode.ai/\n\n\n======\n\n.. class:: center\n\n    |homepage_flair| |docs_flair| |docker_flair|\n    |license_flair| |travis_flair|\n\n\n\nSecurity auditing and static code analysis\n=================================================\n\nAura is a static analysis framework developed as a response to the ever-increasing threat of malicious packages and vulnerable code published on PyPI.\n\n\nProject goals:\n\n* provide an automated monitoring system over uploaded packages to PyPI, alert on anomalies that can either indicate an ongoing attack or vulnerabilities in the code\n* enable an organization to conduct automated security audits of the source code and implement secure coding practices with a focus on auditing 3rd party code such as python package dependencies\n* allow researches to scan code repositories on a large scale, create datasets and perform analysis to further advance research in the area of vulnerable and malicious code dependencies\n\n\nFeature list:\n\n- Suitable for analyzing malware with a guarantee of a zero-code execution\n- Advanced deobfuscation mechanisms by rewriting the AST tree - constant propagations, code unrolling, and other dirty tricks\n- Recursive scanning automatically unpacks archives such as zips, wheels, etc.. and scans the content\n- Support scanning also non-python files - plugins can work in a “raw-file” mode such as the built-in Yara integration\n- Scan for hardcoded secrets, passwords, and other sensitive information\n- Custom diff engine - you can compare changes between different data sources such as typosquatting PyPI packages to what changes were made\n- Works for both Python 2.x and Python 3.x source code\n- High performance, designed to scan the whole PyPI repository\n- Output in numerous formats such as pretty plain text, JSON, SQLite, SARIF, etc…\n- Tested on over 4TB of compressed python source code\n- Aura is able to report on code behavior such as network communication, file access, or system command execution\n- Compute the “Aura score” telling you how trustworthy the source code/input data is\n- and much much more…\n\nDidn\'t find what you are looking for? Aura\'s architecture is based on a robust plugin system, where you can customize almost anything, ranging from a set of data analyzers, transport protocols to custom out formats.\n\n\nInstallation\n============\n\n::\n\n    poetry install --no-dev -E full\n\nOr just use a prebuild docker image ``sourcecodeai/aura:dev``\n\n\nRunning Aura\n============\n\n::\n\n    docker run -ti --rm sourcecodeai/aura:dev scan pypi://requests -v\n\nAura uses a so-called URIs to identify the protocol and location to scan, if no protocol is used, the scan argument is treated as a path to the file or directory on a local system.\n\n\n.. image:: files/imgs/aura_scan.png\n\n\nDiff packages::\n\n    docker run -ti --rm sourcecodeai/aura:dev diff pypi://requests pypi://requests2\n\n\n.. image:: docs/source/_static/imgs/aura_diff.png\n\n\nFind most popular typosquatted packages (you need to call ``aura update`` to download the dataset first)::\n\n    aura find-typosquatting --max-distance 2 --limit 10\n\n\n.. image:: https://asciinema.org/a/367999.svg\n   :target: https://asciinema.org/a/367999\n\n----\n\n.. image:: files/imgs/download_dataset.png\n   :target: https://cdn.sourcecode.ai/pypi_datasets/index/datasets.html\n   :align: center\n   :width: 256\n\n\nWhy Aura?\n---------\n\nWhile there are other tools with functionality that overlaps with Aura such as Bandit, dlint, semgrep etc. the focus of these alternatives is different which impacts the functionality and how they are being used. These alternatives are mainly intended to be used in a similar way to linters, integrated into IDEs, frequently run during the development which makes it important to **minimize false positives** and reporting with clear **actionable** explanations in ideal cases.\n\nAura on the other hand reports on ** behavior of the code**, **anomalies**, and **vulnerabilities** with as much information as possible at the cost of false positive. There are a lot of things reported by aura that are not necessarily actionable by a user but they tell you a lot about the behavior of the code such as doing network communication, accessing sensitive files, or using mechanisms associated with obfuscation indicating a possible malicious code. By collecting this kind of data and aggregating it together, Aura can be compared in functionality to other security systems such as antivirus, IDS, or firewalls that are essentially doing the same analysis but on a different kind of data (network communication, running processes, etc).\n\nHere is a quick overview of differences between Aura and other similar linters and SAST tools:\n\n- **input data**:\n    - **Other SAST tools** - usually restricted to only python (target) source code and python version under which the tool is installed.\n    - **Aura** can analyze both binary (or non-python code) and python source code as well. Able to analyze a mixture of python code compatible with different python versions (py2k & py3k) using **the same Aura installation**.\n- **reporting**:\n    - **Other SAST tools** - Aims at integrating well with other systems such as IDEs, CI systems with actionable results while trying to minimize false positives to prevent overwhelming users with too many non-significant alerts.\n    - **Aura** - reports as much information as possible that is not immediately actionable such as behavioral and anomaly analysis. The output format is designed for easy machine processing and aggregation rather than human readable.\n- **configuration**:\n    - **Other SAST tools** - The tools are fine-tuned to the target project by customizing the signatures to target specific technologies used by the target project. The overriding configuration is often possible by inserting comments inside the source code such as ``# nosec`` that will suppress the alert at that position\n    - **Aura** - it is expected that there is little to no knowledge in advance about the technologies used by code that is being scanned such as auditing a new python package for approval to be used as a dependency in a project. In most cases, it is not even possible to modify the scanned source code such as using comments to indicate to linter or aura to skip detection at that location because it is scanning a copy of that code that is hosted at some remote location.\n\n\nAuthors & Contributors\n======================\n\n* **Martin Carnogursky** - *Initial work and project lead* - https://is.muni.cz/person/410345\n* **Mirza Zulfan** - *Logo Design* - https://github.com/mirzazulfan\n\n\nDonate\n======\n\n* GitHub Sponsors: https://github.com/sponsors/RootLUG\n* Liberapay: https://liberapay.com/SourceCode.AI\n* BuyMeACoffee: https://www.buymeacoffee.com/SourceCodeAI\n* BTC: 3FVTaLsLwTDinmDjPh3BjS1qv3bYHbkcYc\n* XMR: 46xvWZGCexo1NbvjLMMpLB1GhRd819AQr8eFPJT1q6kKMuuDy43JLiESh9XUM3asjk4SVUYqGakFVQZRY1adx8cS6ka4EXr\n* ETH/ERC20: 0x708F1A08E3ee4922f037673E720c405518C0Ec85\n\n\nLICENSE\n=======\nAura framework is licensed under the **GPL-3.0**.\nDatasets produced from global scans using Aura are released under the **CC BY-NC 4.0** license.\nUse the following citation when using Aura or data produced by Aura in research:\n\n::\n\n    @misc{Carnogursky2019thesis,\n    AUTHOR = "CARNOGURSKY, Martin",\n    TITLE = "Attacks on package managers [online]",\n    YEAR = "2019 [cit. 2020-11-02]",\n    TYPE = "Bachelor Thesis",\n    SCHOOL = "Masaryk University, Faculty of Informatics, Brno",\n    SUPERVISOR = "Vit Bukac",\n    URL = "Available at WWW <https://is.muni.cz/th/y41ft/>",\n    }\n\n\n.. |homepage_flair| image:: https://img.shields.io/badge/Homepage-aura.sourcecode.ai-blue\n   :target: https://aura.sourcecode.ai/\n   :align: middle\n\n.. |docs_flair| image:: https://img.shields.io/badge/-Documentation-blue\n   :target: https://docs.aura.sourcecode.ai/\n   :align: middle\n\n.. |docker_flair| image:: https://img.shields.io/badge/docker-SourceCodeAI/aura-blue\n   :target: https://hub.docker.com/r/sourcecodeai/aura\n   :align: middle\n\n.. |license_flair| image:: https://img.shields.io/github/license/SourceCode-AI/aura?color=blue\n\n.. |travis_flair| image:: https://travis-ci.com/SourceCode-AI/aura.svg?branch=dev\n',
    'author': 'Martin Carnogursky',
    'author_email': 'admin@sourcecode.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://aura.sourcecode.ai/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
