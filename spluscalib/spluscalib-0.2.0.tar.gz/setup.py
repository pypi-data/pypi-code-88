import setuptools

setuptools.setup(
   name='spluscalib',
   version='0.2.0',
   description='S-PLUS calibration pipeline',
   author='Felipe Almeida Fernandes',
   author_email='felipefer42@gmail.com',
   packages=setuptools.find_packages(),
   install_requires=['astropy', 'astroquery', 'sfdmap', 'numpy',
                     'pandas', 'scipy', 'sklearn', 'matplotlib',
                     'shapely', 'Pillow'],
   url='https://github.com/felipefer42/spluscalib',
   python_requires='>3.6.0',
   include_package_data=True
)

# python setup.py sdist
# python setup.py bdist_wheel
# twine upload dist/spluscalib-0.2*

# twine upload --repository-url https://test.pypi.org/legacy/ dist/spluscalib-0.1.10*
# pip3 install --index-url https://test.pypi.org/simple/ spluscalib --user --version==0.1.10