import setuptools
import os

def read(filepath):
    return open(os.path.join(os.path.dirname(__file__), filepath)).read()


setuptools.setup(
    name='FastaDist',
    version='1.0.1',
    description='Package to calculate a distance matrix from a multiple sequence file',
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author='Anthony Underwood',
    author_email='au3@sanger.ac.uk',
    license='MIT',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'fastadist = fastadist.run_fastadist:main'
        ]
    },
    python_requires='>=3',
    install_requires=['biopython', 'bitarray', 'parmap', 'tqdm', 'dendropy'],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[ 
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Science/Research', 
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)