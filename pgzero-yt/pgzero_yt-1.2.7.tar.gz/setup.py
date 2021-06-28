# coding=utf-8

from setuptools import setup, find_packages

__author__ = 'pygame'
__date__ = '2021/06/28'

setup(
    name='pgzero_yt',
    version='1.2.7',
    description=(
        '添加move collide_mask Size'
    ),
    long_description=open('README.rst').read(),
    author='pygame',
    author_email='1758918244@qq.com',
    license='License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/ZENGXIANGXUAN/pgzero_.git',
    install_requires=['pygame', 'numpy'],
    include_package_data=True,
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ])