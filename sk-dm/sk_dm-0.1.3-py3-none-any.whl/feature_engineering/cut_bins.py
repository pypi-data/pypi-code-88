import pandas as pd
"""
本模块用于特征的分箱
"""


def cutbins(x, bins, right, labels, retbins, precision, include_lowest):
    """
    本模块用于特征的分箱

    :param x: {array} 必须为一维，待切割的原形式
    :param bins: {int, sequence of scalars, or IntervalIndex}
    如果bins是一个整数，它定义了x宽度范围内的等宽面元数量，但是在这种情况下，x的范围在每个边上被延长1%，以保证包括x的最小值或最大值。
    如果bin是序列，它定义了允许非均匀in宽度的bin边缘。在这种情况下没有x的范围的扩展。
    :param right: {bool} 是否是左开右闭区间
    :param labels: 用作结果箱的标签。必须与结果箱相同长度。如果FALSE，只返回整数指标面元。
    :param retbins: {bool} 是否返回箱
    :param precision: {int} 返回面元的小数点几位
    :param include_lowest: {bool} 第一个区间的左端点是否包含
    :return: 返回切箱后的数据
    """
    cats = pd.cut(x, bins, right, labels, retbins, precision, include_lowest)
    return cats


def auto_cutbins(data, n, labels, retbins, precision, duplicates):
    """
    本模块用于自己划分组 -无监督 使用的是qcut方法

    :param data: {1d ndarray or Series} 输入数据
    :param n: {int or list-like of float} 按n分位数进行切割
    :param labels: {array or False, default None}
          用作结果箱的标签。 长度必须与结果箱一样。 如果为 False，则只返回整数指标箱。 如果为 True，则报错
    :param retbins: {bool, optional} 是否返回（箱，标签）。
    :param precision: {int, optional} 存储和显示 bin 标签的精度
    :param duplicates: {default 'raise', 'drop'}, 可选
            如果 bin 边缘不唯一，则引发 ValueError 或删除非唯一值
    :return: 返回切箱后的数据
    """
    s = pd.Series(data)
    a = pd.qcut(s, n, labels, retbins, precision, duplicates)
    cats = pd.value_counts(a)
    return cats
