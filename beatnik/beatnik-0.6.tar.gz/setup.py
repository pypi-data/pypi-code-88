from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'beatnik',
  packages = ['beatnik'],
  version = '0.6',
  license='MIT',
  description = 'beatnik interpreter',
  #long_description=long_description,
  #long_description_content_type="text/markdown",
  author = 'Experimental Informatics',
  author_email = 't.liu@khm.de',
  url = 'https://github.com/experimental-informatics/beatnik',
  keywords = ['beatnik', 'esoteric programming language', 'stack-based'],
  install_requires=[
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
