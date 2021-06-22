"""Copyright (C) Nanosurf AG (2021)
License - MIT"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='nanosurf',
    version='0.3.10.1_3',
    author='Nanosurf AG',
    author_email='scripting@nanosurf.com',
    description='Python API for Nanosurf controllers',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['nanosurf','nanosurf.lowlevel', 'nanosurf.workflow',
              'nanosurf.fileio', 'nanosurf.demo', 'nanosurf.spmcontroller'],
    include_package_data = True,
    zip_safe=False,
    install_requires=['pywin32', 'matplotlib', 'notebook', 'psutil'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"
    ],
    python_requires='>=3.6'
)