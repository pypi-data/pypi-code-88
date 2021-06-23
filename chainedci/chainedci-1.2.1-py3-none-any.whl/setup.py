#!/usr/bin/env python3

"""Setup and install chainedci."""

from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def readme():
    """Set Readme from file."""
    with open('README.md') as f:
        return f.read()


version = {}
with open("chainedci/version.py") as fp:
    exec(fp.read(), version)

setup(name='chainedci',
      version=version['__version__'],
      description='Chaine Gitlab CI pipelines',
      long_description=readme(),
      url='https://gitlab.com/Orange-OpenSource/lfn/ci_cd/chained-ci',
      author='Orange OpenSource',
      license='Apache 2.0',
      packages=find_packages('.'),
      py_modules=[splitext(basename(path))[0] for path in glob('*.py')],
      include_package_data=True,
      scripts=["chainedci/chainedci"],
      install_requires=[
          "ansible-base==2.10.*",
          "schema",
          "requests"
      ],
      setup_requires=["pytest-runner"],
      tests_require=[
          "pytest",
          "pytest-cov",
          "pytest-mock",
          "mock",
          "requests_mock"
      ],
      zip_safe=False)
