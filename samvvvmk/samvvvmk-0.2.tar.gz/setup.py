from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='samvvvmk',
      version='0.2',
      long_description = long_description,
      long_description_content_type="text/markdown",
      description='basic function',
      url='http://github.com/storborg/funniest',
      author='samvvv2002',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['samvvvmk'],
      zip_safe=False)