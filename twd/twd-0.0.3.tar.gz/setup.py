from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='twd',
    version='0.0.3',
    url='https://github.com/profssribeiro/twd',
    license='MIT License',
    author='Sergio S. Ribeiro',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='profssribeiro@gmail.com',
    keywords='Pacote',
    description=u'Three Way Decision/Rough Set library',
    packages=['twd'],
    install_requires=[],)