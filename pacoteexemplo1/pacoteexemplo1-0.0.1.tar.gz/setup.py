from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='pacoteexemplo1',
    version='0.0.1',
    license='MIT License',
    author='Fábio Minutti teixeira',
    long_description=readme,
    author_email='fabiomt92@hotmail.com',
    keywords='Pacote',
    description=u'Exemplo de pacote PyPI',
    packages=['pacoteexemplo1'],
    install_requires=['numpy'],)


    