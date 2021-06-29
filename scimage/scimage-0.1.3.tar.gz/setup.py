from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
	name="scimage",
	version="0.1.3",

	description="Algorithms for data analysis and image processing, including automation of feature extraction and characterization of images.",
    long_description=long_description,
    long_description_content_type="text/markdown",

	packages=["scimage",],
	include_package_data=True,

	install_requires=['numpy','matplotlib'],

	license='GNU GPLv3',

	author='Amir Chatraee, Mehrdad Bagheri',
	author_email='amirchatraee@yahoo.com, bagheri_mehrdad@hotmail.com',
	url='https://github.com/amirchatraee/scimage',

	classifiers=[
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
		'Programming Language :: Python :: 3',		
		'Programming Language :: Python :: 3.8',
	],  
)
