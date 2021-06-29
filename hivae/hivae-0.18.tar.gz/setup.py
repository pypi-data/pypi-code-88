import setuptools

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ['tensorflow>=1.13.0,<2',
                'pandas',
                'sklearn',
                    ]
    
setuptools.setup(
    name='hivae',
    version='0.18',
    url='https://github.com/gkoutos-group/hivae/',
    license='MIT',
    author='Andreas Karwath',
    author_email='a.karwath@bham.ac.uk',
    description='HIVAE (Handling incomplete heterogeneous data using VAEs. - by Nazabal, et al., DOI: 10.1016/j.patcog.2020.107501  (2020))\n Extenstion of implementations as easy to use Python library',
    packages=setuptools.find_packages(exclude=['examples']),
    install_requires=requirements,
    long_description=readme,
    long_description_content_type="text/markdown",
    zip_safe=False
    )


