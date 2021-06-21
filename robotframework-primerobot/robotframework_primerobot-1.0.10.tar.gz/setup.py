from setuptools import setup, find_packages

setup(
    name='robotframework_primerobot',
    version='1.0.10',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'PyYAML',
        'typing_extensions',
        'pandas==1.2.3',
        'gql==3.0.0a2',
        'elasticsearch_dsl'
    ],
)
