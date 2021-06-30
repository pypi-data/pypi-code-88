from sklearn.model_selection import GridSearchCV
import catboost


def catboost_cls(xtrain, ytrain, n, param_grid):
    """
    catboost分类模型

    :param xtrain: {array-like of shape (n_samples, n_features)} 输入训练数据集
    :param ytrain: {array-like of shape (n_samples, n_output) \
                   or (n_samples,), default=None} 输入训练标签
    :param n: {float} 交叉验证集的比例
    :param param_grid: {dict} 参数字典
    :return: 模型
    """
    cb = catboost.CatBoostClassifier()
    cb_model = GridSearchCV(cb, param_grid, cv=n)
    cb_model.fit(xtrain, ytrain)
    print("最好得分：%s" % cb_model.best_score_)
    print("最好特征：%s" % cb_model.best_params_)
    return cb_model
