from setuptools import setup, find_packages

setup(
    name= 'SymmetryGecko', # for pip install
    #packages= ['SymmetryGecko'],
    packages= find_packages(exclude=[]),
    include_package_data=True,
    version= '0.0.15',
    license= 'MIT',
    description= 'CoinGecko API for Symmetry Finance',
    author= 'Mr. Bluesky',
    author_email= 'solana.bluesky@gmail.com',
    url = 'https://github.com/symmetry-protocol/coingeckoAPI.git',
    download_url = 'https://github.com/symmetry-protocol/coingeckoAPI.git',
    intsall_requires= [
        'requests'
    ],
    classifiers= [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)