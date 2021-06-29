import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='bln-tools',
    version='0.0.1',
    author='Daniel Jenson',
    author_email='djenson@stanford.edu',
    description='Big Local News Tools',
    license='GNU GPLv3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    platform='OS Independent',
    url='https://github.com/biglocalnews/tools',
    packages=setuptools.find_packages(),
    scripts=[
        'scripts/harmonizer',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'fuzzywuzzy',
        'numpy',
        'pandas',
        'python-Levenshtein',
        'sklearn',
    ],
)
