from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='AEfunniest',
      version='0.2',
      long_description = long_description,
      long_description_content_type="text/markdown",
      description='I am Taiwanese',
      url='http://github.com/storborg/AEfunniest',
      author='Eason Hsieh',
      author_email='eason.hsieh@outlook.com',
      license='MIT',
      packages=['AEfunniest'],
      zip_safe=False)