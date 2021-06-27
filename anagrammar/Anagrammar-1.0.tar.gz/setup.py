from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Anagrammar',
    version='1.0',
    description='Takes Some Characters And Return A List Of All Possible Combinations',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Ilay Furst',
    author_email='furstilay11@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='Anagram',
    packages=find_packages(),
    install_requires=['']
)