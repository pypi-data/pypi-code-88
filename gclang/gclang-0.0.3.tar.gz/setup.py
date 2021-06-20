from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="gclang",
    version='0.0.3',
    author="Makar Solomatin",
    description="Guarded command language interpreter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slmtnm/guarded",
    packages=find_packages(),
    py_modules=['gclang'],
    install_requires=[
        'Click',
        'sympy==1.7.1',
        'click==7.1.2',
        'antlr4-python3-runtime==4.7.2'
    ],
    entry_points='''
        [console_scripts]
        gclang=gclang.__main__:cli
    ''',
)
