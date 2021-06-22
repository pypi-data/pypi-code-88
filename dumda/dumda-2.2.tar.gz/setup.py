from setuptools import setup
import os
from setuptools import find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()


setup(name='dumda',
      version='2.2',
      description='generate highly customizable dummy data for data science testing',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      keywords=['data science', 'python'],
      url='https://github.com/oliverbdot/dumda',
      author='Oliver B.',
      author_email='oliverbcontact@gmail.com',
      license='MIT',
      packages=['dumda'],
      include_package_data=True,
      zip_safe=False)
