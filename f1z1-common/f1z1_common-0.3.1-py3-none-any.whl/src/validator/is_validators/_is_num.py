# @Time     : 2021/5/28
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
def is_int(value):
    return isinstance(value, int)


def is_float(value):
    return isinstance(value, float)


def is_number(value):
    return any([
        is_int(value),
        is_float(value)
    ])
