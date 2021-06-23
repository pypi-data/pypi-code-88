import setuptools
print(setuptools.find_packages())

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="pyqt5_gui_yyj",
  install_requires=[
      # 'requests', 'maya', 'records',
  ],
  version="0.1.7",
  author="YangYijian",
  author_email="2715336141@qq.com",
  description="A developing pyqt gui",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://gitee.com/yangyijian1202/PyQt5_GUI",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)

#packages：申明你的包里面要包含的目录，比如 ['mypackage', 'mypackage_test'] 可以是这种使用我的示例，让setuptools自动决定要包含哪些包
#install_requires：申明依赖包，安装包时pip会自动安装：格式如下（我上面的setup.py没有这个参数，因为我不依赖第三方包:)）：

