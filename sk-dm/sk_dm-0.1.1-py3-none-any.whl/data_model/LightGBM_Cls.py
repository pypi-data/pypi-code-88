import lightgbm as lgb
from sklearn.metrics import accuracy_score


def lightgbmcls(xtrain, ytrain, xtest, ytest, param_grid):
    """
    Lightbgm分类模型

    :param xtrain: {array-like of shape (n_samples, n_features)} 输入训练数据集
    :param ytrain: {array-like of shape (n_samples, n_output) \
                   or (n_samples,), default=None} 输入测试数据集
    :param xtest: {array-like of shape (n_samples, n_features)} 输入测试数据集
    :param ytest: {array-like of shape (n_samples, n_output)} 输入测试标签
    :param param_grid: {dict} 参数字典
    :return: 模型准确率
    """
    train_data = lgb.Dataset(xtrain, label=ytrain)
    validation_data = lgb.Dataset(xtest, label=ytest)
    gbm = lgb.train(param_grid, train_data, valid_sets=validation_data)
    y_pred = gbm.predict(xtest)
    y_pred = [list(x).index(max(x)) for x in y_pred]
    score = accuracy_score(ytest, y_pred)
    print('准确率为：%.2f' % score)
    return score
