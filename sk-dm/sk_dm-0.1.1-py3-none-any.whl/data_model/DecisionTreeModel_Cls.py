import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV


def decision_tree_model_cls(xtrain, ytrain, n, param_grid):
    """
    决策树分类模型

    :param xtrain: {array-like of shape (n_samples, n_features)} 输入训练数据集
    :param ytrain: array-like of shape (n_samples, n_output) \
                   or (n_samples,), default=None 输入训练标签
    :param n:{float} 交叉验证集比例
    :param param_grid: {dict} 参数字典
    :return: 模型得分
    """
    clf = DecisionTreeClassifier()
    model = GridSearchCV(clf, param_grid, cv=n)
    model.fit(xtrain, ytrain)
    print("最好得分：%s" % model.best_score_)
    print("最好特征：%s" % model.best_params_)
    return model
