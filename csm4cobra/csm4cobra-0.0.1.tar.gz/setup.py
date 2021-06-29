import setuptools
from setuptools import find_packages

install_requires = ['numpy>=1.17.3', 'cobra>=0.22.0', 'corda>=0.4.2', 
                    'fastcore>=1.3.20', 'networkx>=2.5.1', 'pandas>=1.2.5']

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "csm4cobra",
    version = "0.0.1",
    author = "Miguel Ponce-de-Leon",
    author_email = "miguelponcedeleon@gmail.com",
    maintainer = "Miguel Ponce-de-Leon",
    maintainer_email = "miguelponcedeleon@gmail.com",
    description = "Tools and methods for context-specific metabolic modeling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/bsc-life/csm4cobra",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    
    packages=find_packages(exclude=['examples', 'docs', 'tests']),
    python_requires='>=3.6',
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['build-csm=csm4cobra.cmds.build_csm:main',
                            'run-insilico-exp=csm4cobra.cmds.run_insilico_experiment:main']
        
    }
)
