from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='nikki30201',
      version='0.1',
      long_description = long_description,
      long_description_content_type="text/markdown",
      description='Taiwan No. 1',
      url='http://github.com/storborg/nikki30201',
      author='Michael Chen',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['nikki30201'],
      zip_safe=False)