from sklearn.model_selection import GridSearchCV
import catboost


def catboost_reg(xtrain, ytrain, xtest, param_grid):
    """
    catboost回归模型

    :param xtrain: {array-like of shape (n_samples, n_features)} 输入训练数据集
    :param ytrain: {array-like of shape (n_samples, n_output) \
                   or (n_samples,), default=None} 输入训练标签
    :param xtest: {array-like of shape (n_samples, n_features)} 输入测试数据集
    :param param_grid: {dict} 参数字典
    :return: 模型
    """
    cb = catboost.CatBoostRegressor()
    cb_model = GridSearchCV(cb, param_grid)
    cb_model.fit(xtrain, ytrain)
    preds = cb_model.predict(xtest)
    print(preds)
    return cb_model
