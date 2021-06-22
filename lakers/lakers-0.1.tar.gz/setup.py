from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='lakers',
      version='0.1',
      long_description = long_description,
      long_description_content_type="text/markdown",
      description='Taiwan No. 1',
      url='http://github.com/storborg/lakers',
      author='Michael Chen',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['lakers'],
      zip_safe=False)