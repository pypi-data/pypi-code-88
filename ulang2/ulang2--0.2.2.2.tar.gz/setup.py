import ulang,sys,os
from setuptools import setup

try:os.chdir(os.path.split(__file__)[0])
except:pass

desc="木兰编程语言的源代码。This is the source code of Ulang Programming Language."

try:
    with open("README.rst") as f:
        long_desc=f.read()
except OSError:
    long_desc=''

setup(
  name='ulang2',
  version=ulang.__version__,
  description=desc,
  long_description=long_desc,
  author="上传者:七分诚意 qq:3076711200 百度账号:徐丹34",
  packages=["ulang"],
  keywords=["ulang","木兰","木兰编程语言"],
  classifiers=[
      'Programming Language :: Python',
      "Topic :: Software Development :: Code Generators",
      "Natural Language :: Chinese (Simplified)"],
  install_requires=["rply","codegen"]
)
