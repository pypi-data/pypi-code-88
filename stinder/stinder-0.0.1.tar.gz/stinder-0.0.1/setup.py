from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='stinder',
    version='0.0.1',
    description='Stinder aims to help students find compatible study partners through their major and coursework for optimal study sessions.',
    long_description = long_description,
    url='https://github.com/gibbons-eddie/Stinder',
    author='Eddie Gibbons, Allison Denham, Carlos Echenique, Wyatt Townsend, Yuchen Xiong',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=find_packages(where='src'),
    python_requires='>=3.8.2, <4'
)