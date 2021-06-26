from setuptools import setup, find_packages

long_description = open("README.md").read()

setup(
        name='resident',
        version='0.0.0.1',
        description='Address processing',
        long_description=long_description,
        long_description_content_type="text/markdown",
        author_email='william.wyatt@cgu.edu',
        url='https://github.com/Tsangares/address',
        include_package_data=True,
        packages=find_packages(),
        install_requires=[
            'nickname',
            ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
)

