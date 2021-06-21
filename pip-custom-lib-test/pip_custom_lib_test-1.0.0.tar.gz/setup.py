# coding: utf-8

# from setuptools import setup, find_packages
#
# setup(
#     name='pip_custom_lib_test',  # 项目名称,也就是pip list后会出来的包名
#     version='1.0.0',
#     packages=find_packages(),  # 包含所有的py文件
#     include_package_data=True,  # 将数据文件也打包
#     zip_safe=True
# )



import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="pip_custom_lib_test",
  version="1.0.0",
  author="Example Author",
  author_email="author@example.com",
  description="A small example package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/pypa/sampleproject",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)