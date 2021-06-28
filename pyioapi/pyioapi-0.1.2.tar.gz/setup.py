from setuptools import setup, find_packages

setup(
    name='pyioapi',
    version="0.1.2",
    description=(
        'The Python library provides read,write IOAPI-like netCDF file in CMAQ'
    ),
    # long_description=open('README.rst').read(),
    author='Kangjia Gong',
    author_email='kjgong@kjgong.cn',
    maintainer='Kangjia Gong',
    maintainer_email='kjgong@kjgong.cn',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/Gongkangjia/pyioapi',
)


