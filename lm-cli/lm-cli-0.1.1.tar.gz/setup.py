from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="Authors @ One Convergence",
    author_email="manju.vikash145@gmail.com",
    url="https://github.com/oneconvergence/license-manager",
    name='lm-cli',
    version='0.1.1',
    description='cli for dkube license manager',
    install_requires=[
        'Click',
        'prettytable >=1.0.0, <= 2.1.0',
        'requests == 2.25.1',
    ],
    packages=find_packages(),
    # package_dir={'': 'src'},
    # py_modules=["src"],
    entry_points={
        'console_scripts': [
            'lm = src.lm:lm_cli'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3'
)
