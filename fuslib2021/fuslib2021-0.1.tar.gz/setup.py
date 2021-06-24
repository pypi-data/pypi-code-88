
from setuptools import setup
 
setup(
    name='fuslib2021',
    packages=['fuslib2021'], 
    version='0.1',
    license='LGPL v3',
    description='Library for remote sensing images fusion',
    author='Andrea Blanco Gomez',
    author_email='andrea.blanco.gomez@alumnos.upm.es',
    url='https://github.com/andreablancog/fuslib2021', 
    download_url='https://github.com/andreablancog/fuslib2021/tarball/0.1', 
    keywords='remote sensing images fusion landsat modis', 		install_requires=['math','numpy','gdal','os','tkinter','idlwrap','statsmodels','zarr','dask','rasterio','matplotlib'],
)
