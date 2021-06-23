# @Time     : 2021/5/26
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from scripts.build import build_package

name = "f1z1_common"
version = "0.3.1"

if __name__ == '__main__':
    build_package(name, version, filename="README.md")
