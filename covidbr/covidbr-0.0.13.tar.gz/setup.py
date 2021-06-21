from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='covidbr',
    version='0.0.13',
    url='https://github.com/gpftc/covid_br',
    license='MIT License',
    author='Reinan Br',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='covid-19 covid api data science',
    description=u'Library for data mining about covid-19 in brazilian cities',
    packages=['covidbr'],
    install_requires=['numpy','matplotlib','pillow','mechanicalsoup','psutil','requests','pandas'],)