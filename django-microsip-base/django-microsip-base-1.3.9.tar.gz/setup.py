import os
import compileall
import sys

from setuptools import setup, find_packages
import pathlib

if "sdist" in sys.argv:
    path = os.path.abspath(os.path.dirname(__file__))+"\\django_microsip_base\\"
    compileall.compile_dir(path, force=True)

# with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
#     README = readme.read()
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.rst').read_text(encoding='utf-8')
# this grabs the requirements from requirements.txt
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-microsip-base',
    version='1.3.9',
    packages=find_packages(),
    include_package_data=True,
    description="Django Microsip Base",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Servicios de Ingenieria Computacional",
    author_email="desarrollo@siccomputacion.com",
    url = '',   
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=REQUIREMENTS,
)
