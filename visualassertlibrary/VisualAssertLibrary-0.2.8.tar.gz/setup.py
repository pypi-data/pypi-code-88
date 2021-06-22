from setuptools import setup

version = '0.2.8'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='VisualAssertLibrary',
      version=version,
      description='Robot Framework Visual Assert Library',
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
      ],
      install_requires=[
          'mega.py',
          'Pillow',
          'robotframework',
          'robotframework-seleniumlibrary',
      ],
      packages=['VisualAssertLibrary'],
      author='Dmytro Bondarchuk',
      author_email='d.bondarchuk.spv@gmail.com',
      zip_safe=False)
