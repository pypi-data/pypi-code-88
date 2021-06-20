from setuptools import setup, find_packages

setup(
   name='htlib',
   version='0.9',
   description='',
   long_description=open("README.md").read(),
   download_url="https://github.com/harol1997/htlib/archive/refs/heads/main.zip",
   install_requires=[
        "certifi==2020.12.5",
        "chardet==4.0.0",
        "idna==2.10",
        "pyserial==3.5",
        "requests==2.25.1",
        "urllib3==1.26.2"
   ],
   author='Harol Alvardo',
   author_email='harolav3@gmail.com',
   long_description_content_type="text/markdown",
   url="https://github.com/harol1997/htlib",
   packages=find_packages(),
   license="MIT",
   include_package_data=True
)