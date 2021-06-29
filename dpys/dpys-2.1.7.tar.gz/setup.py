from setuptools import setup, find_packages


classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='dpys',
  version='2.1.7',
  description='A library to simplify discord.py',
  long_description="The goal of DPYS is to make basic functionalities that every good bot needs easy to implement for beginners.",
  url='https://sites.google.com/view/dpys',  
  author='George Luca',
  author_email='fixingg@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='discord', 
  packages=find_packages(),
  install_requires=['discord.py==1.7.3']
)