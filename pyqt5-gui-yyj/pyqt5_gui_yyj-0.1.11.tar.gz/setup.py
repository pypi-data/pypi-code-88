import setuptools
print(setuptools.find_packages())

# with open("README.md", "r") as fh:
    # long_description = fh.read()



setuptools.setup(
  name="pyqt5_gui_yyj",
  install_requires=[
      # 'requests', 'maya', 'records',
  ],
  version="0.1.11",
  author="YangYijian",
  author_email="2715336141@qq.com",
  description="A developing pyqt gui, change __init__.py",
  long_description='long_description',
  long_description_content_type="text/markdown",
  url="https://gitee.com/yangyijian1202/PyQt5_GUI",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)