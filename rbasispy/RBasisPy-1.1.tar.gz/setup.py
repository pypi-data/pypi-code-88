from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'RBasisPy',
    packages = ['RBasisPy'],   
    include_package_data=True,    # muy importante para que se incluyan archivos sin extension .py
    version = '1.01',
    install_requires=['scikit-learn', 'numpy'],
    description = 'Implementation of a Radial Basis Network',
    author='Michael Guzmán',
    author_email="michael.guzman.personal@gmail.com",
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    license="GPLv3",
    url="https://github.com/2mikeg/erbn",
    classifiers = ["Programming Language :: Python :: 3",\
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",\
        "Development Status :: 4 - Beta", "Intended Audience :: Developers", \
        "Operating System :: OS Independent"],
    )