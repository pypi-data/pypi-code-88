from distutils.core import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
  name = 'vitess-helpers',
  packages = ['vitess_helpers'],
  version = '0.1.0',
  license='MIT',
  description = 'General purpose Vitess helper library',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'James Stenhouse',
  author_email = 'james.stenhouse@gmail.com',
  url = 'https://github.com/spookiej/vitess-helpers',
  download_url = 'https://github.com/spookiej/vitess-helpers/archive/refs/tags/0.1.0.tar.gz',
  keywords = ['vitess', 'shard', 'shard range'],
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)