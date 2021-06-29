import setuptools


setuptools.setup(
    name='vakantie',
    version='0.0.3',
    # scripts=['yearlyholidays'],
    author="Labiba Kanij Rupty",
    author_email="labibakanij@gmail.com",
    description="A Package to get all holidays starting from 2015",
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    License='MIT',
    long_description_content_type="text/markdown",
    # url="https://github.com/rupaai/happydays",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pandas','beautifulsoup4','requests']
)
