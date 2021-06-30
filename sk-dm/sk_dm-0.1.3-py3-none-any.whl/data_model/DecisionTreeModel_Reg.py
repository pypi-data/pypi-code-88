from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor


def decision_tree_reg(xtrain, ytrain, n, param_grid):
    """
    决策树回归模型

    :param xtrain: {array-like of shape (n_samples, n_features)} 输入训练数据集
    :param ytrain: array-like of shape (n_samples, n_output) \
                   or (n_samples,), default=None 输入训练标签
    :param n:{float} 交叉验证集比例
    :param param_grid: {dict} 参数字典
    :return: 模型得分
    """
    regressor = DecisionTreeRegressor(param_grid, random_state=0)
    return cross_val_score(regressor, xtrain, ytrain, cv=n, scoring="neg_mean_squared_error")
