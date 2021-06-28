import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='fathomdata',
    version='0.0.4',
    author="Fathom Data",
    description="Python package to make interacting with life sciences manufacturing data quick and intuitive.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['fathomdata'],
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.1',
        'pandas>=1.2.3',
        'bokeh>=2.3.2',
        'python-dateutil>=2.8.1'
    ]
)
