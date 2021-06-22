import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
	'Operating System :: OS Independent',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3'
]

setuptools.setup(
	name='stark-middlewares',
	version='0.4',
	description='Stark Middlewares',
	long_description=long_description,
    long_description_content_type="text/markdown",
	url='',
	author='Stark Digital Media Services Pvt. Ltd.',
	author_email='starkengg81@gmail.com',
	License='MIT',
	classifiers=classifiers,
	keywords=['stark', 'stark-middlewares', 'middlewares', 'stark_middlewares'],
	python_requires='>=3.6',
	packages=setuptools.find_packages(),
	install_requires=[
	'requests',
	]
)
