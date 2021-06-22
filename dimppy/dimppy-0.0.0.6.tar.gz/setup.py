from setuptools import setup, find_packages

setup(
    name= 'dimppy', 
    version='0.0.0.6',
    author='Armaan Chauhan',
    author_email='armaanchauhan268@gmail.com',
    description='Data Structures implementation in Python', 
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Armaan-268/dimppy',
    license="MIT",
    classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Education',
    'Topic :: Software Development :: Libraries',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
    ], 
    keywords='datastructures,python',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['numpy']
)