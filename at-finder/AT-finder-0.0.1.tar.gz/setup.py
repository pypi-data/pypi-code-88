from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python CLI for finding A/T rich regions in genbank files.'
LONG_DESCRIPTION = 'This package contains a CLI for finding A/T rich regions in genbank (.gb) files and updating the feature set of the file.'

# Setting up
setup(
        name="AT-finder",
        version=VERSION,
        author="James Sanders",
        author_email="james.sanders1711@gmail.com",
        url = 'https://github.com/J-E-J-S/AT-finder',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            'biopython==1.78',
            'click==7.1.2'
        ],
        entry_points = {
            'console_scripts':['at-finder=atFinder.atFinder:cli']
        }
)
