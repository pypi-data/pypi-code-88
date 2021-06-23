from setuptools import setup,find_packages
setup(
    name="donotimport",
    version="0.0.1",
    author="Yasser BDJ (Ro0t96)",
    author_email="by.root96@gmail.com",
    description='''A simple package to prevent the abusive use of the import statement in Python.''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r').read(),
    license="Apache Software License",
    packages=find_packages(),
    url="https://github.com/byRo0t96/donotimport",
    project_urls={
        'Author WebSite': "https://byro0t96.github.io/",
    },
    install_requires=[],
    keywords=['python', 'donotimport'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.x.x"
)