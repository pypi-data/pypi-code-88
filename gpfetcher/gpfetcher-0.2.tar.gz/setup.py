from setuptools import setup, find_packages


VERSION = '0.2'
DESCRIPTION = 'A python package that fetches your public projects(repos) from github'
LONG_DESCRIPTION = 'A python package that fetches your public projects(repos) from github repositories and generates a JSON file.'

# Setting up
setup(
    name="gpfetcher",
    version=VERSION,
    author="Gautam Chandra Saha",
    author_email="devgautam1231@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['bs4','requests','tqdm','lxml'],
    keywords=['python', 'github', 'projects', 'repositories' , 'JSON'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
