import os
import sys
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


# 'setup.py publish' shortcut.
if sys.argv[-1] in ['publish', 'package']:
	os.system('rm -f dist/*')
	os.system('python setup.py sdist')
	if sys.argv[-1] == 'publish':
		os.system('twine upload -r public dist/*')
	sys.exit()


about = {}
with open(os.path.join(here, 'clpsz', '__version__.py'), 'r') as f:
	exec(f.read(), about)

with open('README.md', 'r') as f:
	readme = f.read()


requires = [
	'click',
	'PyMySQL',
	'pysftp',
	'confluent_kafka',
]


setup(
	name=about['__title__'],
	version=about['__version__'],
	description=about['__description__'],
	long_description=readme,
	long_description_content_type='text/markdown',
	author=about['__author__'],
	author_email=about['__author_email__'],
	url=about['__url__'],
	license=about['__license__'],

	packages=[
		'clpsz',
	],
	package_dir={
		'clpsz': 'clpsz'
	},
	package_data={},
	include_package_data=True,

	install_requires=requires,
	entry_points={
		'console_scripts': [
			'clpsz-flag=clpsz.clpsz_flag:main',
			'clpsz-db-export=clpsz.clpsz_db_export:main',
			'clpsz-sftp=clpsz.clpsz_sftp:main',
			'clpsz-kafka-consumer=clpsz.clpsz_kafka_consumer:main',
			'clpsz-canal-parser=clpsz.clpsz_canal_parser:main',
			'clpsz-word-count=clpsz.clpsz_word_count:main',
		]
	}
)
