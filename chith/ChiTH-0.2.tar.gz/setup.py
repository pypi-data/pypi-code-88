from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='ChiTH',
      version='0.2',
      long_description = long_description,
      long_description_content_type="text/markdown",
      description='Taiwan No. 1',
      url='http://github.com/storborg/ChiTH',
      author='jonathan',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['ChiTH'],
      zip_safe=False)
