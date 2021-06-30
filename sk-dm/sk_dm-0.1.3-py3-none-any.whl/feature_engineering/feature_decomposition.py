from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
'''
本模块是用于对特征进行降维处理
'''


def pcamodel(x, n):
    """
    使用decomposition库的PCA类选择特征
    主成分分析法，返回降维后的数据
    参数n_components为主成分数目

    :param x: {array-like of shape (n_samples, n_features)} 输入特征数据
    :param n: {int}主成分数目
    :return: 降维后的值
    """
    pca = PCA(n_components=n)
    selector = pca.fit_transform(x)
    return selector


def ldamodel(x, y, n):
    """
    使用discriminant_analysis库的L类选择特征
    线性判别分析法，返回降维后的数据
    参数n_components为降维后的维数

    :param x: {array-like of shape (n_samples, n_features)} 输入特征数据
    :param y: {array-like of shape (n_samples,) or (n_samples, n_outputs), \
                default=None} 目标值（无监督转换）
    :param n: {int} 降维后的维数
    :return: 降维后的值
    """
    pca = LinearDiscriminantAnalysis(n_components=n)
    selector = pca.fit_transform(x, y)
    return selector
