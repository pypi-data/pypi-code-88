from setuptools import setup,find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='pyluog',
    version='0.13.9',
    description='A python module for using Luogu Api.',
    url='https://pypi.org/project/pyluog',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='hlwdy',
    author_email='hlwdyck@gmail.com',
    license='MIT',
    include_package_data=True,
    packages=find_packages(),
    python_requires=">=3.6",
    platforms="any",
    install_requires=['requests','matplotlib','Pillow']
)