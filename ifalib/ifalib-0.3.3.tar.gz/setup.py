import numpy
from setuptools import find_packages, setup
import subprocess
from distutils.command.install import install as _install
from distutils.core import setup, Extension

module_rdf = Extension('ifalib.librdf',
                    sources = ['ifalib/rdf.c'],
                    include_dirs=[numpy.get_include()]) 

module_neighbour = Extension('ifalib.libneighbour',
                    sources = ['ifalib/neighbour.c'],
                    include_dirs=[numpy.get_include()]) 

# class install(_install):
#     def run(self):
#         subprocess.call(['make', 'clean', '-C', 'ifalib'])
#         subprocess.call(['make', '-C', 'ifalib'])
#         _install.run(self)


setup(
    name='ifalib',
    # packages=find_packages(include=['ifalib']) + [numpy.get_include()],
    packages=['ifalib'],
    # package_data={'ifalib': ['ifalib/librdf.so']},
    # cmdclass={'install': install},
    ext_modules=[module_rdf, module_neighbour],
    version='0.3.3 ',
    url='https://github.com/IlyaFed/ifalib/tree/master',
    description='Ilya Fedorov Analysis',
    author='Ilya Fedorov',
    author_email='ilya.d.fedorov@phystech.edu',
    license='MIT',
    install_requires=[],
    setup_requires=[],
    tests_require=['pytest==4.4.1','pytest'],
)
