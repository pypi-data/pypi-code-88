from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='hungtool',
      version='0.2',
      long_description = long_description,
      long_description_content_type="text/markdown",
      description='Taiwan No. 1',
      url='http://github.com/storborg/hungtool',
      author='Ming-Hung Hsu',
      author_email='m870920@gmail.com',
      license='MIT',
      packages=['hungtool'],
      zip_safe=False)