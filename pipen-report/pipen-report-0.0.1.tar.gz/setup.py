# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pipen_report']

package_data = \
{'': ['*']}

install_requires = \
['liquidpy', 'pipen', 'python-slugify>=4.0.0,<5.0.0']

entry_points = \
{'pipen': ['report = pipen_report:PipenReportPlugin']}

setup_kwargs = {
    'name': 'pipen-report',
    'version': '0.0.1',
    'description': 'Report generation system for pipen.',
    'long_description': '# pipen-report\n\nReport generation system for [`pipen`][1]\n\n## Installation\n\n```python\npip install -U pipen-report\n```\n\n## Usage\n\n```python\nfrom pipen import Proc, Pipen\n\nclass Figure(Proc):\n    """Generate figures"""\n    input_keys = [\'a:var\']\n    input = [1,2,3]\n    output = \'outfile:file:{{in.a}}.jpg\'\n    script = \'\'\'\\\n    wget https://picsum.photos/200/300 -O {{out.outfile}}\n    \'\'\'\n    plugin_opts = \'Figure.svx\'\n\nclass Table(Figure):\n    """Generate tables"""\n    output = \'outfile:file:{{in.a}}.txt\'\n    script = \'\'\'\\\n    #!/usr/bin/env python\n\n    outfile = "{{out.outfile}}"\n    with open(outfile, \'w\') as fout:\n        fout.write("""\\\\\n    id\tfirst_name\tlast_name\temail\tgender\tip_address\n    1\tLynda\tScirman\tlscirman0@businessweek.com\tFemale\t22.123.155.57\n    2\tMoll\tNiset\tmniset1@marketwatch.com\tFemale\t6.154.75.63\n    3\tJory\tMewitt\tjmewitt2@delicious.com\tMale\t233.225.101.101\n    4\tDukie\tOnslow\tdonslow3@washington.edu\tMale\t238.209.40.250\n    5\tCarlee\tGrasha\tcgrasha4@cocolog-nifty.com\tFemale\t22.65.237.2\n    6\tLeanora\tDoughtery\tldoughtery5@ucoz.com\tFemale\t54.41.211.142\n    7\tWinona\tLevison\twlevison6@cornell.edu\tFemale\t15.186.215.132\n    8\tOrrin\tBaldick\tobaldick7@miitbeian.gov.cn\tMale\t221.49.10.188\n    9\tIngmar\tPapez\tipapez8@dmoz.org\tMale\t225.88.240.74\n    10\tArlena\tCompford\tacompford9@earthlink.net\tFemale\t49.30.204.242\n    11\tDomenico\tLorinez\tdlorineza@hatena.ne.jp\tMale\t106.63.35.124\n    12\tYul\tBonifas\tybonifasb@nba.com\tMale\t198.152.245.214\n    13\tTony\tAntonignetti\ttantonignettic@skype.com\tMale\t61.64.103.108\n    14\tBayard\tGilhooley\tbgilhooleyd@addtoany.com\tMale\t124.48.176.234\n    15\tHillary\tAshbee\thashbeee@bbc.co.uk\tFemale\t111.91.131.252\n    16\tCherye\tSpuffard\tcspuffardf@amazon.com\tFemale\t206.113.100.79\n    17\tDorey\tLorraway\tdlorrawayg@t.co\tFemale\t179.210.96.234\n    18\tIolande\tMcKilroe\timckilroeh@ustream.tv\tFemale\t92.62.191.79\n    19\tErmina\tWoodroofe\tewoodroofei@independent.co.uk\tFemale\t193.75.48.192\n    20\tQuill\tSkoggins\tqskogginsj@t.co\tMale\t157.11.232.242\n    """)\n    \'\'\'\n    plugin_opts = \'Table.svx\'\n\nPipen(\'Test pipeline\',\n      \'Just for pipen-report testing\').starts([Figure, Table]).run()\n```\n\n`Figure.svx`\n\n```html\n# Generated Figures\n\n{% for job in jobs %}\n\n## This is a very long heading for figure {{job.index}}\n\n![Figure{{job.index}}]({{job.out.outfile}})\n\n{% endfor %}\n\n# Another very very veryvery veryvery very long heading at level 1\n\n## Short one\n\n### Third level\n\n## Very very very very very very very long one\n\n## Another short one\n```\n\n`Table.svx`\n\n```html\n<script>\nimport { DataTable } from "pipen-smelte";\n\n</script>\n\n# Heading 1\n\n## SubHeading 2\n<DataTable\n    data="{{ job.out.outfile | @report.datatable: delimiter=\'\\t\' }}"\n    datafile="{{ job.out.outfile }}"\n    />\n\n## SubHeading 3\n<DataTable\n    data="{{ jobs[1].out.outfile | @report.datatable: delimiter=\'\\t\', cols=[\'id\', \'first_name\', \'last_name\'], rows=10 }}"\n    datafile="{{ jobs[1].out.outfile }}"\n    />\n```\n\nSee [here][2] for the reports.\n\n[1]: https://github.com/pwwang/pipen\n[2]: https://pwwang.github.io/pipen-report\n',
    'author': 'pwwang',
    'author_email': 'pwwang@pwwang.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pwwang/pipen-report',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
