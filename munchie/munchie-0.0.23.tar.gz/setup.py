from os import path
from setuptools import setup, find_packages

VERSION = '0.0.23'
DESCRIPTION = 'Pre-packaged common functions for day-to-day'
readme_path = path.join(path.abspath(path.dirname(__file__)), 'README.md')
with open(readme_path, encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

print(LONG_DESCRIPTION)

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="munchie",
    version=VERSION,
    author="Anthony Gaetano",
    author_email="adgaetano@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[
        "pathlib",
        "pendulum",
        "pyyaml",
        "rich"
    ],
    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Operating System :: MacOS :: MacOS X",
    ],
    python_requires='>=3.8, <3.10',
)
