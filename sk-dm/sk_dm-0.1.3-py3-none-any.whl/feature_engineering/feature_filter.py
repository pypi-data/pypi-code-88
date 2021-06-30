from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
'''
本模块是特征的过滤法，通常用作预处理步骤，它是根据各种统计检验中的分数以及相关性的各指标来选择特征
'''


def variance_filter(x, n):
    """
    特征、标签之间热力图

    :param x: {array-like of shape (n_samples, n_features)} 输入特征数据
    :param n: {int} 阈值设置，大于n的保留特征，否则删除
    :return: 过滤后的值
    """
    selector = VarianceThreshold(threshold=n)
    x_var0 = selector.fit_transform(x)
    return x_var0


def kbest_filter(x, y, n):
    """
    # 卡方过滤，专门针对离散型标签（分类问题）的相关性过滤
    # 卡方检验类feature_selection.chi2计算每个非负特征和标签之间的卡方统计量，并依照卡方统计量由高到低为特征排名。再结合feature_selection.SelectKBest
    # 这个可以输入”评分标准“来选出前K个分数最高的特征的类，我们可以借此除去最可能独立于标签，与我们分类目的无关的特征
    特征、标签之间热力图

    :param x: {array-like of shape (n_samples, n_features)} 输入特征数据
    :param y: {str} 输入标签
    :param n: {int} 选取n个分数最高的特征的类
    :return: 过滤后的值
    """
    x_fschi = SelectKBest(chi2, k=n).fit_transform(x, y)
    return x_fschi


def wrapper_filter(x, y, n):
    """
    递归特征消除法，返回特征选择后的数据
    参数estimator为基模型
    参数n_features_to_select为选择的特征个数
    :param x: {array-like of shape (n_samples, n_features)} 输入特征数据
    :param y: {str} 输入标签
    :param n: {int} 选择的特征个数
    :return: 过滤后的值
    """
    selector = RFE(estimator=LogisticRegression(), n_features_to_select=n)
    wrapper = selector.fit_transform(x, y)
    return wrapper


def embedded_filter(x, y, n):
    """
    使用带惩罚项的基模型，除了筛选出特征外，同时也进行了降维。
    使用feature_selection库的SelectFromModel类结合带L1惩罚项的逻辑回归模型
    :param x: {array-like of shape (n_samples, n_features)} 输入特征数据
    :param y: {str} 输入标签
    :param n: {float} 逻辑回归C值
    :return: 过滤后的值
    """
    selector = SelectFromModel(LogisticRegression(penalty="l2", C=n))
    embedded = selector.fit_transform(x, y)
    return embedded


def gbdt_filter(x, y):
    """
    树模型中GBDT可用来作为基模型进行特征选择
    使用feature_selection库的SelectFromModel类结合GBDT模型
    :param x: array-like of shape (n_samples, n_features) 输入特征数据
    :param y: {str} 输入标签
    :return: 过滤后的值
    """
    selector = SelectFromModel(GradientBoostingClassifier())
    gbdt = selector.fit_transform(x, y)
    return gbdt
