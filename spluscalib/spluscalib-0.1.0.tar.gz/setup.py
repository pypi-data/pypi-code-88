import setuptools

setuptools.setup(
   name='spluscalib',
   version='0.1.0',
   description='S-PLUS calibration pipeline',
   author='Felipe Almeida Fernandes',
   author_email='felipefer42@gmail.com',
   packages=setuptools.find_packages(),
   install_requires=['astropy', 'astroquery', 'sfdmap', 'numpy',
                     'pandas', 'scipy', 'sklearn', 'matplotlib',
                     'shapely', 'Pillow'],
   url='https://github.com/felipefer42/spluscalib'
)
