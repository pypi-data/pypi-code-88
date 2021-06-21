# @Time     : 2021/5/28
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from scripts.build import requires, build_package

name = "f1z1_async_runner"
version = "0.0.6"

if __name__ == '__main__':
    build_package(name, version, filename="README.md", install_requires=requires)
