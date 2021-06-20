from setuptools import setup, find_packages

setup(
   name='htlib',
   version='0.7',
   description='',
   long_description=open("README.md").read(),
   download_url="https://github.com/harol1997/htlib/archive/refs/heads/main.zip",
   install_requires=[i.strip() for i in open("requirements.txt").readlines()],
   author='Harol Alvardo',
   author_email='harolav3@gmail.com',
   long_description_content_type="text/markdown",
   url="https://github.com/harol1997/htlib",
   packages=find_packages(),
   license="MIT",
   include_package_data=True
)