from setuptools import setup, find_packages

setup(
    name='sigmind_tools',
    version='0.1.1',    
    author='Sigmind',
    packages= ['sigmind_tools',],
    install_requires=[
                      'boto3'
                      ],
)