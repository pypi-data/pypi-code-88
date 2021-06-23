from setuptools import setup, find_packages

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name='classicML-python',
    version='0.6.2b1',
    description='An easy-to-use ML framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Steve R. Sun',
    author_email='s1638650145@gmail.com',
    url='https://github.com/sun1638650145/classicML',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    license='Apache Software License',
    install_requires=[
        'h5py>=3.2.0, <=3.2.1',
        'matplotlib>=3.4.0, <=3.4.2',
        'numpy>=1.20.0, <=1.20.3',
        'pandas>=1.2.0, <=1.2.4',
        'psutil>=5.7.2, <=5.8.0',
    ],
    python_requires='>=3.7',
)
