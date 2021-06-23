# @Time     : 2021/5/27
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
def is_string(value):
    return isinstance(value, str)


def is_bytes(value):
    return isinstance(value, bytes)


def is_bytearray(value):
    return isinstance(value, bytearray)


def is_any_string(value):
    return any([
        is_bytes(value),
        is_string(value)
    ])
