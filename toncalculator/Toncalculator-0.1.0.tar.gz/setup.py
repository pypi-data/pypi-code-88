from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
# Reading readme.md
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# See note below for more information about classifiers
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Toncalculator',
    version='0.1.0',
    description='A basic calculator',
    #long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description=long_description + "\n\n" +
    open('CHANGELOG.md').read(),
    long_description_content_type='text/markdown',
    # the URL of your package's home page e.g. github link
    url='https://github.com/Tonmoy-abc/Toncalculator',
    author='Mahmudul Hahan Tonmoy',
    author_email='playerandgamertonmoy@gmail.com',
    license='MIT',  # note the American spelling
    classifiers=classifiers,
    # used when people are searching for a module, keywords separated with a space
    keywords='calculator, toncalculator, add, addison, subdivision, log, sin, cos, tan, coat, sce, cosec, a simple calculator, fine calculator, terminal calculator, scitific calculator',
    packages=find_packages(),
    # a list of other Python modules which this module depends on.  For example RPi.GPIO
    install_requires=['']
)
