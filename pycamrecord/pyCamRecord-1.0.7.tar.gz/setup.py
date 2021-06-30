# coding:utf-8

from setuptools import setup
# or
# from distutils.core import setup

with open('README.md',encoding='utf-8') as f:
    long_description = f.read()
    
setup(
        name='pyCamRecord',   
        version='1.0.7',   
        description='Record by Webcam and save automatically while there is different in screen',
        long_description=long_description,
        long_description_content_type = "text/markdown",
        author='KuoYuan Li', 
        author_email='funny4875@gmail.com',  
        url='https://pypi.org/project/pyCamRecord',      
        packages=['pyCamRecord'],   
        include_package_data=True,
        keywords = ['record webcam', 'record webcam by difference','cam recording'],   # Keywords that define your package best
        install_requires=['opencv-contrib-python'],
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
      ],
)
