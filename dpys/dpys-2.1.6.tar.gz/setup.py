from setuptools import setup, find_packages


classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='dpys',
  version='2.1.6',
  description='Docs: https://sites.google.com/view/dpys',
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