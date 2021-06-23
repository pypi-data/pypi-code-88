
from setuptools import setup, find_packages

setup(
    name='Ocr-Req',
    version='0.6',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['setuptools','numpy','fitz','opencv-python', 'imutils', 'PyMuPDF', 'pdfminer', 'PyPDF2'],
    author='Vardhani k ',
    author_email='vardhanikanamarlapudi@gmail.com'
)
