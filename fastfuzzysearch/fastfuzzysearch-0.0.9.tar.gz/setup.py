from setuptools import setup
import subprocess
from sys import version_info as python_version

version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
assert "." in version


if python_version.major < 3:
    raise ValueError('Python %s is not supported' % python_version)

setup(
  name='fastfuzzysearch',  
  packages=['fastfuzzysearch'],  
  version=version, 
  license='BSD-3-Clause and Public-Domain',
  description='a Python package for fast fuzzy search entirely in-memory based',
  author='Eyal Paz',
  author_email='eyalsus@gmail.com',  
  url='https://github.com/eyalsus/fastfuzzysearch', 
  platforms=['Linux', 'MacOSX', 'Windows'],
  keywords=['search', 'fastsearch', 'fuzzy search', 'ngrams', 'aho-corasick', 'fastfuzzysearch', 'fuzzy'], 
  install_requires=[
          'fastsearch',
          'pyssdeep'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)