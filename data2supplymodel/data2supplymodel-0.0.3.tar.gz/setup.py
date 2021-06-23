import setuptools 


# read the contents of your README file
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
	name='data2supplymodel',
	version='0.0.3',
	author='Xin Wu, Xuesong Zhou',
	author_email='xinwu3@asu.edu, xzhou74@asu.edu',
	url='https://github.com/Grieverwzn/data2supplymodel',
	description='The data2supply is a data-driven calibration package for traffic flow model calibration, Bureau of Public Roads (BPR) function calibration, and the queueing characterization for transportation planners, engineers, and researchers.',
    long_description=long_description,
    long_description_content_type='text/markdown',
	license='GPLb3+',
	packages=['data2supplymodel'],
	python_requires=">=3.6.0",
	install_requires=['pandas','numpy','scipy','sklearn','matplotlib'],
	)