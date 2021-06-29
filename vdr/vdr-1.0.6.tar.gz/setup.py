from setuptools import setup

setup(
    name='vdr',
    version='1.0.6',
    author='Maxence Lannuzel',
    author_email='maxence.lannuzel@ecole-navale.fr',
    description='A simple library to simulate a VDR.',
    license='MIT',
    keywords='vdr',
    url='https://github.com/MaxouPicsou/VDR',
    packages=[
        'vdr',
        'screenagent'
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: French',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development'
    ],
    install_requires=[
        'pyautogui',
        'configparser'
    ],
    include_package_data=True
)
