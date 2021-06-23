from setuptools import setup, find_packages

setup(
    name = 'RBasisPy',
    packages = ['RBasisPy'],   
    include_package_data=True,    # muy importante para que se incluyan archivos sin extension .py
    version = '1.0',
    install_requires=['scikit-learn', 'numpy'],
    description = 'Implementation of a Radial Basis Network',
    author='Michael Guzmán',
    author_email="michael.guzman.personal@gmail.com",
    license="GPLv3",
    url="https://github.com/2mikeg/erbn",
    classifiers = ["Programming Language :: Python :: 3",\
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",\
        "Development Status :: 4 - Beta", "Intended Audience :: Developers", \
        "Operating System :: OS Independent"],
    )