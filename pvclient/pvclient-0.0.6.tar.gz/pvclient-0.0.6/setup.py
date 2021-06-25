import setuptools
from os import path

__version__ = "0.0.6"
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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'purview = pvclient.purview:main'
        ],
    },
    package_dir={"pvclient": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)