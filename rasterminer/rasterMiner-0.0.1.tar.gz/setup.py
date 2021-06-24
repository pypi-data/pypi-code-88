import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'rasterMiner',
    version = '0.0.1',
    author = 'Rage Uday Kiran',
    author_email = 'uday.rage@gmail.com',
    description = 'Raster Mining',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/udayRage/rasterMiner.git',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
)
