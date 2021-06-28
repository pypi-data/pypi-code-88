import setuptools
from os import path
from pvclient import __version__

# Read the contents of README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='pvclient',
    version=__version__,
    description="This package allows interacting with Azure Purview's REST API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Thanh-Truong/purview',
    author='Thanh Truong',
    author_email='tcthanh@gmail.com',
    license='MIT',
    install_requires = ['pyapacheatlas==0.6.0','azure-identity==1.6.0','azure-mgmt-resource==18.0.0','azure-mgmt-purview==1.0.0b1'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'purview = pvclient.client.main:main'
        ],
    },
    python_requires=">=3.6"
)