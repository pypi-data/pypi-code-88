from setuptools import setup,find_packages

version = '0.1.3'

with open('readme.md', 'r', encoding = 'utf-8') as f:
    long_description = f.read()
pkgs = [
    'somerandomstuff'
]
setup(
        name = 'somerandomstuff.py',
        version = version,
        description = 'A module to get info from somerandomstuff api',
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        url = "https://github.com/Sengolda/somerandomstuffpy",  
        author = 'Sengolda',
        license = 'MIT', 
        install_requires = ['requests'],
        packages = find_packages(include=['*']),
)