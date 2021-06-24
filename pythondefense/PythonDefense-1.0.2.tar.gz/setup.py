from setuptools import setup

setup(
    name='PythonDefense',
    version='1.0.2',
    description='Tower defense game written in python',
    author='Alex Skladanek, Amer  Khalifa, Benjamin Coretese, Eric Weisfeld, Maxwell Walmer',
    url='https://github.com/mwalmer/Python-Defense',
    packages=['PythonDefense', ],
    entry_points={
        'console_scripts': [
            'play_PythonDefense=PythonDefense.main:main'
        ],
    },
    install_requires=[
        'pygame~=2.0.1'
    ],
    package_data={
        '': [
            'assets', 'assets/*'
        ],
    },
)
