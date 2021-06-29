from setuptools import setup

f = open('README.md', 'r')
long_description = f.read()
f.close()

setup(
        long_description=long_description,
        long_description_content_type='text/markdown',
        )
