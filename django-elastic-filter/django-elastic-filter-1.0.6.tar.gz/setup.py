from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(name='django-elastic-filter',
      version='1.0.6',
      description='Django Elastic Filter for models',
      license="MIT",
      long_description=long_description,
      author='Saeed Hassani Borzadaran',
      author_email='hassanisaeed19@gmail.com',
      packages=['django-elastic-filter'])
