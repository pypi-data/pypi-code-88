from setuptools import setup, find_packages

# Source: https://github.com/chardet/chardet/blob/master/setup.py
#     get version without importing (avoids dependency issues)
def get_version():
    import re

    with open("src/parsearg/version.py") as version_file:
        return re.search(
            r"""__version__\s+=\s+(['"])(?P<version>.+?)\1""", version_file.read()
        ).group("version")


def readme():
    with open('README.md', 'r') as fh:
        long_description = fh.read()

    return long_description


setup(
    name='parsearg',
    version=get_version(),
    author='Thomas P. Harte',
    author_email='tharte@cantab.net',
    maintainer='Thomas P. Harte',
    maintainer_email='tharte@cantab.net',
    description='parsearg turns argparse on its head the declarative way',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/tharte/parsearg',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["CLI", "subcommand", "parser", "argparse"],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
)
