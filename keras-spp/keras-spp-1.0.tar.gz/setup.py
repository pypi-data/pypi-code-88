from setuptools import setup

setup(
    name='keras-spp',
    url='https://github.com/yhenon/keras-spp',
    version='1.0',
    description='Spatial pyramid pooling layers for keras, based on https://arxiv.org/abs/1406.4729 . This code requires Keras version 2.0 or greater.',
    author='yhenon',
    author_email='yhenon@peanuts.com',
    packages=['spp'],
    license='',
    requires=[
        'keras'
    ]
)
