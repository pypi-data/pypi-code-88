from setuptools import setup, find_packages

setup(
    name             = 'mseo_gifconvert_test',
    version          = '1.0.1',
    description      = 'Test package __mseo',
    author           = 'mseo',
    author_email     = 'mseo@mvista.com',
    url              = '',
    download_url     = '',
    install_requires = ['pillow'],
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['GIFCONVERTER', 'gifconverter'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 