from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='hsccorpdamnitstupiddogman',
    version='0.0.1',
    description='A tool ',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Ian Moffet and Arnav Nanduri',
    author_email='arnanduri2006@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='Hack',
    packages=find_packages(),
    install_requires=['']
)

