from setuptools import setup

setup(
  name='CPT_GFFParser',
  version='1.1.1',
  author='Anthony Criscione',
  author_email='talkingbeaverthing@gmail.com',
  packages=['CPT_GFFParser'],
  #scripts=['bin/script1','bin/script2'],
  url='https://pypi.org/project/CPT-GFFParser/',
  license='LICENSE.txt',
  description='A Biopython extension package for I/O of GFF files',
  long_description=open('README.md').read(),
  install_requires=[
      "biopython",
  ],
)
