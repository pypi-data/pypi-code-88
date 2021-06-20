import setuptools
from iniparser2 import __version__ as version

def read(fname):
	with open(fname,'r') as f:
		return f.read()

setuptools.setup(
name='iniparser2',
version=version,
author='HugeBrain16',
author_email='joshtuck373@gmail.com',
description='An INI parser or config parser',
license='MIT',
keywords='iniparser configparser ini config parser file',
url='https://github.com/HugeBrain16/iniparser2',
packages=setuptools.find_packages(),
long_description=read('README.md'),
long_description_content_type='text/markdown',
classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
	]
)