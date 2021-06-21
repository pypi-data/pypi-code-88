import os
from setuptools import setup, find_packages

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8",
]

# Get the long description from the README file
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
readme = os.path.join(CURRENT_PATH, "README.md")
with open(readme, "r") as fh:
    readme_data = fh.read()

setup(
  name='postcode-validator',
  version=open('version.txt').read(),
  description='Postcode Validator Library',
  long_description=readme_data,
  long_description_content_type="text/markdown",
  url='https://github.com/GouthamSiddhaarth/postcode_validator',
  author='Goutham Siddhaarth M.S.K',
  author_email='mskgouthamsiddhaarth@gmail.com',
  license='MIT',
  classifiers=classifiers,
  packages=find_packages(),
  install_requires=['']
)
