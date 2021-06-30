from setuptools import setup
from setuptools import find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name= 'xieminxuan10',
    version= '1.0.3',
    py_modules =['xieminxuan10'],
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author= 'xieminxuan',
    author_email='2091549152@qq.com',
    url='https://gitee.com/siemingsuan',
    description= '小尝试哦'
)