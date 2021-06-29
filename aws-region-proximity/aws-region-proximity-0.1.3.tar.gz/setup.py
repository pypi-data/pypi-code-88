from codecs import open
import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), 'r') as infile:
    long_description = infile.read()

about = {}
with open(os.path.join(here, 'aws_region_proximity', '__version__.py'), 'r', encoding='utf-8') as infile:
    exec(infile.read(), about)

setup(
    name='aws-region-proximity',
    version=about['__version__'],
    packages=[
        'aws_region_proximity'
    ],
    zip_safe=True,
    include_package_data=True,
    url='https://github.com/phistrom/aws-region-proximity',
    license='MIT',
    author='Phillip Stromberg',
    author_email='phillip@strombergs.com',
    description='Generates a list of AWS regions closest to each other',
    install_requires=[
        "haversine",
    ],
    entry_points={
        'console_scripts': [
            'aws-regions = aws_region_proximity:cli',
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
