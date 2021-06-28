'''
Author: chunyuzhang
Mail: 1821074357@qq.com
Date: 2019-6-9 19:15
'''

from setuptools import setup, find_packages            

setup(
    name = "Nanoha",  
    version = "1.0.0", 
    keywords = ("pip", "Nanoha"),
    description = "Takamachi Nanoha",
    long_description = "Takamachi Nanoha",
    license = "MIT Licence",

    url = "https://github.com/chunyu-zhang",    
    author = "Chunyu Zhang",
    author_email = "1821074357@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy", 'matplotlib']
    )