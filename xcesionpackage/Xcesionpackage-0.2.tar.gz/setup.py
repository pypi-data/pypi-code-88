from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='Xcesionpackage',
      version='0.2',
      long_description = long_description,
      long_description_content_type="text/markdown",
      description='Taiwan No. 1',
      url='http://github.com/storborg/Xcesionpackage',
      author='Michael Chen',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['Xcesionpackage'],
      zip_safe=False)