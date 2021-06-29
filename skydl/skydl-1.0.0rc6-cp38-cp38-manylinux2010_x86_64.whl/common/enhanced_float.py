# -*- coding:utf-8 -*-
from decimal import Decimal


class EnhancedFloat(float):
    """
    增强的float，"加、减、乘、除"的操作不会丢失精度。
    如果EnhancedFloat(float) 将默认支持所有的float操作。
    如果设置EnhancedFloat(object) 就只解决"加、减、乘、除"丢失精度的问题
    目前解决的问题：
    0.1 + 0.2 = 0.30000000000000004
    0.1 * 0.2 = 0.020000000000000004
    0.09 - 0.02 = 0.06999999999999999
    0.2 + 0.1 + 0.3 = 0.6000000000000001
    0.3 / 0.2 = 1.4999999999999998
    参考：Python中浮点数精度处理 https://blog.csdn.net/Jerry_1126/article/details/74079819
    """
    def __init__(self, val):
        self.val = float(val)

    def __add__(self, other):  # self + other
        other = other if isinstance(other, EnhancedFloat) else self.__class__(other)
        return float(Decimal(str(self.val)) + Decimal(str(other.val)))

    def __radd__(self, other):   # other + self
        return self + other

    def __sub__(self, other):  # self - other
        return self + (-other)

    def __rsub__(self, other):  # other - self
        return self.__class__(-self) + other

    def __mul__(self, other):  # self * other
        other = other if isinstance(other, EnhancedFloat) else self.__class__(other)
        return float(Decimal(str(self.val)) * Decimal(str(other.val)))

    def __rmul__(self, other):  # other * self
        return self * other

    def __neg__(self):  # -self
        return self * -1

    def __truediv__(self, other):  # self / other
        other = other if isinstance(other, EnhancedFloat) else self.__class__(other)
        return float(Decimal(str(self.val)) / Decimal(str(other.val)))

    def __rtruediv__(self, other):  # other / self
        other = other if isinstance(other, EnhancedFloat) else self.__class__(other)
        return float(Decimal(str(other.val)) / Decimal(str(self.val)))

    def __repr__(self):
        """print(tensor) 返回的内容"""
        return str(self.val)


if __name__ == '__main__':
    print(f"isinstance(EnhancedFloat(0.3), float)：{isinstance(EnhancedFloat(0.3), float)}")
    try:
        print(f"EnhancedFloat(0.3) ** 2：{EnhancedFloat(0.3) ** 2}")
    except:
        print("目前EnhancedFloat(object) 还未支持乘幂操作！")
    print(f"print(Decimal(0.3)) 将显示 0.299999999999999988897769753748434595763683319091796875：{Decimal(0.3)}")
    print(f"float(0.3)：{float(0.3)}")
    print(f"EnhancedFloat(Decimal(0.3))：{EnhancedFloat(Decimal(0.3))}")
    print(f"-EnhancedFloat(0.1) + 0.2 = {-EnhancedFloat(0.1) + 0.2}")
    print(f"EnhancedFloat(0.1) + 0.2 = {EnhancedFloat(0.1) + 0.2}")
    print(f"0.2 + EnhancedFloat(0.1) + 0.3 = {0.2 + EnhancedFloat(0.1) + 0.3}")
    print(f"EnhancedFloat(0.09) - 0.02 = {EnhancedFloat(0.09) - 0.02}")
    print(f"0.02 - EnhancedFloat(0.09) = {0.02 - EnhancedFloat(0.09)}")
    print(f"EnhancedFloat(0.1) * -EnhancedFloat(1) = {EnhancedFloat(0.1) * -EnhancedFloat(1)}")
    print(f"EnhancedFloat(0.1) * 0.2 = {EnhancedFloat(0.1) * 0.2}")
    print(f"0.2 * EnhancedFloat(0.1) = {0.2 * EnhancedFloat(0.1)}")
    print(f"EnhancedFloat(0.3) / 0.2 = {EnhancedFloat(0.3) / 0.2}")
    print(f"0.3 / EnhancedFloat(0.2) = {0.3 / EnhancedFloat(0.2)}")
    print(f"1 / EnhancedFloat(3) = {1/EnhancedFloat(3)}")
    print(f"(1/EnhancedFloat(3))*3 = {(1/EnhancedFloat(3))*3}")

