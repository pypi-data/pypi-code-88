from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='whist-core',
    version='0.1.0rc2',
    author='Whist Team',
    description='Game implementation of Whist.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Whist-Team/Whist-Core',
    project_urls={
        'Bug Tracker': 'https://github.com/Whist-Team/Whist-Core/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='game whist',
    packages=find_packages(exclude=('tests*',)),
    namespace_package=['whist'],
    python_requires='>=3.9',
    install_requires=[]
)
