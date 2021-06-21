from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='NOTMENOTME',
    version='0.4.2',
    description='NOTMENOTME',
    long_description=open('README.txt').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    url='',
    author='NOTMENOTME',
    author_email='armannikoopour@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='NOTMENOTME',
    packages=find_packages(),
    install_requires=['']
)
