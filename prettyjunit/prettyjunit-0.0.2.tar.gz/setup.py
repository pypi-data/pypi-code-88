import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prettyjunit",                     
    version="0.0.2",                       
    author="Dinesh RVL",                     
    description="Junit to HTML Conversion Package",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    entry_points ={
            'console_scripts': [
                'prettyjunit = prettyjunit.convert:generate_html'
            ]
        },   
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      
    python_requires='>=3.6',
    py_modules=["prettyjunit"],                
    keywords ='junit report junit2html junittohtml dineshrvl pretty testreport',
    install_requires=[],
    package_data = {
    'static': ['*']
}                    
)